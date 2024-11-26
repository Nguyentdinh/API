from sqlalchemy import Column, Integer, String
from app.database import Base

# Định nghĩa mô hình User để ánh xạ với bảng 'users' trong PostgreSQL
class User(Base):
    __tablename__ = "users"  # Tên bảng trong cơ sở dữ liệu

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
