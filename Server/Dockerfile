FROM python:3.9-buster
EXPOSE 5001/tcp
WORKDIR /app
COPY . .
# Build run type
ENV ENGINEER_API=dev
# Install requirements
RUN python3 -m pip install -r requirements.txt
# Start python app
CMD python3 server.py run