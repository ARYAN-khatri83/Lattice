from celery import Celery
from app.config import settings

celery_app = Celery(
    "openclaims_worker",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@celery_app.task(name="process_document")
def process_document(file_key: str, job_id: str):
    print(f"Processing document: {file_key}, Job ID: {job_id}")
    return {"status": "completed", "job_id": job_id, "file_key": file_key}
