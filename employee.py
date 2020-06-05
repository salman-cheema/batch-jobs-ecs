

import boto3
import os
import sqlalchemy as sa
from sqlalchemy import create_engine
import pandas as pd
from connection import postgres_connection
s3 = boto3.resource('s3')

def main():
    df = pd.read_sql_query('select * from employee',con=postgres_connection())
    s3.Bucket(bucket).download_file(key, '/tmp/file')
    # reading csv filess
    df=pd.read_csv('/tmp/file')
    # Insert to table
    df.to_sql("company",con=postgres_connection(),if_exists='append',index=False)

main()
