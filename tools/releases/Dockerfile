FROM debian:12.0

# Install some useful tools.
RUN apt-get update -y && \
    apt-get install -y sudo \
                       curl \
                       unzip \
                       default-jre \
                       python3-pip

COPY requirements.txt requirements.txt
RUN cat requirements.txt
RUN pip install --require-hashes -r requirements.txt --break-system-packages

ENTRYPOINT ["/bin/bash"]