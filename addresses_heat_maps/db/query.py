from sqlalchemy import text

from addresses_heat_maps.db.core import session
from addresses_heat_maps.db.models import ChargingStation, Address


def get_charging_stations_k_colouring_for_addresses(max_distance: float = 0.001) -> (float, float, int):
    a = Address.__tablename__
    s = ChargingStation.__tablename__

    result = session.execute(text(f'WITH "precalc" AS (\n'
                                  f'  SELECT {a}.x AS x, {a}.y AS y'
                                  f'  FROM {a}\n'
                                  f'  CROSS JOIN {s}\n'
                                  f'  WHERE free IS true AND SQRT(POWER({a}.x - {s}.x, 2) + POWER({a}.y - {s}.y, 2)) < :max_distance\n'
                                  f')\n'
                                  f'SELECT x, y, COUNT(*) as colouring\n'
                                  f'FROM precalc\n'
                                  f'GROUP BY x, y\n'
                                  f'ORDER BY x, y\n'
                                  'LIMIT 1000'), {'max_distance': max_distance}).all()

    return result
