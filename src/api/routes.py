"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User,Favorite, People, Planet
from api.utils import generate_sitemap, APIException
import json

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/people', methods=['GET'])
def get_People():

    personajes = People.query.all()
    resultado = list(map(lambda personaje: personaje.serialize(), personajes))
    return jsonify(resultado) , 200

@api.route('/people/<int:people_id>', methods=['GET'])
def get_PeopleId(people_id):

    persona = People.query.filter_by(id = people_id).first()
    if persona is None:
        return ({'msg': "No existe el personaje"}) , 400
    
    resultado = persona.serialize()
    return jsonify(resultado) , 200

@api.route('/planets', methods=['GET'])
def get_Planets():

    planetas = Planet.query.all()
    resultado = list(map(lambda planeta: planeta.serialize(), planetas))
    return jsonify(resultado) , 200


@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_PlanetaId(planet_id):

    planetas = Planet.query.filter_by(id = planet_id).first()

    if planetas is None:
        return ({'msg': "No existe el planeta"}) , 400
    
    resultado = planetas.serialize()
    return jsonify(resultado) , 200

@api.route('/user', methods=['GET'])
def get_User():

    usuario = User.query.all()
    resultado = list(map(lambda usu: usu.serialize(), usuario))
    return jsonify(resultado) , 200

@api.route('/favorite', methods=['GET'])
def get_Favorite():

    favorito = Favorite.query.all()
    resultado = list(map(lambda fav: fav.serialize(), favorito))
    return jsonify(resultado) , 200

@api.route('/favorite/planets/<int:planet_id>', methods=['POST'])
def post_FavoritePlanet(planet_id):
    body = json.loads(request.data)
    new_Favorite = Favorite(
        user_id = body['user_id'],
        planet_id = planet_id
    )
    db.session.add(new_Favorite)
    db.session.commit()
    return ({'msg': "Favorito agregado"}) , 200 

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def post_FavoritePeople(people_id):
    body = json.loads(request.data)
    new_Favorite = Favorite(
        user_id = body['user_id'],
        people_id = people_id
    )
    db.session.add(new_Favorite)
    db.session.commit()
    return ({'msg': "Favorito agregado"}) , 200 

@api.route('/favorite/planet/<int:planet_id>/<int:user_id>', methods=['DELETE'])
def delete_FavoritePlanet(planet_id, user_id):
    fav_user = Favorite.query.filter_by(user_id = user_id).first()
    if fav_user is None: 
        return ({'msg': "Usuario no encontrado"}) , 400 
    fav_planet = Favorite.query.filter_by(planet_id = planet_id).first()
    if fav_planet is None: 
        return ({'msg': "Planeta no encontrado"}) , 400 
    
    favorito = Favorite.query.filter_by(user_id = user_id).filter_by(planet_id = planet_id).first()
    db.session.delete(favorito)
    db.session.commit()
    return ({'msg': "Favorito eliminado"})

@api.route('/favorite/people/<int:people_id>/<int:user_id>', methods=['DELETE'])
def delete_FavoritePeopleUser(people_id, user_id):
    fav_user = Favorite.query.filter_by(user_id = user_id).first()
    if fav_user is None: 
        return ({'msg': "Usuario no encontrado"}) , 400 
    fav_people = Favorite.query.filter_by(people_id = people_id).first()
    if fav_people is None: 
        return ({'msg': "Planeta no encontrado"}) , 400 
    
    favorito = Favorite.query.filter_by(user_id = user_id).filter_by(people_id = people_id).first()
    db.session.delete(favorito)
    db.session.commit()
    return ({'msg': "Favorito eliminado"})


    # favorito = Favorite.query.all()
    # resultado = list(map(lambda fav: fav.serialize(), favorito))
    # return jsonify(resultado) , 200

