class BaseQueries:
    def select_country_all(self) -> str:
        raise NotImplementedError

    def select_country_id_and_name(self):
        raise NotImplementedError

    def select_with_where(self):
        raise NotImplementedError

    def select_with_join(self):
        raise NotImplementedError

    def group_by(self):
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
