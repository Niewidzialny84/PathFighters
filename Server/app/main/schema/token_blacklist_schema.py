from .. import ma

class TokenBlacklistSchema(ma.Schema):
    """ Token Black LIst Schema. """
    class Meta:
        fields = ('id', 'jti', 'expiration_time')

token_blacklist_schema = TokenBlacklistSchema() 
tokens_blacklist_schema =  TokenBlacklistSchema(many=True)
