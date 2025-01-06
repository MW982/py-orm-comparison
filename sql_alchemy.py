import logging
import os

from sqlalchemy import create_engine, func, select
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from utils import BaseQueries, BaseQueryAnalyzer

logging.basicConfig(filename="logfile.txt", level=logging.DEBUG)
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)

db_path = os.path.abspath(os.getcwd()) + "/db.sqlite3"
engine = create_engine(f"sqlite:////{db_path}", echo=False, echo_pool=False)

Base = automap_base()
Base.prepare(autoload_with=engine)

Country = Base.classes.country
Area = Base.classes.area
Citizen = Base.classes.citizen
GovernemntFacility = Base.classes.government_facility


class SQLAlchemyQueries(BaseQueries):
    def select_country_all(self) -> str:
        return "select(Country)"

    def select_country_id_and_name(self) -> str:
        return "select(Country.id, Country.name)"

    def select_with_where(self):
        return "select(Country).where(Country.name == 'Poland').order_by(Country.founding_date)"

    def select_with_join(self):
        return "select(Country).join(Area)"

    def select_with_multiple_joins(self):
        return ""

    def group_by(self):
        return "select(Citizen, func.count(Citizen.id)).group_by(Citizen.last_name)"


class SQLAlchemyAnalyzer(BaseQueryAnalyzer):
    def query(self) -> str:
        return str(eval(self.orm_query).compile(compile_kwargs={"literal_binds": True}))

    def exec(self):
        with Session(engine) as session:
            return session.execute(eval(self.orm_query)).all()
