"""front 2 back data preset."""

from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class RegistarData(BaseModel):
    """front to backend.

    Args:
        BaseModel (_type_): _description_

    """

    start_time: str
    end_time: str
    annkenn: str
    work: str
    kousuutukesaki: str
