from .UserSchema import UserSchema
from .AuthSchema import AuthSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)
auth_schema = AuthSchema()
