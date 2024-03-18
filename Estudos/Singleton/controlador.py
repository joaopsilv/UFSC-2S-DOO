

class Controller:
    __instance = None
    
    def __init__(self):
        self.list = []

    def __new__(cls):
        if Controller.__instance is None:
            Controller.__instance = object.__new__(cls)
        return Controller.__instance
