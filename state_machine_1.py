class Teleop:
    def __init__(self, direction, speed):
        self.direction = direction
        self.speed = speed

    def acc(self, amt):
        self.speed += amt
        return self.speed

    def turn(self, degree):
        self.direction += degree
        return self.direction

    def get_dir(self):
        print(self.direction, ' degrees')

    def get_speed(self):
        print(self.speed, ' m/s')

    #if State == Auto:
        #type in auto code here

    #if State == Arm:
        #type the arm code here

class Auto:
    pass
    #TODO Auto code

class Arm:
    pass
    #TODO Arm code


drive_1 = Teleop(0,120)

drive_1.get_dir()

drive_1.get_speed()

drive_1.turn(15)

drive_1.acc(-10)

drive_1.get_dir()

drive_1.get_speed()
