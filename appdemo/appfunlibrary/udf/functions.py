import ctypes
import glob
import hashlib
import re
import requests
import json
from pyspark import SparkContext
from pyspark.sql import SparkSession

def get_dbutils(spark): 
  try: 
    from pyspark.dbutils import DBUtils
    dbutils = DBUtils(spark)
  except ImportError:
    import IPython
    dbutils = IPython.get_ipython().user_ns["dbutils"]
  return dbutils

def get_sum_function_app(spark, dbutils, params, api_url): 
  api_url = api_url
  spark = SparkSession.builder.getOrCreate()
  dbutils = get_dbutils(spark)
  try: 
    response = requests.get(url=api_url, json=params)
    res = response.text
  except requests.exceptions.RequestException as e: 
    raise e
  return res
