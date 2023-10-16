FROM python:3.11


ARG WEBSITE_NAME=lambda_project
ENV WEBSITE_NAME=${WEBSITE_NAME}

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    build-essential \
    libssl-dev \
    libffi-dev \
    gdal-bin \
    vim \
    virtualenv \
    sudo \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório para o projeto
RUN mkdir /var/www/lambda_project/
WORKDIR /var/www/lambda_project/



# Copiar arquivos do projeto
COPY requirements.txt .

# Instalar dependências
RUN pip install -r requirements.txt

COPY ./lambda_project .

# Expor a porta 80 no container
EXPOSE 80
