1.BACKEND FOUNDATION:
User Register
User Login
JWT Authentication
PostgreSQL Connection


2.FOLDER BACKEND STRUCTURE:

backend/

├── app/
│
├── app/models/
│
├── app/schemas/
│
├── app/routers/
│
├── app/services/
│
├── app/core/
│
├── app/database/
│
├── app/main.py
│
└── requirements.txt


3.WHY?

models
    ↓
database tables

schemas
    ↓
request/response validation

routers
    ↓
API endpoints

services
    ↓
business logic

core
    ↓
security
    JWT
    config

database
    ↓
connection



