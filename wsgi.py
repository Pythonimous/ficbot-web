"""
WSGI config for ficbotweb project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
from ficbotweb import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
