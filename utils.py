class BaseQueries:
    def select_x_and_y(self):
        raise NotImplementedError


class BaseQueryAnalyzer:
    def __init__(self, orm_query: str):
        self.orm_query: str = orm_query

    def _get_sql_query(self):
        raise NotImplementedError

    def query(self) -> str:
        raise NotImplementedError

    def exec(self):
        raise NotImplementedError
