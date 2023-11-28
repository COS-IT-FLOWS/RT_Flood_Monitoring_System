import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine
import confuse


source = confuse.YamlSource('config.yaml')
config = confuse.RootView([source])

dbAuth = config['database'].get()


class DB_Connector:
    def __init__(self):
        self.dbAuth = confuse.RootView([confuse.YamlSource('config.yaml')])['database'].get()
        self.dialect = self.dbAuth['dialect']
        self.driver = self.dbAuth['driver']
        self.username = self.dbAuth['username']
        self.password = self.dbAuth['password']
        self.hostname = self.dbAuth['hostname']
        self.db_name = self.dbAuth['db_name']
        self.dbschema = self.dbAuth['db_schema']
        self.engine = create_engine(f'{self.dialect}+{self.driver}://{self.username}:{self.password}@{self.hostname}/{self.db_name}')

    def get_data(self, table, index_col):
        return pd.read_sql_table(con=self.engine, table_name=table, index_col=index_col)

    def get_geodata(self, sql, geom_col):
        return gpd.GeoDataFrame.from_postgis(con=self.engine, sql=sql, geom_col=geom_col)