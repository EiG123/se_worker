#!/bin/sh
gunicorn main:app -c gunicorn.config.py