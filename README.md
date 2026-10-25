# API REST Serverless con AWS SAM - TODO App

Este repositorio contiene la implementación de una API RESTful para la gestión de tareas (TODOs), desarrollada como parte del taller práctico de **AWS SAM (Serverless Application Model)**.

## 🏗️ Arquitectura del Sistema

La solución utiliza una arquitectura 100% Serverless en AWS:

- **AWS API Gateway:** Punto de entrada HTTP para enrutar las peticiones CRUD.
- **AWS Lambda (Python 3.x):** Funciones sin servidor para procesar la lógica de negocio (Create, Read, Update, Delete).
- **Amazon DynamoDB:** Base de datos NoSQL para la persistencia de datos.
- **AWS CloudWatch:** Registro y monitoreo de eventos y logs.

## 📌 Endpoints de la API

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| **POST** | `/todos` | Crear una nueva tarea |
| **GET** | `/todos` | Listar todas las tareas |
| **GET** | `/todos/{id}` | Obtener una tarea por ID |
| **PUT** | `/todos/{id}` | Actualizar estado o título de una tarea |
| **DELETE** | `/todos/{id}` | Eliminar una tarea por ID |

## 🛠️ Comandos Principales de SAM

```bash
# Compilar el proyecto
sam build

# Desplegar en AWS
sam deploy --guided

# Ver logs de las funciones Lambda
sam logs -n GetTodoFunction --stack-name todo-sam-stack

# Limpieza de infraestructura
sam delete


Santiago Mendoza
