from unittest.case import TestCase
from Model.GeodesicModel import Geodesic
from Queue import PriorityQueue


class TestNearestStationFetch(TestCase):
    def __init__(self):
        TestCase.__init__()
        print 'Hi'

    def test_PriorityQueue(self):
        q = PriorityQueue()
        q.put(Geodesic(2, 5, 17))
        q.put(Geodesic(1, 2, 14))
        q.put(Geodesic(3, 5, 12))
        q.put(Geodesic(2, 9, 19))
        print q
