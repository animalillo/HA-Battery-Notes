# Home Assistant Battery Notes

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]

[![Community Forum][forum-shield]][forum]

_Integration to add battery notes to a device._

![Battery Notes](https://github.com/andrew-codechimp/HA-Battery-Notes/blob/main/images/screenshot-device.png "Battery Notes")

**This integration will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show battery type.

## Installation

### HACS

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=andrew-codechimp&repository=HA-Battery-Notes&category=Integration)

Or  
Search for `Battery Notes` in HACS and install it under the "Integrations" category.  
Restart Home Assistant  
In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Battery Notes"  

### Manual Installation

<details>
<summary>Show detailed instructions</summary>
1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `battery_notes`.
1. Download _all_ the files from the `custom_components/battery_notes/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Battery Notes"
</details>

## Configuration is done in the UI

On the "Configuration" -> "Integrations" -> "Battery Notes" screen add a new device, pick your device with a battery and add the battery type.  
The battery type will then be displayed as a diagnotic sensor on the device.  

## Automatic discovery

By default Battery Notes will automatically discover devices that it has in its library and create a notification to add a battery note.
If you wish to disable this functionality then add the following to your ```configuration.yaml```  
```
battery_notes:
  enable_autodiscovery: false
```

## Contributing to the Battery Library

The battery library is a JSON document at ```custom_components/battery_notes/data/library.json```  
To contribute, fork the repository, add your device details to the JSON document and submit a pull request.  
Please keep devices in alphabetical order by manufacturer/model.  
The manufacturer and model should be exactly what is displayed on the Device screen within Home Assistant.  The make & model names may be different between integrations such as Zigbee2MQTT and ZHA, if you see a similar device please duplicate the entry rather than changing it.   

For the example image below your JSON entry will look like this  

```
{
    "manufacturer": "Philips",
    "model": "Hue motion sensor (9290012607)",
    "battery_type": "AAA",
    "battery_quantity": 2
},
```  

Note that the ```battery_quantity``` is numeric (no quotes) and optional, if a device only has one battery it should be omitted.  

![Device Details](https://github.com/andrew-codechimp/HA-Battery-Notes/blob/main/images/screenshot-device-info.png "Device Details")
<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Acknowledgements

A lot of the inspiration for this integration came from the excellent [PowerCalc by bramstroker](https://github.com/bramstroker/homeassistant-powercalc), without adapting code from PowerCalc I'd never have worked out how to add additional sensors to a device.

<!---->
[battery_notes]: https://github.com/andrew-codechimp/HA-Battery-Notes
[commits-shield]: https://img.shields.io/github/commit-activity/y/andrew-codechimp/HA-Battery-Notes.svg?style=for-the-badge
[commits]: https://github.com/andrew-codechimp/HA-Battery-Notes/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/t/custom-component-battery-notes/613821
[license-shield]: https://img.shields.io/github/license/andrew-codechimp/HA-Battery-Notes.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/andrew-codechimp/HA-Battery-Notes.svg?style=for-the-badge
[releases]: https://github.com/andrew-codechimp/HA-Battery-Notes/releases
