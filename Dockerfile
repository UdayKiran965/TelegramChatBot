# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "bot.py"]
