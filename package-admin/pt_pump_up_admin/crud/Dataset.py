
from pt_pump_up_admin.crud.Crud import Crud

class Dataset(Crud):
    def __init__(self, pt_pump_up) -> None:
        super().__init__(pt_pump_up, "datasets")
    
    def insert(self, **kwargs):
        pass
    
    def delete(self, **kwargs):
        pass
    
    def update(self, **kwargs):
        pass
    
    def get(self, **kwargs):
        pass