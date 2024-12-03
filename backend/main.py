"""backend main script."""

from datas import RegistarData
from fastapi import FastAPI
from func import (
    calc_total,
    delete_data,
    get_all_data,
    get_task_data,
    get_today_data,
    registar_data,
)

app = FastAPI()


@app.get("/work")
def get_today_data_api():
    """Get today data.

    Returns:
        json: _description_

    """
    return get_today_data()


@app.get("/task")
def get_task():
    """_summary_."""
    return get_task_data()


@app.get("/work/all")
def get_all_data_api():
    """Get today data.

    Returns:
        json: _description_

    """
    return get_all_data()


@app.post("/work")
def registar_data_api(data: RegistarData):
    """Registar function.

    Args:
        data (RegistarData): _description_

    Returns:
        json: _description_

    """
    return registar_data(data=data)


@app.get("/work/{target_month}")
def get_total_data_api(target_month):
    return calc_total(target_month)


@app.delete("/work/{id}")
def delete_data_api(id):
    """Delete data.

    Args:
        id (_type_): _description_

    """
    return delete_data(delet_id=id)
