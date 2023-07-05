import csv
import logging

import sqlalchemy
from sqlalchemy.exc import IntegrityError

from addresses_heat_maps.db.core import engine, session, Model
from addresses_heat_maps.db.models import ChargingStation, Address


def is_data_loaded() -> bool:
    return \
        sqlalchemy.inspect(engine).has_table(ChargingStation.__tablename__) and \
        sqlalchemy.inspect(engine).has_table(Address.__tablename__)


def load_csv(csv_filename: str, model: Model):
    n = 0
    with open(csv_filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            session.add(
                model.from_row(row)
            )
            try:
                session.commit()
                n += 1
            except IntegrityError as e:
                session.rollback()
                logging.info(str(e))

    logging.info(f'{n} inserted')
