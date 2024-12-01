"""front 2 back data preset."""

from dataclasses import dataclass

from pydantic import BaseModel


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
