#Project 3 Kevin Yin 29211757
#connections

import json
import urllib.parse
import urllib.request
from mapquest_json import *
from mapquest_class import *

def interface()-> None:

    locations_list= create_locations_list()
    output_list= create_output_list()
    
    try:
        url= build_url_directions(locations_list)
        json = get_result(url)
    except:
        print('')
        print('MAPQUEST ERROR')
        return
    if json['route']['routeError']['errorCode'] == 0:
        print('')
        print('NO ROUTE FOUND')
        return
    object_list= create_object_list(output_list, json)
    print('')
    for output in object_list:
        output.print_data()
        print('')
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

def create_output_list() -> list:
    '''
    Asks user for how many outputs they would like, then appnds those options to a list
    '''
    outputs= int(input())
    output_list= []
    for output in range(outputs):
        option= input()
        output_list.append(option)

    return output_list

def create_locations_list() -> list:
    '''
    Asks user for how many locations they would like, then appends those locations to a list
    '''
    location_number = int(input())
    locations_list = []
    for x in range(location_number):
        locations_list.append((input()))

    return locations_list

def create_object_list(output_list: 'list of outputs', json: 'JSON'):
    '''
    This function takes in a list of outputs containing the ouputs that the user wants to print
    out and appends the corresponding objects it to a list
    '''
    object_list= []
    for option in output_list:
        if option == 'STEPS':
            object_list.append(STEPS(json))
        elif option == 'TOTALTIME':
            object_list.append(TOTALTIME(json))
        elif option == 'TOTALDISTANCE':
            object_list.append(TOTALDISTANCE(json))
        elif option == 'LATLONG':
            object_list.append(LATLONG(json))
        elif option == 'ELEVATION':
            object_list.append(ELEVATION(LATLONG(json)))

    return object_list


if __name__ == '__main__':  
    interface()
