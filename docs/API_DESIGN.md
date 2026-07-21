1.API OVERIVIEW

# ALPA 2.0 API Design

ALPA backend provides RESTful APIs
to manage authentication, users,
projects, tasks, activities and AI insights.


2.BASE URL
Untuk development:
http://localhost:8000/api/v1

Future production:
https://api.alpa.com/api/v1


3.AUTHENTICATION API

Register User
Endpoint:
POST /auth/register

Request:
{
    "name": "Ubaidillah",
    "email": "user@email.com",
    "password": "password123"
}

Response:
{
    "message": "User created successfully"
}

Login
Endpoint:
POST /auth/login

Request:
{
    "email": "user@email.com",
    "password": "password123"
}

Response:
{
    "access_token": "jwt_token_here",
    "token_type": "bearer"
}


4.USER API

Get Current User:
GET /users/me

Response:
{
"id":1,
"name":"Ubaidillah",
"role":"employee"
}

5.TASK API

Create Task:
POST /tasks

Request:
{
"title":"Build authentication API",
"description":"Create JWT login system",
"priority":"high",
"deadline":"2026-08-01"
}

Get Tasks:
GET /tasks

Response:
[
{
"title":"Build API",
"status":"in_progress"
}
]

Update Task:
PUT /tasks/{task_id}

Delete Task:
DELETE /tasks/{task_id}


6.ACTIVITY API

Create Activity:
POST /activities

Request:
{
"task_id":1,
"activity_type":"coding",
"duration":120,
"notes":"Completed JWT authentication"
}

Get Activity History:
GET /activities


7.AI ANALYSIS API

Generate Personal Insight:
POST /ai/analyze

Input:
{
"user_id":1,
"period":"weekly"
}

AI Process:
User Data

↓

FastAPI

↓

OpenAI API

↓

Generate Insight

Response:
{
"insight":
"You improved 20% this week.
Focus on testing next."
}


8.FUTURE TEAM API

Dokumen dulu:
POST /teams

GET /teams/{id}/members

GET /teams/{id}/analytics


9.ERROR HANDLING

400:
{
"error":"Invalid request"
}

401:
{
"error":"Unauthorized"
}

404:
{
"error":"Resource not found"
}


10.API DEVELOPMENT PRIORITY

Phase 1

Authentication
Users
Tasks
Activities


Phase 2

AI Analysis


Phase 3

Team Management
Analytics


