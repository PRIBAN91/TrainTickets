from DataAcess.CassandraConn import session


class FetchFareDetails:
    def __init__(self, station_code):
        self.station_code = station_code

    def fetch_fare_details(self):
        results = []
        prepared_stmt = session.prepare("select * from fare_charts where station_from_code = ?")
        bound_stmt = prepared_stmt.bind([self.station_code])
        db_results = session.execute(bound_stmt)
        for row in db_results:
            results.append(
                {'StationToName': row.station_to_name, 'StationToCode': row.station_to_code, 'Fares': row.fare,
                 'StationViaNames': row.station_via_names, 'StationViaCodes': row.station_via_codes})
        return results
