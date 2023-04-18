class Order():
    """Class defining properties for a order object
    """

    def __init__(self, id, metalId, sizeId, styleId, jewelTypeId, timestamp):
        self.id = id
        self.metalId = metalId
        self.sizeId = sizeId
        self.styleId = styleId
        self.jewelTypeId = jewelTypeId
        self.timestamp = timestamp
