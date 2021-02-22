from marshmallow import Schema, fields


class UserSchema(Schema):
    nome = fields.String()
    data_nascimento = fields.Date()
    email = fields.Email()
    idade = fields.Int()
    peso = fields.Float()
    altura = fields.Int()
