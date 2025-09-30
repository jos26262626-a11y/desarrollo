from pydantic import BaseModel
from typing import List, Dict

class CatalogoItem(BaseModel):
    id: int
    nombre: str

class CatalogosBootstrapResponse(BaseModel):
    metodos_entrega: List[str]
    condiciones_articulo: List[str] 
    tipos_articulo: List[CatalogoItem]
    estados: Dict[str, List[CatalogoItem]]

# Datos estáticos según la especificación del Jira
CATALOGOS_DATA = {
    "metodos_entrega": ["domicilio", "oficina"],
    "condiciones_articulo": ["nuevo", "seminuevo", "usado", "malo"],
    "tipos_articulo": [
        {"id": 1, "nombre": "Electrónica"},
        {"id": 2, "nombre": "Joyería"}
    ],
    "estados": {
        "solicitud": [
            {"id": 1, "nombre": "pendiente"},
            {"id": 2, "nombre": "evaluada"},
            {"id": 3, "nombre": "rechazada"}
        ],
        "articulo": [
            {"id": 1, "nombre": "pendiente"},
            {"id": 2, "nombre": "evaluado"}
        ],
        "prestamo": [
            {"id": 2, "nombre": "activo"}
        ],
        "pago": [
            {"id": 1, "nombre": "pendiente"},
            {"id": 2, "nombre": "validado"}
        ],
        "inventario": [
            {"id": 1, "nombre": "disponible"},
            {"id": 3, "nombre": "en_venta"}
        ]
    }
}