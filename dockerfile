# Use the official Python 3.9.18 image from the Docker Hub
FROM python:3.9.18

# Set the working directory in the container to /banknote-authenticator
WORKDIR /banknote-authenticator

# Add the current directory contents into the container at /banknote-authenticator
ADD . /banknote-authenticator

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade Sckit-Learn
RUN pip install --upgrade scikit-learn

# Make port 5000 available to the world outside this container
EXPOSE 5000

# cd into the directory where app.py is located
WORKDIR /banknote-authenticator/authenticator

# Run app.py when the container launches
CMD ["python", "app.py"]
