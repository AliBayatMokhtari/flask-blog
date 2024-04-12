import os

SECRET_KEY = os.environ.get("SECRET_KEY") or "this is a secret"
URL_PREFIX = "/api"
AUTHORIZATION_HEADER_KEY = "Authorization"
AUTHORIZATION_JWT_ALGO = "HS256"