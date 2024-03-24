import traceback
from requests import Request
from pt_pump_up_admin import PTPumpAdminFactory
from pt_pump_up_orms import HTTPException, ORM


class CRUD:

    client = PTPumpAdminFactory.create()

    @staticmethod
    def index(orm: ORM):
        try:
            response = CRUD.client.submit(
                Request(method="GET", url=orm.route))
        except HTTPException as e:
            traceback.print_exc()
            response = e.response
        finally:
            return response

    @staticmethod
    def store(orm: ORM):
        try:
            response = CRUD.client.submit(
                Request(method="POST", url=orm.route, json=orm.serialize()))

            orm.deserialize(response)
        except HTTPException as e:
            traceback.print_exc()
            response = e.response
            orm.id = None
        finally:
            return response

    @staticmethod
    def show(orm: ORM):
        try:
            response = CRUD.client.submit(
                Request(method="GET", url=f"{orm.route}/{orm.id}"))
            orm.deserialize(response)
        except HTTPException as e:
            traceback.print_exc()
            response = e.response
            orm.json = dict()
        finally:
            return response

    @staticmethod
    def update(orm: ORM):
        try:
            response = CRUD.client.submit(
                Request(method="PUT", url=f"{orm.route}/{orm.id}", json=orm.json))

            orm.deserialize(response)
        except HTTPException as e:
            traceback.print_exc()
            response = e.response
        finally:
            return response

    @staticmethod
    def destroy(orm: ORM):
        try:
            response = CRUD.client.submit(
                Request(method="DELETE", url=f"{orm.route}/{orm.id}"))
            orm.id = None

        except HTTPException as e:
            response = e.response
            traceback.print_exc()
        finally:
            return response
