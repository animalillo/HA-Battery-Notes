"""Battery Type library for battery_notes."""
from __future__ import annotations

import json
import logging
import os
from typing import NamedTuple

BUILT_IN_DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), "../data")

_LOGGER = logging.getLogger(__name__)


class Library:
    """Hold all known battery types."""

    def __init__(self) -> None:
        json_path = os.path.join(BUILT_IN_DATA_DIRECTORY, "library.json")

        try:
            with open(json_path, encoding="utf-8") as file:
                json_data = json.load(file)

                self._devices = json_data["devices"]

        except FileNotFoundError:
            _LOGGER.error(
                "library.json file not found in directory %s", BUILT_IN_DATA_DIRECTORY
            )

    async def get_device_battery_details(
        self,
        manufacturer: str,
        model: str,
    ) -> DeviceBatteryDetails | None:
        """Create a battery details object from the JSON devices data."""

        for device in self._devices:
            if device["manufacturer"] == manufacturer and device["model"] == model:
                device_battery_details = DeviceBatteryDetails(
                    manufacturer=device["manufacturer"],
                    model=device["model"],
                    battery_type=device["battery_type"],
                    battery_quantity=device["battery_quantity"],
                )
                return device_battery_details

        return None


class DeviceBatteryDetails(NamedTuple):
    """Describes a device battery type."""

    manufacturer: str
    model: str
    battery_type: str
    battery_quantity: int


class ModelInfo(NamedTuple):
    """Describes a device."""

    manufacturer: str
    model: str