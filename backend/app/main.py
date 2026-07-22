from fastapi import FastAPI
from app.database.connection import engine
from app.models import user
from app.routes.users import router as users_router
from app.routes.auth import router as auth_router
from app.routes.projects import router as project_router

app = FastAPI(
    title="ALPA API",
    version="2.0.0"
)

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(project_router)

@app.get("/")
def root():
    return {"message": "ALPA API Running"}

@app.get("/database")
def database_test():

    try:
        connection = engine.connect()
        connection.close()

        return {
            "database": "connected"
        }

    except Exception as e:

        return {
            "error": str(e)
        }