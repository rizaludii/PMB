from sqlalchemy.orm import Session
import models, schemas
from nim_generator import generate_nim

def create_pendaftaran(db: Session, data: schemas.CalonMahasiswaCreate):
    calon = models.CalonMahasiswa(
        nama=data.nama,
        email=data.email,
        phone=data.phone,
        prodi=data.prodi,
        status="PENDING"
    )
    db.add(calon)
    db.commit()
    db.refresh(calon)
    return calon

def approve_pendaftaran(db: Session, calon_id: int):
    calon = db.query(models.CalonMahasiswa).filter(models.CalonMahasiswa.id == calon_id).first()
    if not calon:
        return None
    if calon.status == "APPROVED":
        return calon
    calon.status = "APPROVED"
    calon.nim = generate_nim(calon.prodi)
    db.commit()
    db.refresh(calon)
    return calon

def get_status(db: Session, calon_id: int):
    return db.query(models.CalonMahasiswa).filter(models.CalonMahasiswa.id == calon_id).first()

def list_pendaftar(db: Session):
    return db.query(models.CalonMahasiswa).all()
