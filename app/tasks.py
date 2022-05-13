from typing import List
from celery import Celery
from models.parser import Parser
from utils import send_email
from datetime import datetime
import os

celery = Celery(__name__)

celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379"
)


@celery.task
def send_json(data: List, max: int):
    start = Parser()
    results = start.parse(max=max)

    json_data = []

    for pi in results:
        if pi["available"] == "Yes":
            for user in data:
                # if pi["model"] in user["model"] and pi["region"] in user["region"]:
                dt = datetime.now()
                body = {
                    "address": user["mail"],
                    "model": pi["model"],
                    "shop": pi["shop"],
                    "price": pi["price"],
                    "email_sent": dt.strftime("%Y-%d-%m, %H:%M:%S"),
                }
                json_data.append(body)
    return json_data
