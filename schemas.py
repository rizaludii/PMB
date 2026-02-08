from pydantic import BaseModel, EmailStr, Field

class CalonMahasiswaCreate(BaseModel):
    nama: str
    email: EmailStr
    phone: str = Field(pattern=r"^08[0-9]{8,11}$")
    prodi: str

class CalonMahasiswaResponse(BaseModel):
    id: int
    nama: str
    email: EmailStr
    phone: str
    prodi: str
    status: str
    nim: str | None

    model_config = {"from_attributes": True}
