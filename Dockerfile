# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /home/daniwar/deliverables_OpenScienceAI

# Copia los archivos del proyecto al contenedor
COPY . /home/daniwar/deliverables_OpenScienceAI

# Asegúrate de que el script de inicio es ejecutable
RUN chmod +x /home/daniwar/deliverables_OpenScienceAI/start.sh

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Configura el script de inicio como ENTRYPOINT
ENTRYPOINT ["/home/daniwar/deliverables_OpenScienceAI/start.sh"]
