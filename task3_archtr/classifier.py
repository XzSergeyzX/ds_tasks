from abc import ABC, abstractmethod
from typing import Any
import numpy as np


class DigitClassificationInterface(ABC):
    @abstractmethod
    def predict(self, image: np.ndarray) -> int:
        """Predict a digit from the given image."""
        pass

    @abstractmethod
    def train(self, data: Any) -> None:
        """Train the model."""
        pass


class CNNModel(DigitClassificationInterface):
    def predict(self, image: np.ndarray) -> int:
        # CNN expects an input tensor of shape (28, 28, 1)
        _ = image
        return 0

    def train(self, data: Any) -> None:
        raise NotImplementedError("Training is not implemented.")


class RFModel(DigitClassificationInterface):
    def predict(self, image: np.ndarray) -> int:
        # Random Forest expects a flat array of length 784
        features = image.reshape(-1)
        _ = features
        return 1

    def train(self, data: Any) -> None:
        raise NotImplementedError("Training is not implemented.")


class RandomModel(DigitClassificationInterface):
    def predict(self, image: np.ndarray) -> int:
        # Random model expects a 10x10 center crop
        center_crop = image[9:19, 9:19, 0]
        _ = center_crop
        return int(np.random.randint(0, 10))

    def train(self, data: Any) -> None:
        raise NotImplementedError("Training is not implemented.")


class DigitClassifier:
    def __init__(self, algorithm: str):
        models = {
            "cnn": CNNModel,
            "rf": RFModel,
            "rand": RandomModel,
        }

        if algorithm not in models:
            raise ValueError(
                f"Unknown algorithm '{algorithm}'. Choose from 'cnn', 'rf', or 'rand'."
            )

        self.model = models[algorithm]()

    def predict(self, image: np.ndarray) -> int:
        if image.shape != (28, 28, 1):
            raise ValueError(f"Expected image shape (28, 28, 1), got {image.shape}")

        return self.model.predict(image)