from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = 'postgresql://postgres:postgres@localhost:5432/db_test'
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()