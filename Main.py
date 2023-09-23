import random

max_lines=3
max_bet=100
min_bet=1

row=3
col=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}


def check_win(cols,lines,bet,values):
    win=0
    win_lines=[]
    for l in range(lines):
        symbol=cols[0][l]
        for c in cols:
            symbol_to_check=c[l]
            if symbol!=symbol_to_check:
                break
        else:
            win+=values[symbol]*bet
            win_lines.append(l+1)

    return win,win_lines


def get_slot_machine(row,col,sym):
    all_symbols=[]
    for symbol,symbol_count in sym.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    
    cols=[]
    for c in range(col):
        column=[]
        current_symbols=all_symbols[:]
        for r in range(row):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        cols.append(column)
    
    return cols


def print_slot_machine(cols):
    for row in range(len(cols[0])):
        for i,c in enumerate(cols):
            if i!= len(cols)-1:
                print(c[row],end=" | ")
            else:
                print(c[row])



def deposit():
    while True:
        amount=input("How much you are depositing ? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Provide amount greater than 0.")
        else:
            print("Provide a number.")

    return amount


def get_number_of_lines():
    while True:
        lines=input("Provide the number of lines to bet on (1-" +str(max_lines)+ ") ? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=  lines <= max_lines:
                break
            else:
                print("Provide valid number of lines.")
        else:
            print("Provide a number.")

    return lines


def get_bet():
    while True:
        amount=input("How much would you like to bet on each line ? $")
        if amount.isdigit():
            amount=int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f"Amount must be between ${min_bet} - ${max_bet}.")
        else:
            print("Provide a number.")

    return amount


def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"You do not have enough to bet that amount, Your current balance is ${balance}.")
            if balance==0:
                print("Your balance is zero so you can't play anymore.")
                quit()
        else:
            break
    print(f"You are betting ${bet} on ${lines}. Total bet is equal to : ${total_bet}.")

    slots=get_slot_machine(row,col,symbol_count)
    print_slot_machine(slots)
    win,win_lines=check_win(slots,lines,bet,symbol_value)
    if win>0:
        print(f"You won ${win}.")
        print(f"You won on lines :",*win_lines)
    else:
        print("You did not won anything.")

    return win - total_bet


def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}.")
        ans=input("Press enter to play or q to quit : ")
        if ans=="q":
            break
        balance+=spin(balance)
    print(f"You left with ${balance}.")

    
main()
