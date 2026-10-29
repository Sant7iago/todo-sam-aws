# 🚀 API REST Serverless con AWS SAM - TODO App (Partes 1 y 2)

Este repositorio contiene la implementación de una **API RESTful orientada a eventos** para la gestión de tareas (TODOs), desarrollada como parte del taller práctico de **AWS SAM (Serverless Application Model)**.

En la Parte 1 se construyó la API síncrona CRUD básica, y en la Parte 2 la solución evolucionó hacia un sistema de microservicios desacoplados mediante mensajería asíncrona, filtrado de eventos y tolerancia a fallos.

---

## 🏗️ Arquitectura del Sistema

La solución utiliza una arquitectura **100% Serverless** basada en infraestructura como código (IaC) con AWS SAM:

### 🔹 Componentes Síncronos (Capa API)
- **Amazon API Gateway:** Punto de entrada HTTP para la API REST.
- **AWS Lambda (Python 3.13):** Funciones para la lógica CRUD (`Create`, `List`, `Get`, `Update`, `Delete`) y consulta de historial (`GetHistory`).
- **Amazon DynamoDB (`TodosTable`):** Base de datos NoSQL para la persistencia de las tareas.

### 🔹 Componentes Asíncronos (Patrón Fan-Out & Eventos)
- **Amazon SNS (`TodoEventsTopic`):** Tópico pub/sub para la emisión de eventos de dominio (`todo.created`, `todo.updated`, `todo.completed`, `todo.deleted`).
- **Amazon SQS (`AuditQueue` & `NotificationsQueue`):** Colas de mensajes para desacoplar a los consumidores y procesar eventos de forma asíncrona.
- **Dead-Letter Queues (`AuditDLQ` & `NotificationsDLQ`):** Colas de mensajes muertos para capturar e aislar procesamientos fallidos o mensajes venenosos (`#fail`).
- **Amazon DynamoDB (`AuditTable`):** Almacén NoSQL para registrar el historial de auditoría de cada tarea.
- **Suscripciones con Filter Policies:** Reglas de filtrado en SNS para garantizar que `NotificationsQueue` procese únicamente el evento `todo.completed`.

---

## 📌 Endpoints de la API

| Método | Ruta | Descripción | Tipo |
| :--- | :--- | :--- | :--- |
| **POST** | `/todos` | Crear una nueva tarea | Síncrono |
| **GET** | `/todos` | Listar todas las tareas | Síncrono |
| **GET** | `/todos/{id}` | Obtener una tarea por ID | Síncrono |
| **PUT** | `/todos/{id}` | Actualizar estado o título de una tarea | Síncrono |
| **DELETE** | `/todos/{id}` | Eliminar una tarea por ID | Síncrono |
| **GET** | `/todos/{id}/history` | **(Nuevo)** Consultar el historial de auditoría | Síncrono |

---

## 🛠️ Comandos Principales de AWS SAM

```bash
# Validar el template y verificar sintaxis YAML
sam validate --lint

# Compilar las funciones y dependencias
sam build

# Desplegar la infraestructura en AWS
sam deploy

# Consultar logs en tiempo real de los consumidores o funciones
sam logs -n AuditFunction --stack-name todo-sam-stack --tail
sam logs -n NotifyFunction --stack-name todo-sam-stack --tail

# Eliminar todos los recursos del stack
sam delete --stack-name todo-sam-stack





#🧪 Pruebas y Tolerancia a Fallos (DLQ)
Para verificar el procesamiento asíncrono y la resiliencia ante fallos:

Monitoreo de Logs: Consultar los logs con sam logs -n AuditFunction para verificar el registro de auditoría.

Filtrado por Eventos: Verificar que NotifyFunction solo responda cuando una tarea cambie a completed: true.

Mensajes Venenosos: Crear un TODO con #fail en el título para forzar el fallo controlado en la notificación.

Verificación en la DLQ:
aws sqs get-queue-attributes --queue-url "$NOTIF_DLQ" --attribute-names ApproximateNumberOfMessages



Autor: Santiago Mendoza

Tecnologías: AWS SAM | Python 3.13 | Amazon SNS | Amazon SQS | DynamoDB | API Gateway
