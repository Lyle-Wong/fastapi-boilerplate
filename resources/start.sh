#! /usr/bin/env sh
set -e

DEFAULT_MODULE_NAME=src.main
DEFAULT_GUNICORN_CONF=gunicorn_conf.py

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}

EXECUTABLE_PEX_FILENAME=$(ls *.pex| sort -V | tail -n 1)

export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}
export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}
export WORKER_CLASS=${WORKER_CLASS:-"uvicorn.workers.UvicornWorker"}
export LOGGER_CLASS=${LOGGER_CLASS:-"src.core.logging.StubbedGunicornLogger"}
export EXECUTABLE_PEX_FILENAME=${EXECUTABLE_PEX_FILENAME:-"app.pex"}

# If there's a prestart.sh script in the /app directory or other path specified, run it before starting
PRE_START_PATH=${PRE_START_PATH:-prestart.sh}
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    sh "$PRE_START_PATH"
else
    echo "There is no script $PRE_START_PATH"
fi

# Start Gunicorn
# echo "pipenv run exec gunicorn -k \"$WORKER_CLASS\" -c \"$GUNICORN_CONF\" \"$APP_MODULE\""
# exec pipenv run gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"
echo "./$EXECUTABLE_PEX_FILENAME -k \"$WORKER_CLASS\" -c \"$GUNICORN_CONF\" --logger-class \"$LOGGER_CLASS\" \"$APP_MODULE\""
exec ./"$EXECUTABLE_PEX_FILENAME" -k "$WORKER_CLASS" -c "$GUNICORN_CONF" --logger-class "$LOGGER_CLASS" "$APP_MODULE"
