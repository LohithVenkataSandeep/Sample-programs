from fastapi import FastAPI
app=FastAPI()
@app.get("/hello/{name}")
def hello(name):
      return f"welcome to aurum intel {name}"