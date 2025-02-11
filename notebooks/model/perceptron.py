
from dataclasses import dataclass
from random import random
from typing import Any, Iterable

from numpy import array, dot, zeros

class Perceptron:

    def __init__(self,n_features: int, bias: float = random(), learning_rate: float = 0.01, epochs: int = 200):
        self.weights = zeros(n_features)
        self.bias = bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, dataset: Any) -> int: 
        linear_output = dot(dataset, self.weights) + self.bias
        return (linear_output >= 0.5).astype(int)

    def fit(self, dataset, target) -> None: 
        for _ in range(self.epochs):
            for iterated_value, iterated_target in zip(dataset, target):
                prediction = self.predict(iterated_value)
                update = self.learning_rate * (iterated_target - prediction)
                self.weights += update * iterated_value
                self.bias += update
    
