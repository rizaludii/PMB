from sqlalchemy import Column, Integer, String
from database import Base

class CalonMahasiswa(Base):
    __tablename__ = "calon_mahasiswa"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    prodi = Column(String, nullable=False)
    status = Column(String, default="PENDING")
    nim = Column(String, nullable=True)
