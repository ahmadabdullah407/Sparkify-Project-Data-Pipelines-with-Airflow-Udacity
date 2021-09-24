from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'
    insert_sql = """INSERT INTO {}
                        {}"""
    @apply_defaults
    def __init__(self,
                 # operators params (with defaults) here
                 redshift_conn_id='',
                 table='',
                 sql='',
                 truncate=False,
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        # Mapping params here
        self.redshift_conn_id=redshift_conn_id
        self.table=table
        self.sql=sql
        self.truncate=truncate
        
    def execute(self, context):
        self.log.info('LoadFactOperator not implemented yet')
        redshift=PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.truncate:
            self.log.info(f"Clearing data from {self.table}")
            redshift.run("TRUNCATE {}".format(self.table))
        self.log.info("Inserting data into destination Redshift table")
        formatted_sql=LoadFactOperator.insert_sql.format(self.table,self.sql)
        redshift.run(formatted_sql)
