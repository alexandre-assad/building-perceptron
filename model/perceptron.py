
from dataclasses import dataclass
from typing import Iterable

def activation(matrix: Iterable[float]) -> int: ...

@dataclass
class Perceptron:
    entries : Iterable[float]
    wieghts:  Iterable[float]
    bias : float 


    @property
    def output(self) -> int :
        return activation(self.entries)