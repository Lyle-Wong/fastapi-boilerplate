# from fastapi.templating import Jinja2Templates
from src import config

# templates = Jinja2Templates(directory=config.TEMPLATE_DIR)


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance