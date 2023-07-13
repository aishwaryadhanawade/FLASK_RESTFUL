from celery import Celery


def celery_conf(app):
    celery_app = Celery(app, broker="amqp://rabbitmq:5672//", backend="redis://redis:6379/0")
    return celery_app
