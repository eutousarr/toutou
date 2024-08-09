from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random
from slugify import slugify  # among other things

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=30000)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    bookmarks = db.relationship('Bookmark', backref="user")
    bons = db.relationship('Bon', backref='owner', lazy=True)

    def __repr__(self) -> str:
        return 'User>>> {self.username}'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(5), nullable=True)
    visits = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def generate_short_characters(self):
        characters = string.digits+string.ascii_letters
        picked_chars = ''.join(random.choices(characters, k=5))

        link = self.query.filter_by(short_url=picked_chars).first()

        if link:
            self.generate_short_characters()
        else:
            return picked_chars

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.short_url = self.generate_short_characters()

    def __repr__(self) -> str:
        return 'Boomark>>> {self.url}'

      
class Bon(db.Model):
    
    __tablename__ = 'bon'
    
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    annee = db.Column(db.Integer, nullable=False)
    mois = db.Column(db.Integer, nullable=False)
    quota_mois = db.Column(db.Integer, nullable=False, default=45000)
    engage = db.Column(db.Integer, default=0)
    reste_quota = db.Column(db.Integer, default=0)
    paid = db.Column(db.Boolean, nullable=False, default=False)
    date_paiement = db.Column(db.DateTime, nullable=True)
    engage_par = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=True)

    articles = db.relationship('Article', backref='bon')
    
    def __repr__(self):
        return f'<Bon>>> {self.title}, {self.engage}>'
    
    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get(['annee', 'mois'], '-'))
        super().__init__(*args, **kwargs)
        
    def get_id(self):
        return self.id
    
    @property
    def get_montant(self):
        articles = self.articles 
        total = sum(article.get_total for article in articles)
        return total
    
    def commande_possible(self, article_obj):
        return self.quota_mois >= article_obj.get_total
    
    def regler_bon(self, bon):
        bon.reste_quota = self.quota_mois - self.get_montant
        db.session.commit()

        
class Article(db.Model):
    
    __tablename__ = 'article'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    quantite = db.Column(db.Integer, nullable=True, default=0)
    price = db.Column(db.Integer, nullable=True, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=True)
    
    bon_id = db.Column(db.Integer, db.ForeignKey('bon.id'))
    
    def __repr__(self):
        return f'<Article {self.name}, {self.quantite}:{self.price}>'
    
    def get_id(self):
        return self.id
    
    @property
    def get_total(self):
        total = self.quantite * self.price
        return total
    
    def commander(self, bon):
        self.bon_id = bon.id
        bon.quota_mois -= self.get_total
        bon.engage += self.get_total
        db.session.commit()


def get_montant_mois(mois=None, annee=None):
        
    if mois and annee:
        bon = Bon.query.filter(mois=mois, annee=annee).first()
        depense_general = bon.get_montant
    else:
        bon = Bon.query.all()
        depense_general = sum(bon.get_montant for b in bon)  
    
    return depense_general
