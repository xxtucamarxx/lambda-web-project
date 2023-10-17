FROM python:3.11

ARG BASE_DIR=/var/www
ARG WEBSITE_NAME=lambda_project
ENV WEBSITE_NAME=${WEBSITE_NAME}

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    apache2 \
    gdal-bin\
    libapache2-mod-wsgi-py3 \
    build-essential \
    libssl-dev \
    libffi-dev \
    vim \
    virtualenv \
    sudo \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório para o projeto

# Copiar arquivos do projeto
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expor a porta 80 no container
EXPOSE 80
