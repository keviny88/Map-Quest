#This module contains all of the information for the outputs and their
#corresponding classes

import json
import urllib.parse
import urllib.request
from mapquest_interface import *
from mapquest_json import *

class STEPS:

    def __init__(self, json: 'JSON'):
        directions_list= []
        for leg_number in range(len(json['route']['legs'])):
            for maneuver in json['route']['legs'][leg_number]['maneuvers']:
                directions_list.append(maneuver['narrative'])
        self.steps= directions_list

    def print_data(self):
        print('DIRECTIONS')
        for step in self.steps:
            print(step)

class TOTALTIME:

    def __init__(self,json):
        time= json['route']['time']
        self.minutes= round(time / 60)

    def print_data(self):
        print('TOTAL TIME:', self.minutes, 'minutes')


class TOTALDISTANCE:

    def __init__(self,json):
        miles= round(json['route']['distance'])
        self.miles= miles

    def print_data(self):
        print('TOTAL DISTANCE:', str(self.miles),'miles')

class LATLONG:

    def __init__(self,json):
        coord_list= []
        for x in json['route']['locations']:
            lat= x['latLng']['lat']
            lng= x['latLng']['lng']
            coord_list.append( (lat,lng) )
        self.coord_list = coord_list

    def print_data(self):
        print('LATLONGS')
        for coord in self.coord_list:
            if coord[0] <= 0:
                lat_string = abs(coord[0])
                lat_end= 'S'
            else:
                lat_string = coord[0]
                lat_end= 'N'
            if coord[1] <= 0:
                lng_string = abs(coord[1])
                lng_end = 'E'
            else:
                lng_string= coord[1]
                lng_end = 'W'
            print('{:.2f}{} {:.2f}{}'.format(lat_string, lat_end, lng_string, lng_end) )

class ELEVATION():

    def __init__(self, LatLong):
        url= build_url_elevations(LatLong)
        json= get_result(url)
        elevation_list= []
        for coord in json['elevationProfile']:
            elevation_list.append(round(coord['height']))
        self.elevation_list= elevation_list

    def print_data(self):
        print('ELEVATIONS')
        for elevation in self.elevation_list:
            print(elevation)
