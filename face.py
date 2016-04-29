import facebook
import urllib
import urlparse
import warnings
import requests
import json

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID     = '693172180786480'
FACEBOOK_APP_SECRET = 'c3b0e3087cc7a8f5554ef1504cfd2b91'


# Trying to get an access token. Very awkward.
oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')

oauth_response = requests.get("https://graph.facebook.com/oauth/access_token?" + urllib.urlencode(oauth_args)).text

try:
  oauth_access_token = urlparse.parse_qs(oauth_response)['access_token'][0]
except KeyError:
  print('Unable to grab an access token!')
  exit(1)

graph = facebook.GraphAPI(access_token=oauth_access_token, version="2.2")

# Try to post something on the wall.
try:
  graph.put_wall_post(parent_object="997135347069351",
                      connection_name="feed",
                      message="Hello, world")
  print fb_response
except facebook.GraphAPIError as e:
  print 'Something went wrong:', e.type, e.message, e.code