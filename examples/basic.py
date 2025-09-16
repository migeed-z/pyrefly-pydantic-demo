from pydantic import BaseModel, Field


# This is a basic model
class User1(BaseModel):
    name: str
    age: int


# Coersion is allowed here, so we will not typecheck this model
x = User1(name="Alice", age=30)

# str is runtime corcible to int.
y = User1(name="Alice", age="30")


# if you want strict typechecking for fields, add the strict keyword to it
# Note: Fails in mypy, pyrefly and runtime
class User2(BaseModel):
    name: str
    age: int = Field(strict=True)


# we will get IDE hints and red squiggles for type errors
z = User2(name="Alice", age="30")
