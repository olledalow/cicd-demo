from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/fail", status_code=404)
def fail_endpoint():
    return {"msg": "This should fail"}
