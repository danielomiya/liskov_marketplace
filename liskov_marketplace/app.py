from flask import Flask

from liskov_marketplace.routes.users import bp as users

app = Flask(__name__)
app.register_blueprint(users)
