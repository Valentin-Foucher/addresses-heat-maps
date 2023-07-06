import logging
import os

from addresses_heat_maps import config
from addresses_heat_maps.db.core import init_db, Model

from addresses_heat_maps.db.models import ChargingStation, Address
from addresses_heat_maps.db.query import get_charging_stations_k_colouring_for_addresses
from addresses_heat_maps.utils.db_utils import is_data_loaded, load_csv

logging.basicConfig(level=logging.INFO)

data_loaded = is_data_loaded()

logging.info('Initializing database...')
init_db()


def load_data_from_directory(addr_dir: str, model: Model):
    for file in os.listdir(addr_dir):
        load_csv(f'{addr_dir}/{file}', model)


if not data_loaded:
    logging.info('Data not stored yet, inserting charging stations...')
    load_data_from_directory(config.get('data.charging_stations_directory'), ChargingStation)

    logging.info('Inserting addresses...')
    load_data_from_directory(config.get('data.addresses_directory'), Address)

    logging.info('Done')

else:
    logging.info('Data already loaded proceeding')


print(get_charging_stations_k_colouring_for_addresses())
