import random

MAX_LINES = 3

MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {"   Apple   ": 90,
                "   Apricot ": 80,
                "   Banana  ": 70,
                "   Grapes  ": 60,
                " Watermelon": 50,
                "   Pear    ": 40,
                "   Orange  ": 30,
                " Strawberry": 20,
                "   cherry  ": 10,
                "   Lemon   ": 100,
                "     7     ": 5}

symbol_value = {"   Apple   ": 1,
                "   Apricot ": 2,
                "   Banana  ": 3,
                "   Grapes  ": 4,
                " Watermelon": 5,
                "   Pear    ": 6,
                "   Orange  ": 7,
                " Strawberry": 8,
                "   cherry  ": 9,
                "   Lemon   ": -1,
                "     7     ": 10}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("Enter the deposit value of amount?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please Enter a value higher than zero")
        else:
            print("Please Enter enter a amount:")
    return amount


def get_lines():
    while True:
        lines = input(f"Enter a value b/w (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please Enter a proper value")
        else:
            print("Please Enter a number")
    return lines


def get_bet():
    while True:
        amount = input("How much you want to bet on each line?: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please Enter a value b/w ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please Enter a amount")
    return amount


def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You are broke. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines and the total amount is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    remaining = winnings - total_bet
    return remaining


def main():
    balance = deposit()
    while balance != 0:
        print(f"Your current balance is ${balance}")
        spins = input("Press (Enter) to spin or (q) to quit: ")
        if spins == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


main()

while True:
    play_again = input("Would you like to test your LUCK again ?? (y/n) : ").lower()
    if play_again == "y":
        main()
    else:
        exit()
