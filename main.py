from sqlalchemy import create_engine, Column, Integer, String, DateTime, URL, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc as pyodbc
import datetime
import os
import urllib


connection_url = URL.create(
    "mssql+pyodbc",
    username="LAPTOP-1C40NA38",
    password="",
    host="localhost",
    port=1433,
    database="master",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
    },
)
# engine = create_engine(connection_url)
engine = create_engine("mssql+pyodbc://LAPTOP-1C40NA38@localhost/master?"
                       "driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"
                       "&authentication=ActiveDirectoryIntegrated")

# Establishing a connection
connection = engine.connect()

# You can use the connection to execute queries or create a MetaData object for further use
metadata = MetaData()
metadata.reflect(bind=engine)

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# Step 4: Create the database tables
Base.metadata.create_all(engine)

# Step 5: Insert data into the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Inserting a new user into the database
new_user = User(username='Sandy', email='sandy@gmail.com')
session.add(new_user)
session.commit()
