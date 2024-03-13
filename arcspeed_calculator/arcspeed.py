import math
import os
import platform

class CircleCalculator():
    def __init__(self):
        self.radius = []
        self.circumferences = []
        self.arcspeeds = []

    def circumference(self, r):
        return 2 * r * math.pi

    def arcspeed(self, a, d):
        return (d / 360) * a

    @staticmethod
    def oscheck():
        os_name = platform.system()
        if os_name == "Windows":
            return "cls"
        elif os_name in ("Linux", "Darwin"):
            return "clear"
        else:
            return "Unknown OS"

    def main(self):
        os_chk = self.oscheck()
        os.system(os_chk)
        try:
            deg = int(input("Input the ˚/s: "))
            os.system(os_chk)
            print(f"Speed is: {deg}˚/s\nFull circle: {360/deg} seconds.\n")
            howmany = int(input("How many ranges? "))
            for i in range(howmany):
                radius = int(input((f"Radius {i + 1} (meters): ")))
                self.radius.append(radius)
                circumference = self.circumference(radius)
                self.circumferences.append(circumference)
                arcspeed = self.arcspeed(circumference, deg)
                self.arcspeeds.append(arcspeed)
        except KeyboardInterrupt:
            os.system(os_chk)
            print("Sigterm by user")

        for i in range(len(self.radius)):
            print(f"\nCircumference: {self.circumferences[i]} m")
            print(f"Arcspeed at {self.radius[i]} m: {self.arcspeeds[i]} m/s")


if __name__ == '__main__':
    calculator = CircleCalculator()
    calculator.main()
