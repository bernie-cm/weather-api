FROM python:3.12

# Install application dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --requirement /tmp/requirements.txt

# Copy in the source code
COPY /src/app.py ./src/app.py

ENTRYPOINT ["python","./src/app.py"]