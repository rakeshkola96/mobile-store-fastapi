from fastapi import FastAPI
import database


app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Mobile Store Management API"
    }


@app.get("/mobiles")
def get_mobiles():

    return database.get_all_mobiles()


@app.get("/mobiles/{name}")
def search_mobile(name: str):

    mobile = database.search_mobile(name)

    if mobile:

        return mobile

    return {
        "message": "Mobile not found!"
    }


@app.post("/mobiles")
def add_mobile(
    name: str,
    brand: str,
    model: str,
    storage: str,
    ram: str,
    price: float
):

    database.insert_mobile(
        name,
        brand,
        model,
        storage,
        ram,
        price
    )

    return {
        "message": "Mobile added successfully!"
    }


@app.delete("/mobiles/{name}")
def delete_mobile(name: str):

    result = database.delete_mobile(name)

    if result:

        return {
            "message": "Mobile deleted successfully!"
        }

    return {
        "message": "Mobile not found!"
    }


@app.put("/mobiles/{name}/price")
def update_price(
    name: str,
    new_price: float
):

    result = database.update_price(
        name,
        new_price
    )

    if result:

        return {
            "message": "Price updated successfully!"
        }

    return {
        "message": "Mobile not found!"
    }