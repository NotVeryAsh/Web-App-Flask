FROM python:3.8

# Set directory for the app to sit under
WORKDIR /usr/src/app

# Copy all the files to the container
COPY . .

# Install requirements
RUN pip install -r requirements.txt

# Expose port that flask runs on
EXPOSE 5000

# Start flask server
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]