from fastapi import FastAPI
from tasks import send_json
from fastapi.responses import JSONResponse
import json

app = FastAPI()


@app.get("/")
async def get_all_pi():
    data = json.load(open("app/fixtures/sample_data.json", "r"))
    task = send_json.delay(data=data, max=3)
    return JSONResponse(content=task.id)


@app.get("/status/{task_id}")
async def read_pi(task_id):
    task = send_json.AsyncResult(task_id)
    return JSONResponse(content=task.get())
