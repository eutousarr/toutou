from flask import Flask
from flask_cors import CORS
from .extensions import api, db
from .resources import ns

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///toutou.sqlite3"
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # CORS(app,
    #      resources={r"/api/*": {"origins": ['http://192.168.50.16:5000', 'http://localhost:3000']}},
    #      supports_credentials=True
    #      )
    api.init_app(app)
    db.init_app(app)
    
    api.add_namespace(ns)
    
    return app