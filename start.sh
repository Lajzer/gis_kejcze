#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn gis_kejcze.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
