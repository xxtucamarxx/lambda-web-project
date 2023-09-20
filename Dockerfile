FROM ubuntu:22.04

ARG BASE_DIR=/var/www
ARG WEBSITE_NAME=lambda_site
ENV WEBSITE_NAME=${WEBSITE_NAME}

# Add apache2, mod_wsgi, python3.10 libraries
RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3.10 \
    python3.10-dev \
    python3.10-pip \
    vim \
    virtualenv \
    sudo \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /lambda_site/
WORKDIR /lambda_site/
COPY requirements.txt /lambda_site
RUN pip install -r requirements.txt
COPY . /lambda_site/

# Expose port 80 on the container
EXPOSE 80
# Make directory for lambda_project
RUN mkdir ${BASE_DIR}/${WEBSITE_NAME}
ENTRYPOINT ["/bin/bash", "/var/www/startup.sh"]
