# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cập nhật URL kết nối với địa chỉ IP của PostgreSQL container
DATABASE_URL = "postgresql://username:password@192.168.1.100:5432/postgres"


# Tạo engine kết nối đến PostgreSQL
engine = create_engine(DATABASE_URL)

# Tạo session để thao tác với cơ sở dữ liệu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base để tạo các lớp mô hình
Base = declarative_base()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
