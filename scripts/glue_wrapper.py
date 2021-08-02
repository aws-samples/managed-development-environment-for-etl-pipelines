# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

class glue_wrapper:
    
    def __init__(self):
        from awsglue.context import GlueContext
        from pyspark.context import SparkContext
        self.glueContext = GlueContext(SparkContext.getOrCreate())
        from transformation_code import transformation_code
        self.transformation_code_obj = transformation_code()
    
    def execute(self):
        self.transformation_code_obj.main()
    
if __name__=="__main__":
    glue_wrapper_obj=glue_wrapper()
    glue_wrapper_obj.execute()