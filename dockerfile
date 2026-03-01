# Use Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements text file 
COPY requirements.txt .

# Copy project scripts
COPY 1_Fetching_Data.py .
COPY 2_Analysis.py .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Create plots folder to save the plots images 
RUN mkdir -p plots

# Run project automatically
CMD python 1_Fetching_Data.py && \
    python 2_Analysis.py
    
  
