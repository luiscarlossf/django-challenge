from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task
def send_email_task(username, email):
    """Send a email about published regular plans.

    Args:
        username (str): name of addressee.
        email (str): email of addressee.
    """
    logger.info('Creating the send_email_task...')

    subject = "Plan published!"
    from_email = settings.EMAIL_HOST_USER
    message = "Hi, {0}!\nYour regular plan was published!".format(username)
    to = email

    send_mail(
        subject,
        message,
        from_email,
        [to],
    )

    logger.info('Finishing send_email_task')