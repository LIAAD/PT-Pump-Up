from abc import ABC, abstractmethod
import requests
import json

# Crud follows the Resource Controller pattern of Laravel
# https://laravel.com/docs/master/controllers#resource-controllers


class Crud(ABC):
    def __init__(self, pt_pump_up, route) -> None:
        self.pt_pump_up = pt_pump_up
        self.route = route

    @abstractmethod
    def insert(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, id, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, id, *args, **kwargs):
        pass

    @abstractmethod
    def get(self, id, *args, **kwargs):
        pass

    def send_get_request(self, params, query_string):
        pass

    def send_post_request(self, data):

        response = requests.post(
            url=f"{self.pt_pump_up.url}/{self.route}",
            json=data,
            headers={
                "Authorization": "Bearer " + self.pt_pump_up.bearer_token,             
                "Accept": "application/json"
            }
        )

        return response.json()

    def send_delete_request(self, params):

        response = requests.delete(
            f"{self.pt_pump_up.url}/{self.route}",
            params=params,
            headers={"Authorization": "Bearer " +
                     self.pt_pump_up.pt_pump_up_token}
        )

        return response.json()

    def send_put_request(self, data):
        pass
