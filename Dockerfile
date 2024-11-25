# Start from the official Python image
FROM python:3.8.10


# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# we install brcypt so is recognized by FastAPI
RUN pip install passlib[bcrypt]

# Copy the rest of the application code
COPY . .
# Set the working directory
WORKDIR /project
# Run the application
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
