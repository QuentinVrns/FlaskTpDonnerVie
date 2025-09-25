from typing import List, Optional
from models import Supplier

class SupplierService:
    def __init__(self) -> None:
        self._suppliers: List[Supplier] = []
        self._next_id = 1
        self.create(Supplier(name="Fournisseur A", address="123 Rue de Paris, 75000 Paris",
                             email="fournisseurA@example.com", phone="01 23 45 67 89"))
        self.create(Supplier(name="Fournisseur B", address="456 Boulevard de Lyon, 69000 Lyon",
                             email="fournisseurB@example.com", phone="04 56 78 90 12"))
        self.create(Supplier(name="Fournisseur C", address="789 Avenue de Marseille, 13000 Marseille",
                             email="fournisseurC@example.com", phone="09 87 65 43 21"))
        self.create(Supplier(name="Fournisseur D", address="321 Place de Nice, 06000 Nice",
                             email="fournisseurD@example.com", phone="06 78 56 34 12"))

    def list(self) -> List[Supplier]:
        return list(self._suppliers)

    def get(self, supplier_id: int) -> Optional[Supplier]:
        return next((s for s in self._suppliers if s.id == supplier_id), None)

    def create(self, supplier: Supplier) -> Supplier:
        supplier.id = self._next_id
        self._next_id += 1
        self._suppliers.append(supplier)
        return supplier

    def update(self, supplier_id: int, data: Supplier) -> Optional[Supplier]:
        s = self.get(supplier_id)
        if not s:
            return None
        s.name = data.name
        s.address = data.address
        s.email = data.email
        s.phone = data.phone
        return s

