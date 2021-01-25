import time
import requests
import json


def read_token():
    with open('/home/nearha/myprivvacy/DESIRE/python.vn/ex9/token_key.txt') as f:
        return f.read()


def take_fifty_locations(coordinator, radious, keyword):
    api = read_token()[:-1]
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}&radius={}&keyword={}&key={}'.format(
        coordinator, radious, keyword, api)
    url_respond = requests.get(url)
    google_data = url_respond.json()
    geodict = {"type": "FeatureCollection", "features": []}
    for point in google_data['results']:
        point_coordinates = [point['geometry']['location']
                             ['lng'], point['geometry']['location']['lat']]
        point_name = point['name']
        point_address = point['vicinity']
        infor_of_point = {"type": "Feature",
                          "geometry": {"type": "Point", "coordinates": point_coordinates},
                          "properties": {"Address": point_address, "name": point_name}}
        geodict['features'].append(infor_of_point)
    number_of_points = len(geodict['features'])
    while (number_of_points < 50) and ('next_page_token' in list(google_data.keys())):
        time.sleep(5)
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={}&key={}'.format(
            google_data['next_page_token'], api)
        url_respond = requests.get(url)
        google_data = url_respond.json()
        for point in google_data['results']:
            point_coordinates = [point['geometry']['location']
                                 ['lng'], point['geometry']['location']['lat']]
            point_name = point['name']
            point_address = point['vicinity']
            infor_of_point = {"type": "Feature",
                              "geometry": {"type": "Point", "coordinates": point_coordinates},
                              "properties": {"Address": point_address, "name": point_name}}
            geodict['features'].append(infor_of_point)
        number_of_points = len(geodict['features'])
    print('there are {} desired points which were found'.format(number_of_points))
    return geodict


def map_generation(geodict):
    with open("map.geojson", "w") as outfile:
        json.dump(geodict, outfile)


def main():
    keyword = 'beer'
    coordinator = '21.012754, 105.821771'
    radious = 2000
    geodict = take_fifty_locations(coordinator, radious, keyword)
    map_generation(geodict)


if __name__ == '__main__':
    main()
