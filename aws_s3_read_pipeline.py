from pyspark.sql import SparkSession
import pyspark.sql.functions as func
if __name__ == '__main__':

    spark=SparkSession.builder.appName("aws s3 read and write pipeline").getOrCreate()
    spark._jsc.hadoopConfiguration().set("fs.s3a.access.key","XXXXX")
    spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "XXX")
    spark._jsc.hadoopConfiguration().set("fs.s3n.impl", "org.apache.hadoop.fs.s3n.S3AFileSystem")
    spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.ap-south-1.amazonaws.com")
    sc = spark.sparkContext
    sc.setSystemProperty("com.amazonaws.services.s3.enableV4", "true")
    sc.setLogLevel("ERROR")
    inputDF=spark.read.format("csv").option("Header",True).option("inferSchema",True).csv("s3a://pysparkinp/")
    inputDF.show()
   # inputDF.printSchema()
   # reading landingFileSchema and remove few null records preset in file
    cleanInputDF=inputDF.na.drop()
    # find duplicate records from DataFrame
    id_counts =cleanInputDF.groupby('emp_id').agg(func.count('*').alias('id_cnt')).filter(func.col('id_cnt')>1)
    # create list which contain ids which having emp_id count more than 1
    dups_id=[ i.emp_id for i in id_counts.collect()]
    # data with duplicate ids and write into S3 location path defined
    dup_id_data_df = cleanInputDF.filter(func.col('emp_id').isin(dups_id))
    dup_id_data_df.write.foramt("csv").option('Header',True).save('s3a://pysparkop/output/dup_emp.csv',mode='overwrite')
    # data with non duplicate ids and write into output s3 location
    non_dup_id_df = cleanInputDF.filter(func.col('emp_id').isin(dups_id) == False)
    non_dup_id_df.write.format('csv').option('Header',True).save('s3a://pysparkop/output/non_dup_emp.csv',mode='overwrite')



