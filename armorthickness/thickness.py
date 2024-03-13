import math


# LEAT: LOS (Line of sight) Effective Armor Thickness
class Leat:
    def __init__(self, base_at, angle) -> None:
        self.base_at = base_at
        self.angle = angle

    def calculate(self) -> float:
        return abs(self.base_at / math.cos(math.radians(self.angle)))

    def main(self) -> None:
        while True:
            try:
                self.angle = float(input("Delta degrees compared to zero: "))
                self.base_at = float(input("Base armor thickness (mm): "))
                print("Effective armor thickness:", self.calculate(), "mm")
                break
            except ValueError:
                print("\nError: Please enter valid values.")
            except ZeroDivisionError:
                print("\nError: Division by zero! Please enter valid values.")
            except KeyboardInterrupt:
                print("\n\nInterrupted by user, quitting gracefully...\n")
                break


if __name__ == "__main__":
    instance_thickness = Leat(base_at=0, angle=0)
    instance_thickness.main()