import jwt
from functools import wraps
from flask import request
from flask import current_app
from config import AUTHORIZATION_HEADER_KEY, AUTHORIZATION_JWT_ALGO

def token_required(f):
  @wraps(f)

  def decorated(*args, **kwargs):
    token = None

    if AUTHORIZATION_HEADER_KEY in request.headers:
      token = request.headers[AUTHORIZATION_HEADER_KEY].split(" ")[1]

    if not token:
      return {
        "message": "Authentication token is missing!",
        "data": None,
        "error": "Unauthorized"
      }, 401
    
    try:
      data = jwt.decode(
        token,
        current_app.config["SECRET_KEY"],
        algorithms=[AUTHORIZATION_JWT_ALGO]
      )

      return f(data, *args, **kwargs)
    except Exception as e:
      return {
          "message": "Something went wrong",
          "data": None,
          "error": str(e)
      }, 500
    
  return decorated
