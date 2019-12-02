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


class Meridian:

    def __init__(self, location):
        self.location = location
        self.tokenId, self.mauth = self.getTokenId
        self.headers = {"Content-Type": "multipart/form-data", "Authorization": "Token " + str(self.tokenId)}
        self.base_uri = 'https://edit.meridianapps.com'

    @property
    def getTokenId(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        username = os.getenv("MERIDIAN_USER")
        password = os.getenv("MERIDIAN_PASSWORD")
        login_uri = f'{self.base_uri}/api/login'
        token = req.post(login_uri, {'password': password, 'email': username})
        mauth = HTTPBasicAuth(username=username, password=password)
        return token.json()['token'], mauth

    @property
    def getBeacons(self):
        beacons_uri = f'{self.base_uri}/api/locations/{self.location}/beacons'
        beacons = req.get(beacons_uri)
        return beacons

    @property
    def getPlacemarks(self):
        placemarks_uri = f'{self.base_uri}/api/locations/{self}/placemarks'
        placemarks = req.get(placemarks_uri)
        return placemarks

    def createPlacemarks(self, placemark):
        self.placemark = placemark
        placemarks_uri = f'{self.base_uri}/api/locations/{self}/placemarks'
        placemarks = req.post(placemarks_uri, data=self.placemark, auth=self.mauth)
        return placemarks

    def patchPlacemarks(self, placemarkId):
        self.placemarkId = placemarkId
        placemarks_uri = f'{self.base_uri}/api/locations/{self}/placemarks/ {self.placemarkId}'
        placemark = req.patch(placemarks_uri, data=None)
        return placemark

    def deletePlacemarks(self, placemarkId):
        self.placemarkId = placemarkId
        placemarks_uri = f'{self.base_uri}/api/locations/{self}/placemarks/{self.placemarkId}'
        placemark = req.delete(placemarks_uri)
        return placemark

    def placemarkUploadImage(self, image, placemarkId):
        self.image = image
        self.placemarkId = placemarkId
        placemarks_uri = f'{self.base_uri}/api/locations/{self}/placemarks/{self.placemarkId}/image'
        placemark = req.put(placemarks_uri, data=None, headers=self.headers, files=self.image, auth=self.mauth)
        return placemark

    def getLocations(self):
        locations_uri = f'{self.base_uri}/api/locations'
        locations = req.get(self)
        return locations

    def get_beacon(self, mac):
        self.mac = mac
        beacons_uri = f'{self.base_uri}/api/locations/{self}/beacons/{self.mac}'
        beacon = req.get(beacons_uri)
        return beacon

    def get_beacon_changesets(self, mac):
        self.mac = mac
        beacons_uri = f'{self.base_uri}/api/locations/{self}/beacons/{self.mac}/changesets'
        beacon = req.get(beacons_uri)
        return beacon

    def get_campaings(self):
        campaigns_uri = f'{self.base_uri}/api/locations/{self}/campaigns'
        campaigns = req.get(campaigns_uri)
        return campaigns

    def get_pages(self):
        pages_uri = f'{self.base_uri}/api/locations/{self}/pages?page_size=100'
        pages = req.get(pages_uri)
        return pages

    def get_events(self):
        events_uri = f'{{self.base_uri}}/api/locations/{self}/events?page_size=100'
        events = req.get(events_uri)
        return events

    def get_feeds(self):
        feeds_uri = f'{{self.base_uri}}/api/locations/{self}/feeds'
        feeds = req.get(feeds_uri)
        return feeds

    def get_a_feed(self, feedid):
        self.feedid = feedid
        feed_uri = f'{{self.base_uri}}/api/locations/{self}/feeds/{self.feedid}'
        feed = req.get(feed_uri)
        return feed

    def creat_map(self):
        maps_uri = f'{self.base_uri}/api/locations/{self}/maps'
        map = req.post(maps_uri, headers=self.headers, auth=self.mauth)
        return map

    def upload_a_map(self, mapid, svg):
        self.mapid = mapid
        self.svg = svg
        maps_uri = f'{self.base_uri}/api/locations/{self}/maps/{self.mapid}/svg'
        upload_map = req.put(maps_uri, headers=self.headers, files=self.svg, auth=self.mauth)
        return upload_map

    def delete_map(self, mapid, svg):
        self.mapid = mapid
        self.svg = svg
        maps_uri = f'{self.base_uri}/api/locations/{self}/maps/{self.mapid}/svg'
        upload_map = req.delete(maps_uri, headers=self.headers, files=self.svg, auth=self.mauth)
        return upload_map

    def location_search(self):
        search_uri = f'{self.base_uri}/locations/search?q={self}'
        search = req.get(search_uri)
        return search

    def location_search_field(self, fieldname):
        self.fieldname = fieldname
        fieldname_uri = f'{self.base_uri}/locations/search?q={self.fieldname}:{self}'
        fieldname = req.get(fieldname_uri)
        return fieldname

    def get_org(self):
        org_uri = f'{self.base_uri}/api/organizations/{self}'
        org = req.get(org_uri)
        return org
