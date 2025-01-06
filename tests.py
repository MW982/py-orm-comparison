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


def run_all_tests():
    orm_analyzers_mapping: dict[type[BaseQueries], type[BaseQueryAnalyzer]] = {
        SQLAlchemyQueries: SQLAlchemyAnalyzer,
        # PeeweeQueries: PeeweeAnalyzer,
        DjangoQueries: DjangoAnalyzer,
    }
    orms = orm_analyzers_mapping.keys()
    tests = [
        method
        for method in vars(BaseQueries)
        if callable(getattr(BaseQueries, method)) and not method.startswith("__")
    ]

    for orm in orms:
        orm_instance = orm()
        print("======")
        print(orm)
        print("======")
        for test in tests:
            print("---->", test)
            # print(orm_instance, test)

            orm_query = getattr(orm_instance, test)()
            analyzer_instance = orm_analyzers_mapping[orm](orm_query)
            print(orm_query)
            # print(analyzer_instance.exec()[0].citizen.__dict__)
            print(analyzer_instance.query())

        print("======")


run_all_tests()
