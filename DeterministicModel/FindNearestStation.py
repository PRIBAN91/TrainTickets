from Calculations.CalculateDistance import haversine
from Model.GeodesicModel import Geodesic
from Queue import PriorityQueue
from Config.Constants import *


class GetNearestStations:
    def __init__(self, curr_lat, curr_long, list_of_nearest):
        self.curr_lat = curr_lat
        self.curr_long = curr_long
        self.list_of_nearest = list_of_nearest

    def sort_by_distance(self):
        result_dict = {}
        stations = []
        pq = PriorityQueue()
        for geo_pos in self.list_of_nearest:
            pq.put(Geodesic(geo_pos['Latitude'], geo_pos['Longitude'],
                            haversine(self.curr_lat, self.curr_long, geo_pos['Latitude'], geo_pos['Longitude'])))
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
                break
        result_dict['StationsLatLon'] = stations
        result_dict['NextState'] = next_state_to_call
        return result_dict
