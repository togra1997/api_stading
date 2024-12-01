from func import registar_data
from datas import RegistarData
from fastapi import FastAPI


app = FastAPI()


@app.post("/")
def registar_data_api(data: RegistarData):
    """Registar function.

    Args:
        data (RegistarData): _description_

    Returns:
        json: _description_

    """

    return registar_data(data=data)
    
