"""Support for Google Places API."""
from datetime import timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_NAME,CONF_ADDRESS)
from homeassistant.helpers.entity import Entity
from requests.exceptions import ConnectionError as ConnectError, HTTPError, Timeout
import homeassistant.helpers.config_validation as cv
import logging
import livepopulartimes
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Required(CONF_ADDRESS): cv.string,
    }
)

SCAN_INTERVAL = timedelta(minutes=10)

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config['name']
    address = config['address']
    add_entities([PopularTimesSensor(name, address)], True)


class PopularTimesSensor(Entity):

    def __init__(self, name, address):
        self._name = name
        self._address = address
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
            result = livepopulartimes.get_populartimes_by_address(self._address)

            self._attributes['address'] = result["address"]
            self._attributes['maps_name'] = result["name"]
            self._attributes['popularity_monday'] = result["populartimes"][0]["data"]
            self._attributes['popularity_tuesday'] = result["populartimes"][1]["data"]
            self._attributes['popularity_wednesday'] = result["populartimes"][2]["data"]
            self._attributes['popularity_thursday'] = result["populartimes"][3]["data"]
            self._attributes['popularity_friday'] = result["populartimes"][4]["data"]
            self._attributes['popularity_saturday'] = result["populartimes"][5]["data"]
            self._attributes['popularity_sunday'] = result["populartimes"][6]["data"]

            popularity = result.get('current_popularity', 0)
            self._state = popularity
                
        except:
            _LOGGER.error("No popularity info is returned by the populartimes library.")