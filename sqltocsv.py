from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv, dotenv_values

def export():
    load_dotenv()
    SERVER = os.getenv("SERVER")
    DATABASE = os.getenv("DATABASE")
    DRIVER = 'SQL SERVER'
    USERNAME = os.getenv("USERNAME")    #not used
    PASSWORD = ''                           #not used
    DATABASE_CONNECTION = f'mssql://@{SERVER}/{DATABASE}?driver={DRIVER}'

    engine = create_engine(DATABASE_CONNECTION)
    connection = engine.connect()

    file_name = input("Enter your filename:")
    query = input("Enter your query:")
    data = data = pd.read_sql_query(query, connection)
    with open(file_name, 'w') as file:
        data.to_csv(f"D:/Téléchargements/{file_name}.csv",index=False,header=True)

export()