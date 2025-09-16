from pydantic import RootModel


# This is a simple RootModel
class A(RootModel[int]):
    pass


A("3")
