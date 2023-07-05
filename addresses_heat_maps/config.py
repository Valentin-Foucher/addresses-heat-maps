from typing import Any

import yaml

from addresses_heat_maps.utils.object_utils import get_nested_element


def load_config(config_filename: str = 'configuration.yaml') -> dict[str, Any]:
    with open(config_filename) as config_file:
        return yaml.load(config_file, Loader=yaml.SafeLoader)


def get(path: str) -> Any:
    return get_nested_element(_config, path)


_config = load_config()
