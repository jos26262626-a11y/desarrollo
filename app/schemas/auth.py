from pydantic import BaseModel, EmailStr, Field

# Esquema para el registro de usuario
class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6)

# ✅ Esquema para login (este era el que te faltaba)
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)

# Esquema de respuesta para el usuario
class UserResponse(BaseModel):
    id: int = Field(..., alias="ID_Usuario")
    username: str = Field(..., alias="Nombre")
    email: EmailStr = Field(..., alias="Correo")

    class Config:
        from_attributes = True
        populate_by_name = True
