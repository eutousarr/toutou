from flask_restx import Resource, Namespace, fields

from .api_models import post_model, post_input_model, user_model, user_input_model, fournisseur_model, fournisseur_input_model, bon_model, bon_input_model, article_model, article_input_model
from .models import Post, User, Fournisseur, Bon, Article

ns = Namespace("api", __name__)

@ns.route("/toutou")
class toutou(Resource):
    def get(self):
        return {"prenoms": "Fatou Diop Fall", "surnom": "Toutou", "nom": "SARR", "dateNaissance": "28 décembre 2023", "lieuNaissance": "Ziguinchor", "pere": "Ismaïla", "mere": "Adja Aïssatou AIDARA", "adresse": "Goumel, Ziguinchor"}
    
# @ns.route("/posts")
# class PostListApi(Resource):
#     @ns.marshal_list_with(post_model)
#     def get(self):        
#         return Post.query.all()
    
@ns.route("/users")
class UserListApi(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):        
        return User.query.all()


post_api = Namespace("posts", description="POST operations")

@post_api.route("/")
class PostList(Resource):
    """Shows a list of all posts, and lets you POST to add new tasks"""

    @post_api.doc("list_posts")
    @post_api.marshal_list_with(post_model)
    def get(self):
        """List all Posts"""
        return Post.query.all()

    @post_api.doc("create_post")
    # @post_api.expect(post)
    @post_api.marshal_with(post_input_model, code=201)
    def post(self, payload):
        """Create a new task"""
        
       


# @ns.route("/<int:id>")
# @ns.response(404, "Post not found")
# @ns.param("id", "The task identifier")
# class Post(Resource):
#     """Show a single post item and lets you delete them"""

#     @ns.doc("get_post")
#     @ns.marshal_with(post)
#     def get(self, id):
#         """Fetch a given resource"""
#         return post_dao.get(id)

#     @ns.doc("delete_post")
#     @ns.response(204, "Post deleted")
#     def delete(self, id):
#         """Delete a task given its identifier"""
#         post_dao.delete(id)
#         return "", 204

#     @ns.expect(post)
#     @ns.marshal_with(post)
#     def put(self, id):
#         """Update a task given its identifier"""
#         return post_dao.update(id, api.payload)



bons = Namespace("bons", __name__)

@bons.route("/fournisseurs")
class FournisseurListApi(Resource):
    @bons.marshal_list_with(fournisseur_model)
    def get(self):        
        return Fournisseur.query.all()

@bons.route("/fournisseurs/<int:id>")
class FournisseurListApi(Resource):
    @bons.marshal_list_with(fournisseur_model)
    def get(self, id):        
        return Fournisseur.query.get(id)
    
@bons.route("/")
class BonListApi(Resource):
    @bons.marshal_list_with(bon_model)
    def get(self):        
        return Bon.query.all()
    
@bons.route("/articles")
class ArticleListApi(Resource):
    @bons.marshal_list_with(article_model)
    def get(self):        
        return Article.query.all()