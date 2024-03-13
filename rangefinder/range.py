import os
import platform


class Ranging:
    def __init__(self, mrads, height):
        self.mrads = mrads
        self.height = height

    def distance(self):
        return (self.height / self.mrads) * 1000

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
        while True:
            try:
                self.height = float(input("Enter object height in meters: "))
                self.mrads = float(input("Enter miliradians: "))
                result = self.distance()
                print("Distance:", result, "meters")
                break
            except ValueError:
                print("\nError: Please enter valid values.")
            except ZeroDivisionError:
                print("\nError: Division by zero! Please enter valid values.")
            except KeyboardInterrupt:
                print("\n\nInterrupted by user, quitting gracefully...\n")
                break


if __name__ == "__main__":
    rangefinder_instance = Ranging(mrads=0, height=0)
    rangefinder_instance.main()
