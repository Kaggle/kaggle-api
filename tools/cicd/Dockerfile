# This Docker image is a modified version of the python image that
# includes [hatch](https://hatch.pypa.io/latest/)

ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

# Pick up the emSign/eMudhra CA removal (GHSA-6q48-6c7w-9gw2) in the OS trust store and Python tooling.
RUN apt-get update && apt-get install -y --only-upgrade ca-certificates && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade "pip>=26.2.2" "certifi>=2026.10.19" hatch==1.16.5

ENTRYPOINT ["hatch"]