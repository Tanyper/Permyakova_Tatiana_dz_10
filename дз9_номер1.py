import time
import itertools
class TrafficLight:
    color = [["red",[7,31]],["yellow",[2,33]],["green",[7,32]],["yellow",[2,33]]]
    def runnind(self):
        for light in itertools.cycle(self.color):
            print (f"\r\033[{light[1][1}m\033[1m{light[0]}\033[0m", end="")
            time.sleep (light[1][0])

TrafficLight_one= TrafficLight()
TrafficLight_one.runnind()
#почему-то в visual studio не выводит ничего