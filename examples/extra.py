from pydantic import BaseModel


# We can pass extra fields to our model by default
class ModelAllow(BaseModel):
    x: int


ModelAllow(x=1, y=2)


# we can also forbid extra fields
class ModelForbid(BaseModel, extra="forbid"):
    x: int


ModelForbid(x=1, y=2)
