from sqlalchemy import Column
from sqlalchemy.types import Unicode
from sqlalchemy.types import Integer
from sqlalchemy.types import Float

from notaliens.core.models import Base
from notaliens.core.models.translation import TranslatableMixin
from notaliens.core.models import JsonSerializableMixin


class Country(Base, TranslatableMixin, JsonSerializableMixin):
    __translatables__ = ['name', 'official_name']
    name = Column(Unicode(128), nullable=False)
    official_name = Column(Unicode(128), nullable=True)
    alpha2 = Column(Unicode(128), nullable=True)
    alpha3 = Column(Unicode(128), nullable=True)
    numeric = Column(Integer, nullable=True)


class GeoRegion(Base):
    country = Column(Unicode(128), nullable=False)
    region = Column(Unicode(128), nullable=True)
    city = Column(Unicode(128), nullable=True)
    postal_code = Column(Unicode(128), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    metro_code = Column(Unicode(128), nullable=True)
    area_code = Column(Unicode(128), nullable=True)


class Currency(Base, TranslatableMixin):
    __translatables__ = ['name', 'letter']
    name = Column(Unicode(128), nullable=False)
    letter = Column(Unicode(128), nullable=False, unique=True)


class Language(Base, TranslatableMixin):
    __translatables__ = ['name']
    name = Column(Unicode(128), nullable=False)
    alpha3_bib = Column(Unicode(128), nullable=False)
    alpha3_term = Column(Unicode(128), nullable=False)
    alpha2 = Column(Unicode(128), nullable=False)

    def __json__(self, request):
        return {'pk': self.pk, 'name': self.name.encode('utf-8')}


class Timezone(Base, TranslatableMixin):
    __translatables__ = ['name']
    name = Column(Unicode(128), nullable=False)


def get_region_by_postal(session, postal_code):
    region = session.query(GeoRegion).filter(
        GeoRegion.postal_code == postal_code
    ).one()

    return region

def get_country_by_alpha2(session, alpha2):
    country = session.query(Country).filter(
        Country.alpha2 == alpha2
    ).one()

    return country
