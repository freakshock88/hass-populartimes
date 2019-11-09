"""Support for Google Places API."""
from datetime import timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_API_KEY,CONF_ID,CONF_NAME)
from homeassistant.helpers.entity import Entity
from requests.exceptions import ConnectionError as ConnectError, HTTPError, Timeout
import homeassistant.helpers.config_validation as cv
import populartimes
import voluptuous as vol

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_ID): cv.string,
        vol.Required(CONF_NAME): cv.string,
    }
)

SCAN_INTERVAL = timedelta(minutes=10)

def setup_platform(hass, config, add_entities, discovery_info=None):
    api_key = config['api_key']
    id = config['id']
    name = config['name']
    add_entities([PopularTimesSensor(api_key, id, name)], True)


class PopularTimesSensor(Entity):

    def __init__(self, api_key, id, name):
        self._api_key = api_key
        self._id = id
        self._name = name
        self._state = None

        self._attributes = {
            'maps_name': None,
            'address': None,
            'popularity_monday': None,
            'popularity_tuesday': None,
            'popularity_wednesday': None,
            'popularity_thursday': None,
            'popularity_friday': None,
            'popularity_saturday': None,
            'popularity_sunday': None,
        }

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return '%'

    @property
    def state_attributes(self):
        return self._attributes

    def update(self):
        """Get the latest data from Google Places API."""
        try:
            result = populartimes.get_id(
                self._api_key,
                self._id
            )

            try:
                current_popularity = result["current_popularity"]
                self._state = current_popularity
            except:
                self._state = 0

            self._attributes['address'] = result["address"]
            self._attributes['maps_name'] = result["name"]
            self._attributes['popularity_monday'] = result["populartimes"][0]["data"]
            self._attributes['popularity_tuesday'] = result["populartimes"][1]["data"]
            self._attributes['popularity_wednesday'] = result["populartimes"][2]["data"]
            self._attributes['popularity_thursday'] = result["populartimes"][3]["data"]
            self._attributes['popularity_friday'] = result["populartimes"][4]["data"]
            self._attributes['popularity_saturday'] = result["populartimes"][5]["data"]
            self._attributes['popularity_sunday'] = result["populartimes"][6]["data"]
        except (ConnectError, HTTPError, Timeout, ValueError) as error:
            _LOGGER.error(
                "Unable to connect to Google Place API: %s", error)
            self._state = None
