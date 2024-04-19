from flask import Blueprint, request
from middlewares.auth_middleware import token_required
from config import SECRET_KEY, AUTHORIZATION_JWT_ALGO
import jwt

auth_blueprint = Blueprint("auth_blueprint", __name__)

@auth_blueprint.route("/login", methods=["POST"])
def login():
  try:
    body = request.get_json()

    if "username" not in body or "password" not in body:
      return {
        "message": "username and password are required",
        "data": None,
        "error": True
      }, 400
    
    username = body['username']
    password = body['password']

    if not bool(username) or not bool(password):
      return {
        "message": "username or password can not be empty",
        "data": None,
        "error": True
      }, 400

    token = jwt.encode(
      payload={"username": username, "password": password},
      key=SECRET_KEY,
      algorithm=AUTHORIZATION_JWT_ALGO
    )

    return {
      "message": "Login Successful",
      "data": {
        "username": username,
        "token": token
      },
      "error": None,
    }, 200
  except Exception as e:
    return {
      "message": "Something went wrong",
      "data": None,
      "error": str(e)
    }, 500

@auth_blueprint.route("/logout", methods=["POST"])
@token_required
def logout(user):
  return user, 200
