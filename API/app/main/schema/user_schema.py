from .. import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password')

user_schema = UserSchema() 
users_schema = UserSchema(many=True)