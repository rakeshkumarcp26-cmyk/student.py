FROM python:3.13-slim

WORKDIR /app

COPY . /app

# Install pytest
RUN pip install pytest

# Run tests first, then run main program
CMD pytest -v && python student.py
