from celery_app.celery_settings import app

@app.task
def loadVideo():
    (lambda: print(111111111))()