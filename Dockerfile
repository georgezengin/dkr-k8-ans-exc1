# Base image with Python
FROM python:3.10-alpine

WORKDIR /app
COPY . .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
ENV FLASK_APP="students.py"
EXPOSE 5200
#CMD ["python", "IPshow.py"]
CMD flask run --port=5200 --host=0.0.0.0
