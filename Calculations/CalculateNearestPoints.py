from Config.Constants import EARTH_RADIUS as R, MAXIMUM_SURROUNDING_STATIONS as N
from math import sin, cos, atan, asin, pi
from Model.GeodesicModel import Geodesic
from scipy.spatial import cKDTree
from Queue import PriorityQueue


def fetch_nearest_point(lat, lon):
    xyz_points = lat_lon_to_cartesian(lat, lon)
    dist, ind = tree.query([xyz_points], k=N, n_jobs=-1)
    q = PriorityQueue()
    # noinspection PyTypeChecker
    for (i, d) in zip(ind[0], dist[0]):
        q.put(Geodesic(stations_in_lat_lon[i][0], stations_in_lat_lon[i][1], d))
    return q


def lat_lon_to_cartesian(lat, lon):
    rad = pi / 180
    x = R * cos(lat * rad) * cos(lon * rad)
    y = R * cos(lat * rad) * sin(lon * rad)
    z = R * sin(lat * rad)
    return [x, y, z]


def cartesian_to_lat_lon(x, y, z):
    inv_rad = 180 / pi
    lat = atan(y / x) * inv_rad
    lon = (asin(z / R) * inv_rad)
    return [lat, lon]


stations_in_cartesian_coordinates = []
stations_in_lat_lon = [[19.118327, 72.911174], [19.116510, 72.910321], [19.115641, 72.908825], [19.120284, 72.909157],
                       [19.119878, 72.907172], [19.113401, 72.906142], [19.120071, 72.916346]]
for lat_lon in stations_in_lat_lon:
    stations_in_cartesian_coordinates.append(lat_lon_to_cartesian(lat_lon[0], lat_lon[1]))
tree = cKDTree(stations_in_cartesian_coordinates, leafsize=len(stations_in_lat_lon), copy_data=True)
