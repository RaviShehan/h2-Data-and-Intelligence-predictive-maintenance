from pydantic import BaseModel, Field


class SensorData(BaseModel):
    machine_id: str = Field(..., min_length=1, max_length=50)
    temperature: float = Field(..., ge=0, le=120)
    vibration_x: float = Field(..., ge=0, le=5)
    vibration_y: float = Field(..., ge=0, le=5)
    vibration_z: float = Field(..., ge=0, le=5)
    rpm: int = Field(..., ge=0, le=10000)