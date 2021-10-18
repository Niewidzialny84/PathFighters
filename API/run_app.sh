#!/bin/bash
echo "Initializing database"
python3 main_app.py db init
python3 main_app.py db migrate -m "Docker initial migratie"
python3 main_app.py db upgrade
echo "Running app"
python3 main_app.py run