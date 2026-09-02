import database


USER_CHOICE = """
Enter:

- 'a' to add a new mobile
- 'l' to list all mobiles
- 's' to search for a mobile
- 'd' to delete a mobile
- 'p' to update mobile price
- 'q' to quit

Your choice: """


# Add Mobile
def prompt_add_mobile():

    name = input("Enter mobile name: ")
    brand = input("Enter mobile brand: ")
    model = input("Enter mobile model: ")
    storage = input("Enter mobile storage: ")
    ram = input("Enter mobile RAM: ")
    price = float(input("Enter mobile price: "))

    database.insert_mobile(
        name,
        brand,
        model,
        storage,
        ram,
        price
    )


# List Mobiles
def list_mobiles():

    mobiles = database.get_all_mobiles()

    for mobile in mobiles:

        print(
            f"{mobile['name']} by {mobile['brand']} "
            f"| Model: {mobile['model']} "
            f"| Storage: {mobile['storage']} "
            f"| RAM: {mobile['ram']} "
            f"| Price: ${mobile['price']}"
        )


# Search Mobile
def prompt_search_mobile():

    name = input("Enter mobile name: ")

    mobile = database.search_mobile(name)

    if mobile:

        print("\nMobile Found!")

        print(f"Name    : {mobile['name']}")
        print(f"Brand   : {mobile['brand']}")
        print(f"Model   : {mobile['model']}")
        print(f"Storage : {mobile['storage']}")
        print(f"RAM     : {mobile['ram']}")
        print(f"Price   : ${mobile['price']}")

    else:

        print("Mobile not found!")


# Delete Mobile
def prompt_delete_mobile():

    name = input("Enter the mobile name to delete: ")

    database.delete_mobile(name)


# Update Price
def prompt_update_price():

    name = input("Enter mobile name: ")

    new_price = float(input("Enter new price: "))

    database.update_price(name, new_price)


def menu():

    user_input = input(USER_CHOICE)

    while user_input != "q":

        if user_input == "a":

            prompt_add_mobile()

        elif user_input == "l":

            list_mobiles()

        elif user_input == "s":

            prompt_search_mobile()

        elif user_input == "d":

            prompt_delete_mobile()

        elif user_input == "p":

            prompt_update_price()

        else:

            print("Invalid choice!")

        user_input = input(USER_CHOICE)


menu()