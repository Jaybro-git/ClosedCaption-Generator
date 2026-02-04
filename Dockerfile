# 1. Use a lightweight Python base
FROM python:3.9-slim

# 2. Install FFmpeg (Crucial for Whisper) and Git
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# 3. Set working directory
WORKDIR /app

# 4. Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the Application Code
COPY src/ ./src/
COPY app.py .

# 6. Create a non-root user and fix permissions
RUN useradd -m -u 1000 user

# This allows the app to create the 'temp' folder without Permission Denied errors
RUN chown -R user:user /app

# 7. Switch to the user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# 8. Run the app with security checks disabled for Hugging Face
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]