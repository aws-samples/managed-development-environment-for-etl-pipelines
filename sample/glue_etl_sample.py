# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
glueContext = GlueContext(SparkContext.getOrCreate())
mylist = [
    {"col1":1,"col2":"x"},
    {"col1":2,"col2":"y"},
    {"col1":3,"col2":"z"},
    {"col1":2,"col2":"x"},
    {"col1":4,"col2":"z"}
]
df = spark.createDataFrame(mylist)
df.show()
glue_DyF = DynamicFrame.fromDF(df, glueContext, "glue_DyF")
glue_DyF.toDF().show()
# Read data from a glue catalog table
sample_DyF = glueContext.create_dynamic_frame.from_catalog(database="sampledb", table_name="sample_table")
sample_DyF.toDF().show()