import Calculations.CalculateNearestPoints as Nearest
from Config.Constants import *


class FetchNearbyStations:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def fetch_nearest_stations(self):
        stations = []
        result_dict = {}
        pq = Nearest.fetch_nearest_point(self.lat, self.lon)
        calculated_hop, next_state_to_call = False, 'NearestStation'
        while not pq.empty():
            geo_data = pq.get()
            stations.append({'Latitude': geo_data.lat, 'Longitude': geo_data.lon})
            if not calculated_hop:
                calculated_hop = True
                result_dict.update(determine_next_hop(geo_data.dist))
                if result_dict['OnStation']:
                    break
            if geo_data.dist > MAXIMUM_THRESHOLD_DISTANCE:
                next_state_to_call = 'NearbyStations'
        result_dict['StationsLatLon'] = stations
        result_dict['NextState'] = next_state_to_call
        return result_dict
