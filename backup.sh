#!/bin/bash
. /root/project_env.sh
export $(xargs < /code/.env)
cd /code
echo "Backuping in ${MONGO_INITDB_DATABASE} database..."
/usr/local/bin/python manage.py dumpdata --exclude auth > challenge.json
mongoimport --db $MONGO_INITDB_DATABASE --uri mongodb://$MONGO_INITDB_ROOT_USERNAME:$MONGO_INITDB_ROOT_PASSWORD@mongo_db --jsonArray challenge.json --drop
echo "Finalizing backup..."