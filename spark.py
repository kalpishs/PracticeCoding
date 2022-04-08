from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import types
import sys, logging
from datetime import datetime
from pyspark.sql.types import StructType,StructField, StringType,LongType, IntegerType

from pyspark.sql import types as t
from pyspark.sql import functions as F
# Logging configuration
formatter = logging.Formatter('[%(asctime)s] %(levelname)s @ line %(lineno)d: %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# current time variable to be used for logging purpose
dt_string = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
# change it to your app name
AppName = "SparkDummyApp"

def main():
    # start spark code
    spark = SparkSession.builder.appName(AppName + "_" + str(dt_string)).getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    logger.info("Starting spark application")

   # if len(sys.argv) < 2:
   #     logger.error("Please give file path as argumnet. For ex: file:///abc/ded/a.parquet")
   #     sys.exit()

    data2 = [("test1", "test2"),
         ("Michael", "Rose"),
         ("Robert", "Williams")]

    schema = StructType([
    StructField("firstname", StringType(), True),
    StructField("lastename", StringType(), True)])

    data3=[(1,"co-branded",1471824008,'zoom'),
           (2,"xyz",1471824008,'zoom'),
           (2,"co-brand",1645032272,'zoom'),
           (1,"xyz", 1642364397,'hey'),
           (2,"co-brand", 1639685997,'byy'),
           (2,"co-brand",1637093997,'zoom'),
           (1,"abc",1637007597,'hey')
           ]
    schema1 = StructType([
        StructField("user_id", IntegerType(), True),
        StructField("action", StringType(), True),
        StructField("timestamp", LongType(), True),
        StructField("instance", StringType(), True)
    ])
    adf = spark.createDataFrame(data=data3, schema=schema1)
    adf.printSchema()
    filter_df=adf.withColumn('tempdate', F.to_date(adf.timestamp.cast(dataType=types.TimestampType()))).filter(col("tempdate") >= F.add_months(F.current_date(), -3))
    filter_df.where(col('action').isin("co-brand")).withColumn('timestamp', F.date_format(filter_df.tempdate.cast(dataType=t.TimestampType()), "yyyy-MM")).drop("tempdate").groupBy(col('timestamp'),col('instance')).agg(F.count("user_id").alias("count")).orderBy('timestamp').show()
    #adf.withColumn("date_time", from_utc_timestamp(col("timestamp").cast('timestamp'),"EET")).show()
    df = spark.createDataFrame(data=data2, schema=schema)
    logger.info("Previewing Data schema")
    df.printSchema()
    count = df.count()
    logger.info("File count:{0}".format(str(count)))
    df.show(10, False)

    #df.where('action IN ("co-branded")').withColumn('timestamp',
    #                                            date_format(df.timestamp.cast(dataType=t.TimestampType()),
    #                                                             "yyyy-MM")).groupBy('timestamp', 'instance').agg(
    #    count("user_id").alias("count")).orderBy('timestamp').display()

    logger.info("Ending spark application")
    # end spark code
    spark.stop()
    return None

# Starting point for PySpark
if __name__ == '__main__':
    main()
    sys.exit()
