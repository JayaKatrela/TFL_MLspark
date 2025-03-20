import unittest
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.sql.functions import col

class TFLForecastTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .appName("TestTFLForecast") \
            .master("local[*]") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_data_cleaning(self):
        data = [
            ('2024-03-15 10:00:00', 'Victoria', 'Good Service'),
            ('2024-03-15 12:00:00', 'Central', 'Minor Delays'),
            ('2024-03-15 14:00:00', 'Jubilee', None)
        ]
        schema = ['timedetails', 'line', 'status']
        df = self.spark.createDataFrame(data, schema=schema)

        df = df.fillna({'status': 'Unknown'})
        self.assertEqual(df.filter(df.status == 'Unknown').count(), 1)

    def test_string_indexer(self):
        data = [('Victoria',), ('Central',), ('Jubilee',)]
        schema = ['line']
        df = self.spark.createDataFrame(data, schema=schema)

        indexer = StringIndexer(inputCol='line', outputCol='line_index')
        model = indexer.fit(df)
        transformed_df = model.transform(df)

        self.assertTrue('line_index' in transformed_df.columns)

if __name__ == '__main__':
    unittest.main()
