from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # operators params (with defaults) here
                 redshift_conn_id,
                 sql_tests=[],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Mapping params here
        self.redshift_conn_id = redshift_conn_id
        self.sql_tests = sql_tests

    def execute(self, context):
        self.log.info('DataQualityOperator not implemented yet')
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        error_count = 0
        failing_tests = []
        for test in self.sql_tests:
            records = redshift.get_records(test['sql'])
            if records[0][0] != test['expected_result']:
                error_count+=1
                failing_tests.append(test['sql'])
        if error_count > 0:
            self.log.info('Tests failed')
            self.log.info(failing_tests)
            raise ValueError('Data quality check failed')
        else:
            self.log.info("All data quality checks passed")