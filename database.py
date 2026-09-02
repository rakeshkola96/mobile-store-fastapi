mobiles = []


def insert_mobile(name, brand, model, storage, ram, price):

    mobile = {
        "name": name,
        "brand": brand,
        "model": model,
        "storage": storage,
        "ram": ram,
        "price": price
    }

    mobiles.append(mobile)
    print("Mobile added successfully!")


def get_all_mobiles():
    return mobiles


def search_mobile(name):

    for mobile in mobiles:

        if mobile["name"].lower() == name.lower():
            return mobile

    return None


def delete_mobile(name):

    for mobile in mobiles:

        if mobile["name"].lower() == name.lower():

            mobiles.remove(mobile)
            print("Mobile deleted successfully!")

            return

    print("Mobile not found!")


def update_price(name, new_price):

    mobile = search_mobile(name)

    if mobile:
        mobile["price"] = new_price
        print("Price updated successfully!")

    else:
        print("Mobile not found!")