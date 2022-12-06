import os
from sqlalchemy import create_engine
import pandas as pd

from dotenv import load_dotenv
load_dotenv('.env')

data = pd.read_csv('product.seed.csv')
    
os.chdir("./api")
conn = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI')).raw_connection()
cursor = conn.cursor()

tpls = [tuple(x[1:]) for x in data.to_numpy()]
sql = 'INSERT INTO product (name,x,y,a_line,denim,dots,faux,faux_leather,Floral,knit,Lacy,leather,maxi,midi,mini,pencil,Pleated,Printed,skater,Stripes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
cursor.executemany(sql, tpls)
conn.commit()