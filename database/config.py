from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
DB_DATABASE = os.environ.get("DB_DATABASE")

db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
Base = declarative_base()
