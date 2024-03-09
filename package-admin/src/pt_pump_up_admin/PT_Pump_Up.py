class PT_Pump_Up:
    def __init__(self, bearer_token, url="https://pt-pump-up.inesctec.pt") -> None:
        self.bearer_token = bearer_token
        self.url = url
