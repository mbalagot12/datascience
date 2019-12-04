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

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
username = os.getenv("MERIDIAN_USER")
password = os.getenv("MERIDIAN_PASSWORD")
mauth = HTTPBasicAuth(username=username, password=password)


class Meridian:

    def __init__(self, location, **kwargs):
        self.location = location
        self.login_uri = f'{self.base_uri}/api/login'
        self.tokenId = self.getTokenId
        self.headers = {"Content-Type": "multipart/form-data", "Authorization": "Token " + str(self.tokenId)}
        self.base_uri = 'https://edit.meridianapps.com'
        self.beacons_uri = f'{self.base_uri}/api/locations/{self.location}/beacons'
        self.placemarks_uri = f'{self.base_uri}/api/locations/{self.location}/placemarks'
        self.locations_uri = f'{self.base_uri}/api/locations'
        self.campaigns_uri = f'{self.base_uri}/api/locations/{self.location}/campaigns'
        self.pages_uri = f'{self.base_uri}/api/locations/{location}/pages?page_size=100'
        self.feeds_uri = f'{{self.base_uri}}/api/locations/{self.location}/feeds'
        self.maps_uri = f'{self.base_uri}/api/locations/{self.location}/maps'
        self.search_uri = f'{self.base_uri}/locations/search?q={self.location}'
        self.org_uri = f'{self.base_uri}/api/organizations/{self.location}'
        self.endpoints = kwargs
        if 'placemark' in self.endpoints:
            self.placemark = kwargs['placemark']
        elif 'placemarkId' in self.endpoints:
            self.placemarkId = kwargs['placemarkId']
        elif 'image' in self.endpoints:
            self.image = kwargs['inmage']
        elif 'mac' in self.endpoints:
            self.mac = kwargs['mac']
        elif 'feedId' in self.endpoints:
            self.feedid = kwargs['feedid']
        elif 'mapId' in self.endpoints:
            self.mapId = kwargs['mapId']
        elif 'svg' in self.endpoints:
            self.svg = kwargs['svg']
        elif kwargs['fieldname']:
            self.fieldname = kwargs['fieldname']
        else:
            print('\n Error: Meridian endpoint specified does not exist.')

    def getTokenId(self):
        token = req.post(self.login_uri, {'password': password, 'email': username})
        return token.json()['token']

    def getBeacons(self):
        beacons = req.get(self.beacons_uri)
        return beacons

    def getPlacemarks(self):
        placemarks = req.get(self.placemarks_uri)
        return placemarks

    @property
    def createPlacemarks(self):
        placemarks = req.post(self.placemarks_uri, data=self.placemark, auth=mauth)
        return placemarks

    @createPlacemarks.setter
    def createPlacemarks(self, placemark):
        self.placemark = placemark

    @property
    def patchPlacemarks(self):
        placemarks_uri = f'{self.base_uri}/api/locations/{self.location}/placemarks/{self.placemarkId}'
        placemark = req.patch(placemarks_uri, data=None)
        return placemark

    @patchPlacemarks.setter
    def patchPlacemarks(self, placemarkId):
        self.placemarkId = placemarkId

    @property
    def deletePlacemarks(self):
        placemarks_uri = f'{self.base_uri}/api/locations/{self.location}/placemarks/{self.placemarkId}'
        placemark = req.delete(placemarks_uri)
        return placemark

    @deletePlacemarks.setter
    def deletePlacemarks(self, placemarkId):
        self.placemarkId = placemarkId

    @property
    def placemarkUploadImage(self):
        placemarks_uri = f'{self.base_uri}/api/locations/{self.location}/placemarks/{self.placemarkId}/image'
        placemark = req.put(placemarks_uri, data=None, headers=self.headers, files=self.image, auth=mauth)
        return placemark

    @placemarkUploadImage.setter
    def placemarkUploadImage(self, image):
        self.image = image

    @placemarkUploadImage.setter
    def placemarkUploadImage(self, placemarkId):
        self.placemarkId = placemarkId

    def getLocations(self):
        locations = req.get(self.locations_uri)
        return locations

    def get_beacon(self, mac):
        self.mac = mac
        beacons_uri = f'{self.base_uri}/api/locations/{self.location}/beacons/{self.mac}'
        beacon = req.get(beacons_uri)
        return beacon

    def get_beacon_changesets(self, mac):
        self.mac = mac
        beacons_uri = f'{self.base_uri}/api/locations/{self.location}/beacons/{self.mac}/changesets'
        beacon = req.get(beacons_uri)
        return beacon

    def get_campaigns(self):
        campaigns = req.get(self.campaigns_uri)
        return campaigns

    def get_pages(self):
        pages = req.get(self.pages_uri)
        return pages

    @property
    def get_events(self):
        events_uri = f'{{self.base_uri}}/api/locations/{self.location}/events?page_size={self.pages}'
        events = req.get(events_uri)
        return events

    @get_events.setter
    def get_events(self, pages=100):
        self.pages = pages

    def get_feeds(self):
        feeds = req.get(self.feeds_uri)
        return feeds

    @property
    def get_a_feed(self):
        feed_uri = f'{{self.base_uri}}/api/locations/{self.location}/feeds/{self.feedid}'
        feed = req.get(feed_uri)
        return feed

    @get_a_feed.setter
    def get_a_feed(self, feedid):
        self.feedid = feedid

    def create_map(self):
        maps = req.post(self.maps_uri, headers=self.headers, auth=mauth)
        return maps

    @property
    def upload_map(self):
        maps_uri = f'{self.base_uri}/api/locations/{self.location}/maps/{self.mapId}/svg'
        upload_map = req.put(maps_uri, headers=self.headers, files=self.svg, auth=mauth)
        return upload_map

    @upload_map.setter
    def upload_map(self, mapId):
        self.mapId = mapId

    @upload_map.setter
    def upload_map(self, svg):
        self.svg = svg

    @property
    def delete_map(self):
        maps_uri = f'{self.base_uri}/api/locations/{self.location}/maps/{self.mapid}/svg'
        upload_map = req.delete(maps_uri, headers=self.headers, files=self.svg, auth=mauth)
        return upload_map

    @delete_map.setter
    def delete_map(self, mapid):
        self.mapid = mapid

    @delete_map.setter
    def delete_map(self, svg):
        self.svg = svg

    def location_search(self):
        search = req.get(self.search_uri)
        return search

    @property
    def location_field(self):
        fieldname_uri = f'{self.base_uri}/locations/search?q={self.fieldname}:{self.location}'
        fieldname = req.get(fieldname_uri)
        return fieldname

    @location_field.setter
    def location_field(self, fieldname):
        self.fieldname = fieldname

    def get_org(self):
        org = req.get(self.org_uri)
        return org
