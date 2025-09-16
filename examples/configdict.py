# there are various keywords that can be specified in both, classes and configs.
# ConfigDict groups the options in their own expression, but they are both supported.
# This example tests the frozen property.

from pydantic import BaseModel, ConfigDict


# frozen
class Model(BaseModel):
    model_config = ConfigDict(frozen=True)
    x: int = 42


m = Model()
m.x = 10  # E: Cannot set field `x`
