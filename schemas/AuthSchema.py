from marshmallow import Schema, fields

class AuthSchema(Schema):
  id = fields.Int(dump_only=True)
  email = fields.String(required=True)
  password = fields.String(required=True)
