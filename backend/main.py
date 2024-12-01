"""backend main script."""

from datas import RegistarData
from fastapi import FastAPI
from func import delete_data, get_data, registar_data

app = FastAPI()


@app.get("/")
def get_data_api():
    """Get today data.

    Returns:
        json: _description_

    """
    return get_data()


@app.post("/")
def registar_data_api(data: RegistarData):
    """Registar function.

    Args:
        data (RegistarData): _description_

    Returns:
        json: _description_

    """
    return registar_data(data=data)


@app.delete("/{id}")
def delete_data_api(id):
    """Delete data.

    Args:
        id (_type_): _description_

    """
    return delete_data(id=id)
