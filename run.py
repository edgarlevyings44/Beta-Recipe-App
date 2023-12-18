from flask import Flask
from flask_jwt_extended import JWTManager
from main import create_app
from config import DevConfig, ProdConfig
import os

app = create_app(ProdConfig)

# Set the JWT secret key
app.config['JWT_SECRET_KEY'] = '55bd39030792ae698beb143cef2a1fd489c8961e98a15f8436ca5d0de903ac92'

# Initialize the Flask-JWT-Extended extension
jwt = JWTManager(app)

# run with
if __name__ == "__main__":
    app.run()
