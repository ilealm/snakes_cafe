from textwrap import dedent

menu = {
  "Wings":0, 
  "Cookies" : 0,
  "Spring Rolls" : 0,
  "Salmon": 0,
  "Steak": 0,
  "Meat Tornado": 0,
  "A Literal Garden": 0,
  "Ice Cream": 0,
  "Cake": 0,
  "Pie": 0,
  "Coffee": 0,
  "Tea": 0,
  "Unicorn Tears": 0,
}

def display_welcome():
    msg = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
    print(dedent(msg))

def display_menu():
    msg ="""
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """
    print(dedent(msg))
    


def ask_order():
    msg = """
    ***********************************
    ** What would you like to order? **
    ***********************************    
    """
    while True:
        order = input(dedent(msg))

        if order == "quit":
            break
       
        if order in menu:
            menu[order]+=1
            amount = menu[order]
            print(f"** {amount} order of {order} have been added to your meal **")
        else:
            print("That is not in the menu.")



if __name__ == "__main__":
    display_welcome()
    display_menu()
    ask_order()