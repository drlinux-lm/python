class ROI:
    def __init__(self, invest, value) -> None:
        self.invest = invest
        self.value = value

    def __str__(self) -> str:
        profit = self.value - self.invest
        roi = (profit / self.invest) * 100
        return f"ROI: {roi}%"
    
def main():
    _inv = float(input("Your investment in $ USD: "))
    _val = float(input("Current market price in $ USD: "))
    _roi = ROI(_inv,_val)
    print(_roi)

if __name__ == "__main__":
    main()