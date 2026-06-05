# Tarea 3.0 - Automatización de CI/CD con GitHub Actions y Docker

## Información del Proyecto

**Repositorio:** Tarea3.0

**Aplicación:** ejercicio:3.0.0

**Descripción:**

Aplicación básica de Lista de Tareas desarrollada en Python. Permite agregar tareas a una lista y verificar su funcionamiento mediante pruebas automatizadas utilizando Pytest.

## Tecnologías Utilizadas

* Python 3
* Pytest
* Docker
* GitHub Actions
* GitHub Container Registry (GHCR)

## Estructura del Proyecto

```text
Tarea3.0/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
└── test/
    └── test_app.py
```

## Instalación

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la Aplicación

```bash
python app.py
```

## Ejecutar las Pruebas

```bash
pytest
```

## Construcción de Docker

Construir la imagen:

```bash
docker build -t ejercicio:3.0.0 .
```

Ejecutar el contenedor:

```bash
docker run ejercicio:3.0.0
```

## Automatización CI/CD

El proyecto utiliza GitHub Actions para:

* Descargar el código fuente.
* Instalar dependencias.
* Ejecutar pruebas automatizadas.
* Ejecutar la aplicación.
* Simular una fase de despliegue.
* Construir una imagen Docker.
* Publicar la imagen en GitHub Container Registry (GHCR).

## Autor

Geremy Mateo Galvez Avila
