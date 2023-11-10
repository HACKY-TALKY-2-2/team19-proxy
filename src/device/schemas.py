from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CreateDeviceSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
    )

    device_token: str


class UpdateDevicePositionSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
    )

    longitude: float
    latitude: float
