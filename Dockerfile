FROM alpine:3.4

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip

RUN pip3 install --upgrade pip setuptools hug && \
    rm -r /root/.cache