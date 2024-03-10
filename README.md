
# Django Based Discord Bot Example

Easily connect your discord app to django to create a web app for your discord bot using django models and REST API's.


## Installation
- Ceate your .env file in the root of the directory then create a variable and put your token there
 ```bash
  DISCORD_API_TOKEN=<your token here>
```
- Ceate your virtual environment
```bash
  python -m venv venv
```
- Install Proeject requirements
```bash
  pip install -r requirements.txt
```
windows:
```bash
  .\venv\Scripts\activate
```
Linux/Mac:
```bash
  source venv/bin/activate
```

- Create migrations and migrate 
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
- Create a superuser for django's admin panel (optional)
```bash
  python manage.py createsuperuser
```
- Run the server
```bash
  python manage.py runserver
```
- Locate to ./discord_bot and run main.py
```bash
  cd ./discord_bot
  python main.py
```

 
