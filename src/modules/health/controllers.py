class ControllerHealth:
    @staticmethod
    def health_check():
        return {
            "message":"Estoy vivito :p ",
            "ok": True,
        }