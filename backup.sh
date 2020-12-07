#!/bin/bash
. /root/project_env.sh
export $(xargs < /code/.env)
cd /code
echo "Backuping in ${MONGODB_NAME} database..."
/usr/local/bin/python manage.py dumpdata --exclude auth > challenge.json
mongoimport --db $MONGODB_NAME --uri mongodb://$MONGODB_USER:$MONGODB_PASSWORD@$MONGODB_HOST --jsonArray challenge.json --drop
echo "Finalizing backup..."