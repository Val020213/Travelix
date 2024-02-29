from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os


# Load the environment variables from .env file
load_dotenv()

# Get the password from the environment variable, or use the default value "postgres"
password = os.getenv("PASSWORD", "postgres")

DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/travelixdb"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
