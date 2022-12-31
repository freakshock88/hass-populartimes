# hass-populartimes
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

## Description
This is a custom component for Home Assistant.
The component generates a sensor which shows the current popularity for a place which can be found in Google Maps using the Places API.

Sensor attributes are also generated which indicate past popularity at each hour of the day. 

## Updated requirements

Since updating to a new fork of populartimes, a Google Places API key or Places Id is no longer required.

## Installation
Either:
1. Install via HACS
2. Download files as zip and put the contents of the populartimes folder in your home assistant custom_components folder.


## Configuration

```yaml
sensor:
  platform: populartimes
  name: 'your_sensor_name_here'
  address: 'your_address_here'
```
The address should preferably be in the following format:
"(location name) , full address, city, province/state/etc, country"

## Live vs historical data
Sometimes Google Maps does not provide live popularity data for the place you want to query.
In that case the historical data is used to set the sensor state.
To indicate this, the attribute `popularity_is_live` is set to `false`.

## Links:
[Home Assistant Community Topic](https://community.home-assistant.io/t/google-maps-places-popular-times-component/147362)

## Credits

This component uses the [LivePopularTimes](https://github.com/GrocerCheck/LivePopularTimes) library, which is a fork of the previously used [populartimes](https://github.com/m-wrzr/populartimes) library.
