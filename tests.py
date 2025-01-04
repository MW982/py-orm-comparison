from django_orm import DjangoAnalyzer, DjangoQueries
from peewee import PeeweeAnalyzer, PeeweeQueries
from sql_alchemy import SQLAlchemyAnalyzer, SQLAlchemyQueries
from utils import BaseQueries, BaseQueryAnalyzer

# TODO:
"""
1. Simple select x and y column 
 1a. With Joined table
 1b. Filtered by x
 1c. self joins
 1d. Group by 
 1e. distinct
2. Create x column
 2a. Create with a new joined row
 2b. Bulk creation
 2c. Bulk deletion
 2d. Bulk update
3. Transactions
4. CTEs
5. SubQueries 
6. Window Functions
7. Aggregation
 
"""


# @session
# def main(*args, **kwargs):
#    session = args[0]
#    print("x--------------------------------")
#    # print(session.query(Country))
#    # print("HI", args, kwargs)
#    query = select(Country)
#    print(session.execute(query))


def run_all_tests():
    orm_analyzers_mapping: dict[type[BaseQueries], type[BaseQueryAnalyzer]] = {
        SQLAlchemyQueries: SQLAlchemyAnalyzer,
        #        PeeweeQueries: PeeweeAnalyzer,
        #        DjangoQueries: DjangoAnalyzer,
    }
    orms = orm_analyzers_mapping.keys()
    tests = [
        method
        for method in vars(BaseQueries)
        if callable(getattr(BaseQueries, method)) and not method.startswith("__")
    ]

    for orm in orms:
        orm_instance = orm()
        for test in tests:
            print(orm_instance, test)

            orm_query = getattr(orm_instance, test)()
            analyzer_instance = orm_analyzers_mapping[orm](orm_query)
            print(orm_query, analyzer_instance, orm_instance)
            print("xxx", analyzer_instance.exec())


run_all_tests()
