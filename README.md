# hass-populartimes

## Description
This is a custom component for Home Assistant.
The component generates a sensor which shows the current popularity for a place which can be found in Google Maps using the Places API.

Sensor attributes are also generated which indicate past popularity at each hour of the day. 

For this to work you need a Google Places API key. There are limits for how many calls you can do for free per month.
More info can be found [here](https://developers.google.com/places/web-service/usage-and-billing).
For this reason I have limited the update time for the sensor to once every 10 minutes. 

## Getting required info
- Get a Google Maps API key https://developers.google.com/places/web-service/get-api-key
- Get the Places Id for which you want to see the popularity here: https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder

## Installation
Put the contents of the populartimes folder in your home assistant custom_components folder.

## Configuration

```yaml
sensor:
  platform: populartimes
  api_key: 'your-api-key-here'
  id: 'your_google_places_id_here'
  name: 'your_sensor_name_here'
```

## Links:
[Home Assistant Community Topic](https://community.home-assistant.io/)

## Credits

This component uses the [populartimes](https://github.com/m-wrzr/populartimes) library by [m-wrzr](https://github.com/m-wrzr).