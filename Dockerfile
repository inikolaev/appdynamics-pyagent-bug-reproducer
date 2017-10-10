FROM registry.opensource.zalan.do/stups/python:3.6-cd35

RUN apt-get update && \
    apt-get -y install --no-install-recommends libffi-dev libpq-dev libpython3-dev libssl-dev wget curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/
WORKDIR /app/

# Dependencies
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY appdynamics.cfg /app/appdynamics.cfg

# Actual application
COPY main.py /app/
COPY run.sh /app/

CMD ./run.sh

