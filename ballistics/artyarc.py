import math

class Target:
    def __init__(self, distance, velocity) -> None:
        self.distance = distance
        self.velocity = velocity

    def calculation(self) -> float:
        g = 9.80665
        epsilon = (g * self.distance) / self.velocity**2
        if epsilon >= -1 and epsilon <= 1:
            asin = math.asin(epsilon)
            deg = math.degrees(asin) / 2
            return deg
        
        return "Error" # type: ignore

def main():
    dst = float(input("Target range.......(m): "))
    vel = float(input("Shell velocity...(m/s): "))
    obj = Target(dst, vel)
    print(obj.calculation())

if __name__ == "__main__":
    main()
