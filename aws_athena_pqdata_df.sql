CREATE EXTERNAL TABLE IF NOT EXISTS session09.pqdata (
  `category` string,
  `total_price` int,
  `gender` string,
  `age` int,
  `time` string,
  `state` string,
  `month` string 
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
) LOCATION 's3://fil.aws.training/session09/'
TBLPROPERTIES ('has_encrypted_data'='false');
