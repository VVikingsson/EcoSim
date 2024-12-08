from Weather import Weather

class Environment:
    def __init__(self):
        self.flora = {}
        self.fauna = {}
        self.temperature = 15
        self.time = 0
        self.weather = Weather()