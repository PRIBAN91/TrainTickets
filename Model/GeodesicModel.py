class Geodesic:
    def __init__(self, lat, lon, dist):
        self.lat = lat
        self.lon = lon
        self.dist = dist

    def __cmp__(self, other):
        return cmp(self.dist, other.dist)

    def __hash__(self):
        return hash((self.lat, self.lon))

    def __eq__(self, other):
        return (self.lat, self.lon) == (other.lat, other.lon)

    def __ne__(self, other):
        # To avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)
