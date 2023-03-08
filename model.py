from utils.model_utils import BaseModel

class TestModel(BaseModel):

    def __init__(self, params) -> None:
        self.params = params

    def fit(self, X, y):
        print(self.params)
        print(f"model features are {X}")
        print(f"model labels are {y}") 
    
    def predict(self, X):
        print(f"model prediction is zz")


if __name__ == "__main__":
    params = {"C":1, "n_iters": 10}
    model = TestModel(params=params)
    model.fit(1, 2)
    model.predict(1)