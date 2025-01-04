from utils import BaseQueries, BaseQueryAnalyzer


class PeeweeQueries(BaseQueries):
    def select_x_and_y(self):
        orm_query = "select(Country)"
        return orm_query


class PeeweeAnalyzer(BaseQueryAnalyzer):
    pass
