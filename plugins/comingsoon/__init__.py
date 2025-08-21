from .core import register_comingsoon
from .scheduler import start_scheduler

def register_plugin(app):
    register_comingsoon(app)
    start_scheduler(app)
