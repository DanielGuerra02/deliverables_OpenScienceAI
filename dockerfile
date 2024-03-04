# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Asegúrate de que el script de inicio es ejecutable
RUN chmod +x /app/start.sh

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Configura el script de inicio como ENTRYPOINT
ENTRYPOINT ["/app/start.sh"]
