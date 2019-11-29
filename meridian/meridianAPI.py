"""
########################################################################################################################
#
# meridianAPI.py
#
#
# Author: Miguel Balagot
# Email mbalagot@hpe.com
# 2017 HPE Aruba
#
#
########################################################################################################################
"""

import requests as req
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
base_uri = 'https://edit.meridianapps.com'


class Meridian:

    def __init__(self, location, mauth):
        self.location = location
        self.mauth = mauth
        self.token_id = self.getTokenId()


    def getTokenId(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        username = os.getenv("MERIDIAN_USER")
        password = os.getenv("MERIDIAN_PASSWORD")
        login_uri: str = 'https://edit.meridianapps.com/api/login'
        token = req.post(login_uri, {'password': password, 'email': username})
        mauth = HTTPBasicAuth(username=username, password=password)
        return token.json()['token'] and mauth

    def getBeacons(self):
        beacons_uri = f'https://edit.meridianapps.com/api/locations/{self}/beacons'
        beacons = req.get(beacons_uri)
        return beacons

    def getPlacemarks(self):
        placemarks_uri = f'https://edit.meridianapps.com/api/locations/{self}/placemarks'
        print(placemarks_uri)
        placemarks = req.get(placemarks_uri)
        return placemarks

    def createPlacemarks(self, placemark):
        self.placemark = placemark
        placemarks_uri = f'https://edit.meridianapps.com/api/locations/{self}/placemarks'
        placemarks = req.post(placemarks_uri, data=self.placemark, auth=self.mauth)
        return placemarks

    def patchPlacemarks(self, placemarkId):
        self.placemarkId = placemarkId
        placemarks_uri = f'https://edit.meridianapps.com/api/locations/{self}/placemarks/ {self.placemarkId}'
        placemark = req.patch(placemarks_uri, data=None)
        return placemark

    def deletePlacemarks(self, placemarkId):
        self.placemarkId = placemarkId
        placemarks_uri = f'https://edit.meridianapps.com/api/locations/{self}/placemarks/{self.placemarkId}'
        placemark = req.delete(placemarks_uri)
        return placemark

    def placemarkUploadImage(self, image, placemarkId):
        self.image = image
        self.placemarkId = placemarkId
        headers = {'Content-Type': 'multipart/form-data',
                   'Authorization': 'Token ' + self.tokenId}
        placemarks_uri = f'https://edit.meridianapps.com/api/locations/{self}/placemarks/{self.placemarkId}/image'
        placemark = req.put(placemarks_uri, data=None, headers=headers, files=self.image, auth=self.mauth)
        return placemark

    def getLocations(self):
        locations_uri = f'https://edit.meridianapps.com/api/locations'
        locations = req.get(self)
        return locations

    def get_beacon(self, mac):
        self.mac = mac
        beacons_uri = f'https://edit.meridianapps.com/api/locations/{self}/beacons/{self.mac}'
        beacon = req.get(beacons_uri)
        return beacon

    def get_beacon_changesets(self, mac):
        self.mac = mac
        beacons_uri = f'https://edit.meridianapps.com/api/locations/{self}/beacons/{self.mac}/changesets'
        beacon = req.get(beacons_uri)
        return beacon

    def get_campaings(self):
        campaigns_uri = f'https://edit.meridianapps.com/api/locations/{self}/campaigns'
        campaigns = req.get(campaigns_uri)
        return campaigns

    def get_pages(self):
        pages_uri = f'{base_uri}/api/locations/{self}/pages?page_size=100'
        pages = req.get(pages_uri)
        return pages

    def get_events(self):
        events_uri = f'{base_uri}/api/locations/{self}/events?page_size=100'
        events = req.get(events_uri)
        return events

    def get_feeds(self):
        feeds_uri = f'{base_uri}/api/locations/{self}/feeds'
        feeds = req.get(feeds_uri)
        return feeds

    def get_a_feed(self, feedid):
        self.feedid = feedid
        feed_uri = f'{base_uri}/api/locations/{self}/feeds/{self.feedid}'
        feed = req.get(feed_uri)
        return feed

    def creat_a_map(self):
        maps_uri = f'{base_uri}/api/locations/{self}/maps'
        headers = {'Content-Type': 'multipart/form-data',
                   'Authorization': 'Token ' + self.tokenId}
        map = req.post(maps_uri, headers=headers, auth=self.mauth)
        return map

    def upload_a_map(self, mapid, svg):
        self.mapid = mapid
        self.svg = svg
        headers = {'Content-Type': 'multipart/form-data',
                   'Authorization': 'Token ' + self.tokenId}
        maps_uri = f'{base_uri}/api/locations/{self}/maps/{self.mapid}/svg'
        upload_map = req.put(maps_uri, headers=headers, files=self.svg, auth=self.mauth)
        return upload_map

    def delete_map(self, mapid, svg):
        self.mapid = mapid
        self.svg = svg
        headers = {'Content-Type': 'multipart/form-data',
                   'Authorization': 'Token ' + self.tokenId}
        maps_uri = f'{base_uri}/api/locations/{self}/maps/{self.mapid}/svg'
        upload_map = req.delete(maps_uri, headers=headers, files=self.svg, auth=self.mauth)
        return upload_map

    def location_search(self):
        search_uri = f'{base_uri}/locations/search?q={self}'
        search = req.get(search_uri)
        return search

    def location_search_field(self, fieldname):
        self.fieldname = fieldname
        fieldname_uri = f'{base_uri}/locations/search?q={self.fieldname}:{self}'
        fieldname = req.get(fieldname_uri)
        return fieldname

    def get_org(self):
        org_uri = f'{base_uri}/api/organizations/{self}'
        org = req.get(org_uri)
        return org







