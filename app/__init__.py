from flask import Flask
from flask_cors import CORS
from .extensions import api, db
from .resources import ns, bons, post_api

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://eutousarr:GT1eUpdIcRwWAew3f5vbtWoApGeEUuat@dpg-cqr5lbbv2p9s73beo07g-a.oregon-postgres.render.com/toutou"
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # CORS(app,
    #      resources={r"/api/*": {"origins": ['http://192.168.50.16:5000', 'http://localhost:3000']}},
    #      supports_credentials=True
    #      )
    api.init_app(app,
    version="1.0",
    title="Toutou API",
    description="A simple Toutou API",)
    db.init_app(app)
    
    api.add_namespace(ns)
    api.add_namespace(bons)
    api.add_namespace(post_api)
    
    return app