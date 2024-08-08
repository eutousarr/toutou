from flask_restx import fields

from .extensions import api

post_model = api.model("Post", {
    "id": fields.Integer,
    "title": fields.String,
    "body": fields.String,
    "url": fields.String,
    "short_url": fields.String,
    "visits": fields.Integer,
    "user_id": fields.Integer,
    "created_at": fields.String,
    "updated_at": fields.String,
    # "user":
})

user_model = api.model("User", {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "created_at": fields.String,
    "updated_at": fields.String,
    "posts": fields.List(fields.Nested(post_model))
})

post_input_model = api.model("PostInput", {
    "title": fields.String,
    "body": fields.String,
    "url": fields.String,
    "visits": fields.Integer,
    "user_id": fields.Integer
})

user_input_model = api.model("UserInput", {
    "username": fields.String,
    "email": fields.String,
    "password": fields.String,
    
})

