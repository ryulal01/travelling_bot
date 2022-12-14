from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///user_travel.db')
Session = sessionmaker(autoflush=False, bind=engine)
session = Session()