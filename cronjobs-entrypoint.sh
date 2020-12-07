#!/bin/bash

# Apply database migrations
./manage.py migrate

printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh

# Execute cron
service cron restart
crontab /code/crontab
tail -f /code/cron.log


