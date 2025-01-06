import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testingapp.settings")

import django

django.setup()

from django.db.models import Count

from testmodels.models import Area, Citizen, Country, GovernmentFacility
from utils import BaseQueries, BaseQueryAnalyzer


class DjangoQueries(BaseQueries):
    def select_country_all(self) -> str:
        return "Country.objects.all()"

    def select_country_id_and_name(self) -> str:
        return "Country.objects.all().values_list('id', 'name')"

    def select_with_where(self) -> str:
        return "Country.objects.filter(name='Poland').order_by('founding_date')"

    def select_with_join(self):
        return "Citizen.objects.select_related('area').values_list('id', 'area__name')"

    def group_by(self):
        return "Citizen.objects.values('last_name').annotate(count=Count('id')).order_by().values_list('id', 'name', 'last_name', 'area_id')"


class DjangoAnalyzer(BaseQueryAnalyzer):
    def query(self) -> str:
        return eval(self.orm_query).query

    def exec(self):
        return eval(self.orm_query)
