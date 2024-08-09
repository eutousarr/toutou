from flask_restx import fields

from .extensions import api

post_model = api.model("Post", {
    "id": fields.Integer(readonly=True, description="The task unique identifier"),
    "title": fields.String(required=True, description="The Post title"),
    "body": fields.String(required=False, description="The Post body"),
    "url": fields.String,
    "short_url": fields.String,
    "visits": fields.Integer,
    "user_id": fields.Integer,
    "created_at": fields.String,
    "updated_at": fields.String,
    # "user":
})

fournisseur_model = api.model("Fournisseur", {
    "id": fields.Integer,
    "name": fields.String,
    "contact": fields.String,
    "service": fields.String,
    # "bons":
})

bon_model = api.model("Bon", {
    "id": fields.Integer,
    "annee": fields.String,
    "mois": fields.String,
    "slug": fields.String,
    "quota_mois": fields.String,
    "engage": fields.Integer,
    "reste_quota": fields.Integer,
    "paid": fields.Boolean,
    "date_paiement": fields.DateTime,
    "fournisseur_id": fields.Integer,
    "created_at": fields.String,
    "updated_at": fields.String,
    
    # "articles":
})

article_model = api.model("Article", {
    "id": fields.Integer,
    "name": fields.String,
    "quantite": fields.String,
    "price": fields.Integer,    
    "bon_id": fields.Integer,
    "created_at": fields.String,
    "updated_at": fields.String,
    # "articles":
})

user_model = api.model("User", {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "created_at": fields.String,
    "updated_at": fields.String,
    # "posts": fields.List(fields.Nested(post_model))
})


fournisseur_input_model = api.model("FournisseurInput", {
    "name": fields.String,
    "contact": fields.String,
    "service": fields.String,
})

bon_input_model = api.model("BonInput", {
    "annee": fields.String,
    "mois": fields.String,
    "quota_mois": fields.Integer,
    "fournisseur_id": fields.Integer,
})

article_input_model = api.model("ArticleInput", {
    "name": fields.String,
    "quantite": fields.String,
    "price": fields.String,
    "bon_id": fields.Integer
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

