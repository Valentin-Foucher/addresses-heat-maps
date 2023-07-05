from sqlalchemy import Column, Boolean, Float, String

from addresses_heat_maps.db.core import Model


class ChargingStation(Model):
    __tablename__ = 'charging_stations'

    id = Column('id', String, primary_key=True)
    x = Column('x', Float)
    y = Column('y', Float)
    free = Column('free', Boolean)

    @classmethod
    def from_row(cls, row: dict[str, str]) -> 'ChargingStation':
        return ChargingStation(
            id=row['coordonneesXY'],
            free=True if row['gratuit'] == 'true' else False,
            x=float(row['X']),
            y=float(row['Y'])
        )


class Address(Model):
    __tablename__ = 'addresses'

    id = Column('id', String, primary_key=True)
    x = Column('x', Float)
    y = Column('y', Float)

    @classmethod
    def from_row(cls, row: dict[str, str]) -> 'Address':
        return Address(
            id=row['id'],
            x=float(row['lon']),
            y=float(row['lat'])
        )
