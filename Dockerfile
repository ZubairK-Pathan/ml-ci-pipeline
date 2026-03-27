# 1. Use an official, lightweight Python image
# We use 'slim' to keep the container size small and fast on your Mac
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first to cache the dependencies
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your app (main.py, train_model.py, and house_model.pkl)
COPY . .

# 6. Expose the port FastAPI will run on
EXPOSE 8000

# 7. The command to start the server when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]