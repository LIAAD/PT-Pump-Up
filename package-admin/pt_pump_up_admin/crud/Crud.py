from abc import ABC, abstractmethod
import requests

# Crud follows the Resource Controller pattern of Laravel
# https://laravel.com/docs/master/controllers#resource-controllers
class Crud(ABC):
    def __init__(self, pt_pump_up, route) -> None:
        self.pt_pump_up = pt_pump_up
        self.route = route
    
    @abstractmethod
    def insert(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, **kwargs):
        raise NotImplementedError
    

    def send_get_request(self, params, query_string):
        raise NotImplementedError

    def send_post_request(self, data):
        
        response = requests.post(
            self.pt_pump_up.url + self.route,
            data=data, 
            headers={"Authorization": "Bearer " + self.pt_pump_up.pt_pump_up_token}
        )
        
        return response.json()
    
    def send_delete_request(self, params):
            
        response = requests.delete(
            self.pt_pump_up.url + self.route,
            params=params,
            headers={"Authorization": "Bearer " + self.pt_pump_up.pt_pump_up_token}
        )

        return response.json()
    
    def send_put_request(self, data):
        raise NotImplementedError