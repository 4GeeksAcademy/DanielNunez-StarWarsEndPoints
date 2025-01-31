from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.db.Column(db.db.Integer, primary_key=True)
#     email = db.db.Column(db.db.String(120), unique=True, nullable=False)
#     password = db.db.Column(db.db.String(80), unique=False, nullable=False)
#     is_active = db.db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

    def __repr__(self):
        return f'<Favorite {self.id}>'  

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planet_id": self.planet_id,
            # do not serialize the password, its a security breach
        } 

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    favorite = db.relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'  
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            # do not serialize the password, its a security breach
        } 

class People(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    height = db.Column(db.String(100))
    mass = db.Column(db.String(100))
    hair_color = db.Column(db.String(100))
    skin_color = db.Column(db.String(100))
    eye_color = db.Column(db.String(100))
    birth_year = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    homeworld = db.Column(db.String(100))
    favorite = db.relationship('Favorite', backref='people', lazy=True)

    def __repr__(self):
        return f'<People {self.name}>'  
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            # do not serialize the password, its a security breach
        } 

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    rotation_period = db.Column(db.String(100))
    orbital_period = db.Column(db.String(100))
    diameter = db.Column(db.String(100))
    climate = db.Column(db.String(100))
    gravity = db.Column(db.String(100))
    favorite = db.relationship('Favorite', backref='planet', lazy=True)

    def __repr__(self):
        return f'<Planet {self.name}>'  
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            # do not serialize the password, its a security breach
        } 