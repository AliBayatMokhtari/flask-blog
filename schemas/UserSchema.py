from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str()

user_schema = UserSchema()
users_schema = UserSchema(many=True)
