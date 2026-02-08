from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistem PMB",
    description="Sistem Penerimaan Mahasiswa Baru Lengkap",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"app": "Sistem PMB", "status": "running", "docs": "/docs"}

@app.post("/api/pmb/register", response_model=schemas.CalonMahasiswaResponse)
def register_pmb(data: schemas.CalonMahasiswaCreate, db: Session = Depends(get_db)):
    return crud.create_pendaftaran(db, data)

@app.put("/api/pmb/approve/{calon_id}", response_model=schemas.CalonMahasiswaResponse)
def approve_pmb(calon_id: int, db: Session = Depends(get_db)):
    calon = crud.approve_pendaftaran(db, calon_id)
    if not calon:
        raise HTTPException(status_code=404, detail="Calon mahasiswa tidak ditemukan")
    return calon

@app.get("/api/pmb/status/{calon_id}", response_model=schemas.CalonMahasiswaResponse)
def cek_status(calon_id: int, db: Session = Depends(get_db)):
    calon = crud.get_status(db, calon_id)
    if not calon:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    return calon

@app.get("/api/pmb/list", response_model=list[schemas.CalonMahasiswaResponse])
def list_all(db: Session = Depends(get_db)):
    return crud.list_pendaftar(db)
