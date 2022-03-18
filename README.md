# ficbot-web

An AI-powered Fan Fiction Writing Assistant.

Ficbot is a machine learning-based system that provides various tools to make a good starting point for an aspiring writer when they need a character, but don't know where to start.

Here you will find a ***simple Flask-based web client*** for the main application. You can find out more about the main project in **this [repository](https://github.com/Pythonimous/ficbot)**.
## Features
- Image -> Name generator

### Planned features
- Name generators (from Bio, Image + Bio)
- Bio generators (from Name, Image)
- Image generators (from nothing, Name, Bio)
- Anime filter (to turn yourself into OC!)
- Complete OC generator (Nothing -> Name, Bio, Image) :)

## Installation
I. Create and activate a virtual environment.

1. [Windows (w/o WSL)](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)
2. [Linux (from "Step 1. Install Python") / Windows (w/WSL)](https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/)


II. Install project requirements from [requirements.txt](https://github.com/Pythonimous/ficbot/blob/main/requirements.txt)
```bash
pip3 install -r requirements.txt
```

## Launching the server
### Linux
In a virtual environment and in a project folder:
```bash
export FLASK_ENV=development
export FLASK_APP=ficbotweb
flask run
```
Go to the address in the terminal (i.e. http://127.0.0.1:5000/) and have fun!