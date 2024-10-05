from fastapi import FastAPI

app = FastAPI()

@app.get("/getEmplList")
def read_root():
    return {"name":"test"}


@app.get("/getdeplList")
def read_root():
    return {"name":"test"}