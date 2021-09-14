from app.constants import DEFAULT_READ_CAPACITY_UNITS, DEFAULT_WRITE_CAPACITY_UNITS
from app.models import ALL_MODELS


def init_db() -> None:
    """Clear existing data and create new tables."""
    for model in ALL_MODELS:
        if not model.exists():
            model.create_table(read_capacity_units=DEFAULT_READ_CAPACITY_UNITS,
                               write_capacity_units=DEFAULT_WRITE_CAPACITY_UNITS)
