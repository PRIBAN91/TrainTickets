from cassandra.cluster import Cluster
import Calculations.CalculateGeohash as Geocode

cluster = Cluster()
session = cluster.connect()
session.set_keyspace('demo')


# session.execute(
#     "CREATE KEYSPACE IF NOT EXISTS Demo WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1};")
# print 'Successfully created Key space'


# session.execute("""
#
# insert into users (lastname, age, city, email, firstname) values ('Jones', 35, 'Austin', 'bob@example.com', 'Bob')
#
# """)
#
# result = session.execute("select * from users where lastname='Jones' ")[0]
# print result.firstname, result.age

# create a class to map to the "address" UDT
# class Address:
#     def __init__(self, lat, lon):
#         self.lon = lon
#         self.lat = lat

class Address(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


cluster.register_user_type('demo', 'lat_lon', Address)
geohash = Geocode.encode(19.128634, 72.928142)

# print Geocode.encode(19.112407, 72.928255)
#
# print Geocode.encode(19.142371, 72.937739)

# insert a row using an instance of Address
# cql = "INSERT INTO station_details (station_code, lat, lon, station_name, connecting_stations, number_of_tracks," \
#       " station_radius, track1, track2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#
# session.execute(cql, (
#     geohash, 19.128634, 72.928142, 'Kanjurmarg', {'te7uex29zdbk9knh': 1, 'te7ugsz8ks84f7pz': 2}, 2, 0.2,
#     [Address(19.126593, 72.927815), Address(19.126249, 72.927836), Address(19.125924, 72.927836)],
#     [Address(19.131175, 72.929360), Address(19.132006, 72.929832), Address(19.132959, 72.930368)]))
# cql = "insert into fare_charts (station_from_name, station_from_code, station_from_lat_lon, station_to_name," \
#       " station_to_code, station_to_lat_lon, fare) values (%s, %s, %s, %s, %s, %s, %s)"
# session.execute(cql, (
#     'Kanjurmarg', geohash, Address(19.128634, 72.928142), 'Bhandup', 'te7ugsz8ks84f7pz', Address(19.142371, 72.937739),
#     [10]))

# print 'Successfully inserted data!'
# # results will include Address instances
# results = session.execute("SELECT * FROM station_details")
# row = results[0]
# print row.stationhash, row.track1[0].lat, row.track1[0].lon


# create a class to map to the "address" UDT
# class Address(object):
#     def __init__(self, lat, lon):
#         self.lon = lon
#         self.lat = lat
#
#
# cluster.register_user_type('demo', 'lon_lat', Address)
# geohash = Geocode.encode(19.128634, 72.928142)
#
# session.execute(
#     "INSERT INTO stationdetails (stationcode, lat, lon, numberoftracks, track1) VALUES (%s, %s, %s, %s, %s)",
#     (geohash, 19.128634, 72.928142, 4, [Address(19.125694, 72.927745)]))
# print 'Successfully inserted data!'
#
# results = session.execute("SELECT * FROM collect_things")[0]
# for res in results.k.keys():
#     print res, results.k[res][0]
# session.encoder.mapping[tuple] = session.encoder.cql_encode_tuple
#
# cql = "INSERT INTO station_details (station_code, lat, lon, station_name, connecting_stations," \
#       " station_radius, all_track_details) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#
# session.execute(cql, (
#     geohash, 19.128634, 72.928142, 'Kanjurmarg', {1: 'te7uex29zdbk9knh', 2: 'te7ugsz8ks84f7pz'}, 0.2,
#     {1: ([19.126593, 19.126249, 19.125924], [72.927815, 72.927836, 72.927836]),
#      2: ([19.131175, 19.132006, 19.132959], [72.929360, 72.929832, 72.930368])}))
# list_of_tracks = []
# prepared_stmt = session.prepare("select all_track_details from station_details where station_code = ?")
# bound_stmt = prepared_stmt.bind([geohash])
# row = session.execute(bound_stmt)[0]
# for track_number in row.all_track_details.keys():
#     list_of_tracks.append([row.all_track_details[track_number][0], row.all_track_details[track_number][1]])
# print list_of_tracks