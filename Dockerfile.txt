FROM python:3.8-slim

# Instalar dependencias necesarias para la instalación del controlador ODBC
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    g++ \
    unixodbc-dev \
    curl \
    apt-transport-https \
    ca-certificates \
    gnupg \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Instalar Microsoft ODBC Driver 17 para SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get update \
  && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Instalar ODBC Driver 17 para SQL Server y las dependencias adicionales
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    odbcinst \
    odbcinst1debian2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copiar archivo de requerimientos e instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el código fuente de la aplicación
COPY . /app/
WORKDIR /app/

# Ejecutar la aplicación
CMD export FLASK_APP=app.py && flask run -h 0.0.0.0 -p 10000
