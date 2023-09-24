FROM alpine

ARG BASE_DIR=/var/www
ARG WEBSITE_NAME=lambda_project
ENV WEBSITE_NAME=${WEBSITE_NAME}

# Add apache2, mod_wsgi, python3.10 libraries
RUN apk add apache2 \
    libapache2-mod-wsgi-py3 \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3.10 \
    python3.10-dev \
    python3-pip \
    vim \
    sudo \
    && pip  install pipenv \

# Install dependencies:
RUN mkdir /lambda_project/
WORKDIR /lambda_project/
COPY . /lambda_project/

ENV PIPENV_VENV_IN_PROJECT=1
ENV VIRTUAL_ENV /lambda_project/.venv/lib/python3.10
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pipenv install Pipfile

# Expose port 80 on the container
EXPOSE 80
# Make directory for lambda_project
RUN mkdir ${BASE_DIR}/${WEBSITE_NAME}
CMD ["apache2ctl", "-D", "FOREGROUND"]
ENTRYPOINT ["/bin/bash"]
