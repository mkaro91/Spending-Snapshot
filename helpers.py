def get_amount():
    while True:
        try:
            amount = float(input("\nEnter amount: $"))
            if amount > 0: return amount
            print("Amount spent must be greater than zero.")
        except ValueError:
            print("Please enter a valid amount.")

def get_category():
    while True:
        category = input("Enter purchase category: ").strip()
        if category: return category
        print("Category cannot be blank.")

def get_note():
    return input("Enter purchase note (Leave blank to skip): ")

def press_enter_to_continue():
    input("\nPress <ENTER> to continue...")