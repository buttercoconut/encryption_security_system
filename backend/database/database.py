"""Database models and session factory."""

from sqlalchemy import Column, Integer, String, LargeBinary, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..core.config import settings

Base = declarative_base()

class Key(Base):
    __tablename__ = "keys"
    id = Column(Integer, primary_key=True, index=True)
    key_id = Column(String, unique=True, index=True, nullable=False)
    key_name = Column(String, nullable=False)
    key_value = Column(String, nullable=False)

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    ciphertext = Column(String, nullable=False)
    key_id = Column(String, nullable=False)

# Create engine and session factory
engine = create_engine(settings.DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
