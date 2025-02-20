import os

ENVIRONMENT = os.getenv("DJANGO_ENV", "dev")  # По умолчанию dev

if ENVIRONMENT == "prod":
    from .prod import *
else:
    from .dev import *
