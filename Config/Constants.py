from math import ceil

EARTH_RADIUS = 6371  # Radius of earth in kilometers. Use 3956 for miles
CORRELATION_COEFFICIENT_BENCHMARK = 0.88
TIME_SERIES_POINTS = 3
MAXIMUM_SURROUNDING_STATIONS = 5
MINIMUM_STATION_RADIUS = 0.15
MAXIMUM_THRESHOLD_DISTANCE = 3


def determine_next_hop(smallest_dist):
    result_dict = {}
    if smallest_dist <= MINIMUM_STATION_RADIUS:
        result_dict['OnStation'] = True
        result_dict['NextHop'] = 5
    else:
        result_dict['OnStation'] = False
        result_dict['NextHop'] = int(min(ceil(smallest_dist * 5), 60))
    return result_dict
