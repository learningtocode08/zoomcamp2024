#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
import sqlalchemy
from sqlalchemy import create_engine
from time import time
import argparse

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_name = 'output.csv.gz'

    os.system(f"wget {url} -O {csv_name}")
    
    color = ''

    if 'green' in url:
        color = 'green'
    else:
        color = 'yellow'
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    # engine.connect()
    print('Engine Created')

    df_iter = pd.read_csv(csv_name,iterator = True,chunksize=100000)
    print('DF Iterator Created')
    
    df = next(df_iter)
    print('DF Iterator Next')
    
    if color == 'yellow':
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    elif color == 'green':
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    
    print('Datetime Conversions')
    df.head(n=0).to_sql(name=table_name,con=engine,if_exists='replace')
    df.to_sql(name=table_name,con=engine,if_exists='append')

    print('Start of While Loop')
    while True:
        t_start = time()
        df = next(df_iter)
        
        if color == 'yellow':
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        elif color == 'green':
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

        df.to_sql(name=table_name,con=engine,if_exists='append')
        
        t_end = time()
        print('inserted another chunk..., took %.3f second' % (t_end - t_start))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    # user, password, host, port ,database name, table name,
    # url of the csv

    parser.add_argument('--user',help='username for postgres')
    parser.add_argument('--password',help='pass for postgres')
    parser.add_argument('--host',help='host for postgres')
    parser.add_argument('--port',help='port for postgres')
    parser.add_argument('--db',help='db for postgres')
    parser.add_argument('--table_name',help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)


