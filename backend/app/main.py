from fastapi import FastAPI

app = FastAPI(
    title="ALPA API",
    version="2.0.0"
)

@app.get("/")
def root():
    return {"message": "ALPA API Running"}