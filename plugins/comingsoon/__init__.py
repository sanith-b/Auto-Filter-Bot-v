from plugins.comingsoon.core import register_comingsoon
from plugins.comingsoon.scheduler import start_scheduler

def register_plugin(app):
    register_comingsoon(app)
    start_scheduler(app)
