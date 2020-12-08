from django.shortcuts import render
from rest_framework import status, viewsets
from .serializers import RegularPlanSerializer
from .models import RegularPlan
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import action
from .tasks import send_email_task

class RegularPlanViewset(viewsets.ModelViewSet):
    """
    A ViewSet for listing or retrieving plans.
    """
    queryset = RegularPlan.objects.all()
    serializer_class = RegularPlanSerializer

    def list(self, request):
        """API endpoint that list API RegularPlans with publish True

        Args:
            request (Request): request incoming on view.
        """
        queryset = RegularPlan.objects.filter(publish=True)
        serializer = RegularPlanSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """API endpoint that create Regular Plan for the User

        Args:
            request (Request): request incoming on view.
        """
        serializer = RegularPlanSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            regular_plan = RegularPlan.objects.create(
                name=serializer.data['name'],
                tar_included=serializer.data['tar_included'],
                subscription=serializer.data['subscription'],
                cycle=serializer.data['cycle'],
                type=serializer.data['type'],
                offer_iva=serializer.data['offer_iva'],
                off_peak_price=serializer.data['off_peak_price'],
                peak_price=serializer.data['peak_price'],
                unit = serializer.data['unit'],
                valid=serializer.data['valid'],
                publish=serializer.data['publish'],
                vat=serializer.data['vat'],
                owner=user
            )
            regular_plan.save()
            if(regular_plan.publish):
                send_email_task.delay(regular_plan.owner.username, regular_plan.owner.email)
            return Response(RegularPlanSerializer(regular_plan).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def list_by_user(self, request):
        """List Regular Plan for the User

        Args:
            request (Request): request incoming on view.
        """
        user = request.user
        queryset = RegularPlan.objects.filter(owner=user)
        serializer = RegularPlanSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Update a specific Regular Plan.

        Args:
            request (Request): request incoming on view.
        """
        user = request.user
        serializer = RegularPlanSerializer(data=request.data)
        if serializer.is_valid():
            for regular_plan in RegularPlan.objects.filter(id=pk, owner=user):
                before_publish = regular_plan.publish
                regular_plan.name = serializer.data['name']
                regular_plan.tar_included = serializer.data['tar_included']
                regular_plan.subscription = serializer.data['subscription']
                regular_plan.cycle = serializer.data['cycle']
                regular_plan.type = serializer.data['type']
                regular_plan.offer_iva = serializer.data['offer_iva']
                regular_plan.off_peak_price = serializer.data['off_peak_price']
                regular_plan.peak_price = serializer.data['peak_price']
                regular_plan.unit = serializer.data['unit']
                regular_plan.valid = serializer.data['valid']
                regular_plan.publish = serializer.data['publish']
                regular_plan.vat = serializer.data['vat']
                regular_plan.save()
                if not(before_publish) and regular_plan.publish:
                    send_email_task.delay(regular_plan.owner.username, regular_plan.owner.email)
                return Response(RegularPlanSerializer(regular_plan).data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
                            
    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_permissions(self):
        """Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list_by_user':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

            