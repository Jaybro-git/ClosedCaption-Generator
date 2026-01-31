# 1. Use a lightweight Python base
FROM python:3.9-slim

# 2. Install FFmpeg and Git
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# 3. Set working directory
WORKDIR /app

# 4. Copy requirements
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Create the user and setup permissions
RUN useradd -m -u 1000 user

# Switch ownership of the /app directory to the new user
RUN chown -R user:user /app

# 7. Switch to the user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# 8. Run the app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]