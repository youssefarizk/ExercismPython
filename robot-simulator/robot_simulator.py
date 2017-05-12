NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot(object):
    
    def __init__(self, direction = NORTH, x = 0, y = 0):
        self.bearing = direction
        self.coordinates = (x,y)

    def turn_left(self):
        leftDic = {
            NORTH: WEST,
            WEST: SOUTH,
            SOUTH: EAST,
            EAST: NORTH
        }
        self.bearing = leftDic[self.bearing]

    def turn_right(self):
        rightDic = {
            NORTH: EAST,
            WEST: NORTH,
            SOUTH: WEST,
            EAST: SOUTH
        }
        self.bearing = rightDic[self.bearing]    

    def advance(self):
        adDic = {
            NORTH: (self.coordinates[0],self.coordinates[1] + 1),
            WEST: (self.coordinates[0] - 1,self.coordinates[1]),
            SOUTH: (self.coordinates[0],self.coordinates[1] - 1),
            EAST: (self.coordinates[0] + 1,self.coordinates[1])
        }
        self.coordinates = adDic[self.bearing]

    def simulate(self, cmnd):
        cmndDic = {
            'A': self.advance,
            'L': self.turn_left,
            'R': self.turn_right
        }
        for char in cmnd: cmndDic[char]()

