from meridian import get_token_id, mylocation, mauth, headers
from meridian import meridianAPI
import pandas as pd

#from . meridianAPI import Meridian


placemarks = {'map': 123456,
               'x': 0,
              'y': 0,
              'type': 'elevator'
             }

mr = meridianAPI.Meridian

print(mr.getPlacemarks(mylocation))

print(mr.getPlacemarks(mylocation).json()['results'])

placemarks = mr.getPlacemarks(mylocation).json()['results']

print(pd.DataFrame(placemarks))

beacons = pd.DataFrame(mr.getBeacons(mylocation).json()['results'])

print(beacons.get('latitude'))