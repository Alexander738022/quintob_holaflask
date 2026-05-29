# 1; buscar imagen base 
FROM python:3.12-alpine

# 2; Crear el directorio de trabajo en el contenedor 
WORKDIR /app

# 3;Copiar el archivo de dependencias 
COPY requirements.txt  /app

# 4;Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5: Copiar el código de la aplicación al contenedor
COPY app.py /app

# 6: Exponer el puerto en el que la aplicación se ejecutará
EXPOSE 5000

# 7: Comando para ejecutar la aplicación
CMD ["python", "app.py"]
