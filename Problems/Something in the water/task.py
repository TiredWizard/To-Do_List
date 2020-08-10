class WaterBody:
    def __init__(self, name, length):
        self.name = name
        self.length = length


class River(WaterBody):
    pass


seine = River("Seine", 777)
