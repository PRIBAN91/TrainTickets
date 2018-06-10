from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
session.set_keyspace('demo')


class Address(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


cluster.register_user_type('demo', 'lat_lon', Address)
