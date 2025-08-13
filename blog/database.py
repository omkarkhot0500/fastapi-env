# Import required modules from SQLAlchemy
from sqlalchemy import create_engine  # For connecting to the database
from sqlalchemy.ext.declarative import declarative_base  # For creating database models (tables)
from sqlalchemy.orm import sessionmaker  # For creating sessions to interact with the database

# --------------------------
# Database Configuration
# --------------------------

# This is the database connection URL.
# 'sqlite:///./blog.db' means:
#   - sqlite: use SQLite database
#   - ///: relative path
#   - ./blog.db: store the database file in the current folder with the name 'blog.db'
SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

# Create a database engine.
# `connect_args={"check_same_thread": False}` is needed for SQLite only
# because SQLite has thread-safety limitations.
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class.
# A "session" is used to talk to the database (read/write data).
# autocommit=False → changes are not saved automatically
# autoflush=False → changes are not automatically pushed to the database until committed
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for all our database models (tables).
# We will make classes inherit from this Base to create tables.
Base = declarative_base()

# Dependency function to get a database session for each request.
# This is used inside FastAPI routes to interact with the DB.
def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Provide the session to the route
    finally:
        db.close()  # Close the session after the request is done
