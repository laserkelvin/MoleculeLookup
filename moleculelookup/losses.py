

import numpy as np


class LossFunction:
    def __init__(self, y_true: np.ndarray, name: str):
        self.y_true = y_true
    
    def compute_loss(self, y_pred: np.ndarray):
        loss = self._loss_func(y_pred)
        # Filter out numerical problems like dividing
        # by zero; infinity goes to large numbers
        loss = np.nan_to_num(loss)
        # If there's more than one dimension, take the
        # mean across the row
        if len(loss.shape) == 2:
            loss = np.mean(loss, axis=1)
        loss = np.abs(loss)
        return loss
    

class MeanSquaredError(LossFunction):
    def __init__(self, y_true: np.ndarray):
        super().__init__(y_true, name="mean_squared_error")
    
    def _loss_func(self, y_pred):
        return np.mean(np.square(self.y_true - y_pred), axis=1)
    

class PercentageError(LossFunction):
    def __init__(self, y_true: np.ndarray):
        super().__init__(y_true, name="percentage_error")
    
    def _loss_func(self, y_pred: np.ndarray):
        return (self.y_true - y_pred) / self.y_true