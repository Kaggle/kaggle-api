FROM debian:12.0

# Install some useful tools.
RUN apt-get update -y && \
    apt-get install -y sudo \
                       curl \
                       unzip \
                       default-jre \
                       python3-pip

# Install tools used to generate the Kaggle CLI.
RUN apt-get install -y yapf3 python3-yapf && \
  curl -fsSL --output /tmp/autogen.zip "https://github.com/mbrukman/autogen/archive/refs/heads/master.zip" && \
  mkdir -p /usr/lib/autogen && unzip -qo /tmp/autogen.zip -d /usr/lib/autogen && \
  mv /usr/lib/autogen/autogen-*/* /usr/lib/autogen && rm -rf /usr/lib/autogen/autogen-* && \
  chmod a+rx /usr/lib/autogen/autogen.sh && \
  ln -s /usr/lib/autogen/autogen.sh /usr/bin/autogen

COPY requirements.txt requirements.txt
RUN cat requirements.txt
RUN pip install --require-hashes -r requirements.txt --break-system-packages

ENTRYPOINT ["/bin/bash"]