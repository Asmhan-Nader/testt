class Vehicle:
    def __init__(self):
        self._speed=0
        self._has_wheels= False
        self._wheels_num=0
    def speed_up(self):
        self._speed+=5
    def speed_down(self):
        if self._speed == 0:
            print("the vihcle is stopped")
        elif self._speed <5 and self._speed!= 0:
            self._speed=0
        self._speed-=5
    def stop(self):

        self._speed=0


class Car (Vehicle):
      def __init__(self):
          super().__init__()
          self._has_wheels= True
          self._wheels_num=4

      def speed_up(self):
        self._speed += 10




class ship(Vehicle)  :
    def speed_up(self):
        self._speed += 20 