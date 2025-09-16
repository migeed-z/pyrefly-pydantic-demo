from pydantic import BaseModel, ConfigDict, Field


# we can use aliases like so:
class Model(BaseModel):
    x: int = Field(alias="y")


m = Model(y=0)
m = Model(x=0)  # not allowed to initialize the model with field name


# validate by name is turned off by default but we can enable it like so:
class Model(BaseModel, validate_by_name=True, validate_by_alias=True):
    x: int = Field(alias="y")


Model(x=0)
Model(y=0)


# we can also specify alias behavior via a config dict like so
class Model(BaseModel):
    x: str = Field(..., alias="y")
    model_config = ConfigDict(validate_by_name=True)


Model(y="123")
Model(x="123")
