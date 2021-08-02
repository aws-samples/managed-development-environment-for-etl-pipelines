# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

class transformation_code():
    
    def __init__(self):
        self.sc = SparkContext.getOrCreate()
        self.glueContext = GlueContext(self.sc)
        self.spark = SparkSession(self.sc)
    
    def main(self):
        mylist = [
            {"col1":1,"col2":"x"},
            {"col1":2,"col2":"y"},
            {"col1":3,"col2":"z"},
            {"col1":2,"col2":"x"},
            {"col1":4,"col2":"z"}
        ]
        df = self.spark.createDataFrame(mylist)
        df.show()
        glue_DyF = DynamicFrame.fromDF(df, self.glueContext, "glue_DyF")
        glue_DyF.toDF().show()
        
if __name__ == "__main__":
    transformation_code_obj = transformation_code()
    transformation_code_obj.main()