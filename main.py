def pay(names, transaction_record, number):
    person_name = input("Enter the name of the person paying the bill: ")
    while person_name not in names:
        print("Please enter a valid name😡😡😡")
        person_name = input("Enter the name of the person paying the bill: ")

    amount = input(f"Enter the amount paid by {person_name}: ")
    while amount.isalpha() or float(amount) < 1:
        print("Please enter a valid amount😡😡😡")
        amount = input(f"Enter the amount paid by {person_name}: ")
    amount = float(amount)

    for name in names:
        if name != person_name:
            if f"{person_name}->{name}" not in transaction_record:
                transaction_record[person_name + "->" + name] = 0
            if f"{name}->{person_name}" not in transaction_record:
                transaction_record[name + "->" + person_name] = amount // number
            elif f"{name}->{person_name}" in transaction_record:
                transaction_record[name + "->" + person_name] += amount // number


def instructions():
    print("Here are the instructions on how to use this particular program")
    print("Type 'Pay' to indicate that Person 1 is paying the bill for everyone.")
    print("Type 'Owe' to know how much Person 1 owes Person 2")
    print(
        "Type 'Payback' to indicate that Person 1 is paying back Person 2. In this feature, you can either pay the full amount or a partial amount. So, type 'Full' for full payment and 'Partial' for partial payment.")
    print("Type 'Quit' to indicate that there were no transactions made further.")


def main():
    print("Welcome to the Splitwise Program")
    number = int(input("Please enter the no. of people involved: "))

    names = []
    for name in range(number):
        names.append(input(f"Please enter the name of friend no.{name + 1}: "))
    print("Ok. Good to see that you have many friends😊😊😊")
    instructions()

    transaction_record = {}
    flag = True
    while ("True"):
        action = input("Enter the keyword: ").lower()

        match action:
            case "pay":
                pay()

            case "owe":
                owe()

            case "payback":
                payback()

            case "quit":
                flag = False

            case _:
                print("Please enter a valid keyword")
                continue

        if flag == False:
            break


if __name__ == "__main__":
    main()