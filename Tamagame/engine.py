import main, rng, printer


def engine(tamago,bet):
    lom = rng.rng(0, 1)
    if tamago == 1:
        num = rng.rng(2, 9)
        printer.printer(num)
    elif tamago == 9:
        num = rng.rng(1, 8)
        printer.printer(num)
    else:
        if lom == 0:
            num = rng.rng(1, tamago - 1)
            printer.printer(num)
        else:
            num = rng.rng(tamago + 1, 9)
            printer.printer(num)

    if (tamago < num and bet == "g") or (tamago > num and bet == "l"):
        print("\nYou've won this round.")
        return True
    else:
        print("\nYou've lost this round.")
        return False