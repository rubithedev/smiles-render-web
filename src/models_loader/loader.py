from collections.abc import Callable, MutableMapping
import logging
from typing import NamedTuple
from numpy import ndarray
import joblib


# The model type
# In general, models should implement the following structure:
class Model(NamedTuple):
    predict_proba: Callable[[ndarray], ndarray]
    predict: Callable[[ndarray], ndarray]


class ModelLoader:
    _model_dict: MutableMapping[str, Model]

    def __init__(self) -> None:
        self._model_dict = {}

    def get_model(self, model_name: str) -> Model | None:
        try:
            model = self._model_dict[model_name]
            return model
        except KeyError:
            logging.warning(f"{model_name} not loaded")
            return None

    def load_model(self, model_name: str, model_file_name: str) -> Model | None:
        try:
            print(f"Loading model: '{model_name}', file: '{model_file_name}' ")

            model = joblib.load(
                open(f"./src/models_loader/models/{model_file_name}", "rb")
            )
            self._model_dict[model_name] = model

            return model

        except FileNotFoundError:
            logging.warning(
                f"[ {model_name} ]: Could not load file: '{model_file_name}'"
            )

            return None

        except:
            logging.error(
                "Could not load the model. Check if your file is a valid joblib dump object or check for any c"
            )

            return None


# Global models handler. Should not be accessed by other modules.
_globalModels = ModelLoader()


# Interfaces for other modules
def get_model(model_name: str) -> Model | None:
    return _globalModels.get_model(model_name)


def load_model(model_name: str, model_file_name: str) -> Model | None:
    return _globalModels.load_model(model_name, model_file_name)
