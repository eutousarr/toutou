from flask_restx import Resource, Namespace

from .api_models import post_model, user_model
from .models import Post, User

ns = Namespace("api")

@ns.route("/toutou")
class toutou(Resource):
    def get(self):
        return {"prenoms": "Fatou Diop Fall", "surnom": "Toutou", "nom": "SARR", "dateNaissance": "28 décembre 2023", "lieuNaissance": "Ziguinchor", "pere": "Ismaïla", "mere": "Adja Aïssatou AIDARA", "adresse": "Goumel, Ziguinchor"}
    
@ns.route("/posts")
class PostListApi(Resource):
    @ns.marshal_list_with(post_model)
    def get(self):        
        return Post.query.all()
    
@ns.route("/users")
class UserListApi(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):        
        return User.query.all()