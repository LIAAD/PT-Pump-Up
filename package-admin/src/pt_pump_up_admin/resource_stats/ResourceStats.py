from pt_pump_up_admin import CRUD


class ResourceStats(CRUD):
    def __init__(self,
                 id: int = None,
                 standard_format: bool = None,
                 off_the_shelf: bool = None,
                 preservation_rating: str = None) -> None:

        preservation_rating = preservation_rating.lower(
        ) if preservation_rating is not None else None

        super().__init__("resource-stats",
                         id=id,
                         standard_format=standard_format,
                         off_the_shelf=off_the_shelf,
                         preservation_rating=preservation_rating)
