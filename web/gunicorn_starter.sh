#!/bin/sh

# Start Gunicorn with the appropriate configuration
gunicorn main:app -c gunicorn.config.py