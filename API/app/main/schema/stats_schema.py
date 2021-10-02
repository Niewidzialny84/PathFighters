from .. import ma

class StatsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'total', 'fails', 'wins')

stat_schema = StatsSchema() 
stats_schema = StatsSchema(many=True)