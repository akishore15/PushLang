
FROM python:3-alpine

# Install Python3 and pip
RUN apk add --no-cache python3 py3-pip

# Copy your Python script into the container
COPY lexer_parser.py /app/lexer_parser.py

# Set the working directory
WORKDIR /app

# Command to execute Python interactive mode and run your script
ENTRYPOINT ["python3", "lexer_parser.py"]
