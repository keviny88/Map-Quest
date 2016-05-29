#This module contains all of the functions necessary for interacting with
#the MapQuest Open Data APIs

import json
import urllib.parse
import urllib.request


def build_url_directions(local_list: 'list of locations') -> str:
    '''Takes in a list of destinations and transfers it into a
    MapQuest compatible URL'''
    API_KEY= 'Fmjtd%7Cluu821u2nq%2Cr5%3Do5-94a590'
    BASE_MAP_URL = 'http://open.mapquestapi.com/'
    query_parameters= [ ('from', local_list[0])]
    for x in local_list[1:]:
        query_parameters.append( ('to', x) )
    return BASE_MAP_URL + 'directions/v2/route?key=' + API_KEY + '&' + urllib.parse.urlencode(query_parameters)

def build_url_elevations(LatLong: 'LATLONG')-> str:
    '''
    Takes in a LATLONG class object and returns a URL that can be used to retrieve the appropriate
    JSON object containing the elevation profile
    '''
    API_KEY= 'Fmjtd%7Cluu821u2nq%2Cr5%3Do5-94a590'
    BASE_MAP_URL = 'http://open.mapquestapi.com/'
    query= ''

    for coord in LatLong.coord_list:
        query += str(coord[0]) + ',' + str(coord[1])
        if LatLong.coord_list[-1] != coord:
            query += ','

    query_parameters= [ ('latLngCollection', query) , ('unit', 'f') ]

    return BASE_MAP_URL + 'elevation/v1/profile?key=' + API_KEY+ '&' + urllib.parse.urlencode(query_parameters)


def get_result(url: str) -> 'JSON':
    '''
    Takes in a URL that will be sent to the mapquest server, requesting a
    JSON object and converting it into a python dictionary
    '''
    response= None
    response= urllib.request.urlopen(url)
    json_text= response.read().decode(encoding = 'utf-8')
    return json.loads(json_text)
