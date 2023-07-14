from celery import Celery


def celery_conf(app):
    celery_app = Celery(app, broker="amqp://rabbitmq:5672//",include=['register_restful_api.celery_file.celery_task'])
    return celery_app
