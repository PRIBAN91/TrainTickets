# !/usr/bin/env python
import web
import json
from DeterministicModel.FetchNearbyStations import FetchNearbyStations
from DeterministicModel.FindNearestStation import GetNearestStations
from DeterministicModel.FetchFareChart import FetchFareDetails
from DeterministicModel.CheckIfOnTrack import OnTrack

urls = (
    '/NearbyStations', 'get_nearby_stations',
    '/NearestStation', 'get_nearest_stations',
    '/GetStationDetails', 'get_station_details',
    '/GetFareCharts', 'get_fare_details',
    '/CheckTrack', 'check_if_on_correct_track',
    '/favicon.ico', 'icon'
)

app = web.application(urls, globals())


class get_nearby_stations:
    def POST(self):
        data = json.loads(web.data())
        f = FetchNearbyStations(data['Latitude'], data['Longitude'])
        result = f.fetch_nearest_stations()
        return json.dumps(result)


class get_nearest_stations:
    def POST(self):
        data = json.loads(web.data())
        g = GetNearestStations(data['Latitude'], data['Longitude'], data['NearestList'])
        result = g.sort_by_distance()
        return json.dumps(result)


class get_station_details:
    def POST(self):
        print 'Hi'


class get_fare_details:
    def POST(self):
        data = json.loads(web.data())
        f = FetchFareDetails(data['StationCode'])
        result = f.fetch_fare_details()
        return json.dumps(result)


class check_if_left_station:
    def POST(self):
        data = json.loads(web.data())


class check_if_on_correct_track:
    def POST(self):
        data = json.loads(web.data())
        f = OnTrack(data['StationCode'], data['TimeSeriesLat'], data['TimeSeriesLon'])
        result = f.get_course_path()
        return 'Hi'


class icon:
    def GET(self):
        raise web.seeother("../Resources/favicon.ico")


if __name__ == "__main__":
    app.run()
