import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAcgos8Uy9iVDLSKrnibfEpN249yVKtCJA')


def near_by_places(location):
    resp = gmaps.places_nearby(location, rank_by='distance', keyword='public toilets')
    return resp


def find_route(source, destination):
    resp = gmaps.distance_matrix(
            source,
            destination,
            mode="WALKING",
            language="en-IN",
            units="imperial"
    )
    return resp
