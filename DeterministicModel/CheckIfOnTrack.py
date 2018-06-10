import Calculations.CalculateCorrelation as Coefficient
from DataAcess.CassandraConn import session
from Config.Constants import *


class OnTrack:
    def __init__(self, station_code, time_series_lat, time_series_lon):
        self.station_code = station_code
        self.time_series_lat = time_series_lat
        self.time_series_lon = time_series_lon

    def get_course_path(self):
        is_on_correct_track = False
        list_of_tracks = self.fetch_track_details()
        for count, tracks in enumerate(list_of_tracks):
            # print count, tracks
            for index in xrange(len(tracks[0])):
                if index + TIME_SERIES_POINTS > len(tracks[0]) or index > TIME_SERIES_POINTS or is_on_correct_track:
                    break
                is_on_correct_track = Coefficient.is_correlation_strong(self.time_series_lat, self.time_series_lon,
                                                                        tracks[0][index:index + TIME_SERIES_POINTS],
                                                                        tracks[1][index:index + TIME_SERIES_POINTS])

        print is_on_correct_track
        return is_on_correct_track

    def fetch_track_details(self):
        list_of_tracks = []
        prepared_stmt = session.prepare("select all_track_details from station_details where station_code = ?")
        bound_stmt = prepared_stmt.bind([self.station_code])
        row = session.execute(bound_stmt)[0]
        for track_number in row.all_track_details.keys():
            list_of_tracks.append([row.all_track_details[track_number][0], row.all_track_details[track_number][1]])
        return list_of_tracks
