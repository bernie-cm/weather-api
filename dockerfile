FROM python:3.12

# Install application dependencies
COPY requirements.txt /tmp/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --requirement /tmp/requirements.txt

copy ./src/writer_json.py /src/writer_json.py

ENTRYPOINT ["python","./src/writer_json.py"]