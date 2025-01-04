import os

from sqlalchemy import create_engine, select
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from utils import BaseQueries, BaseQueryAnalyzer

db_path = os.path.abspath(os.getcwd()) + "/db.sqlite3"
engine = create_engine(f"sqlite:////{db_path}", echo=True)

Base = automap_base()
Base.prepare(autoload_with=engine)

Country = Base.classes.country
Area = Base.classes.area
Citizen = Base.classes.citizen
GovernemntFacility = Base.classes.government_facility


def session(func):
    def inner():
        print("-------------")
        print("START SESSION")

        with Session(engine) as session:
            func(session)

    return inner


class SQLAlchemyQueries(BaseQueries):
    def select_x_and_y(self):
        orm_query = "select(Country)"
        return orm_query


class SQLAlchemyAnalyzer(BaseQueryAnalyzer):

    def exec(self):
        print("TEST")
