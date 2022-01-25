from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "AW1ZC2EV3"

from app import routes
