# Fashion Project

## Install

Create the virtual environment, activate and install the required packages.

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
spacy download en_core_web_sm
```

Copy the .env and edit the necessary variables.

```bash
cp .env.example .env
```

Use the flask shell to create the database

```bash
flask --app api shell
```

Inside the shell execute:

```python
from api.models import *
db.create_all()
```

Back to the terminal, seed the database.

```bash
python seed.py
```


## Execution

Use the flask program to start the development server

```bash
flask --app api run
```
