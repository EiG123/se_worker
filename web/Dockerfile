FROM python:3.10

WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymongo
RUN pip install Flask-PyMongo
# Copy the application code into the container at /app
COPY . /app

# Set the environment variables
ENV PORT=8000

# Command to run the application
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8000"]