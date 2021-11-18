from .. import ma

class TokenBlacklistSchema(ma.Schema):
    class Meta:
        fields = ('id', 'jti', 'expiration_time')

token_blacklist_schema = TokenBlacklistSchema() 
tokens_blacklist_schema =  TokenBlacklistSchema(many=True)