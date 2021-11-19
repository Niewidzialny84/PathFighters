FROM python:3.9-buster
EXPOSE 5000/tcp
WORKDIR /app
COPY . .
# Build run type
ENV ENGINEER_API=dev
# Install requirements
RUN python3 -m pip install -r requirements.txt
# Set up Volume
VOLUME [ "/app/app/main/db" ]
# Chmod app
RUN chmod -R 777 run_app.sh
# Run the app
CMD ./run_app.sh
