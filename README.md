# FastAPI Virus Scanner

Este proyecto es una aplicación basada en **FastAPI** que permite escanear archivos utilizando la API de VirusTotal. La aplicación incluye controladores para manejar las solicitudes y servicios para interactuar con la API de VirusTotal.

## Características

- Escaneo de archivos mediante la API de VirusTotal.
- Arquitectura modular con controladores y servicios.
- Configuración sencilla utilizando Docker y Docker Compose.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Instalación y configuración

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

``` bash
git clone https://github.com/jczamudio/prueba_tech.git
cd Prueba_tech
```

### 2. Configurar las dependencias
Si deseas ejecutar el proyecto localmente sin Docker, instala las dependencias con pip:

``` bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Configurar la clave de la API de VirusTotal
Crea un archivo .env en la raíz del proyecto y agrega tu clave de API de VirusTotal:

``` bash
VT_API_KEY=tu_clave_de_api
```
### 4. Ejecutar con Docker
Para ejecutar la aplicación utilizando Docker, asegúrate de tener Docker y Docker Compose instalados. Luego, ejecuta el siguiente comando en la raíz del proyecto:

``` bash
docker-compose up --build
```

### 5. Ejecutar localmente
Si no usas Docker, ejecuta la aplicación con:

``` bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

La aplicación estará disponible en http://localhost:8000.


### Uso
Endpoint principal

POST /scan: Permite subir un archivo para escanearlo con la API de VirusTotal.
Ejemplo de uso con curl:

```bash'
curl -X POST "http://localhost:8000/scan" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@ruta_del_archivo"
```


### Accede a la documentación de la API en:


Swagger UI: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc

### Pruebas
Para ejecutar las pruebas unitarias, utiliza pytest:
```bash
pytest
```