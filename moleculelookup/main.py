
from pathlib import Path

import pandas as pd
import numpy as np

from moleculelookup import losses


class MoleculeLookup:
    def __init__(self, dataframe: pd.DataFrame, loss=None, labels=["A", "B", "C"]):
        self.data = dataframe
        # remove NaN and whatnot
        self.data.dropna(subset=labels)
        self.targets = self.data[labels]
        self.labels = labels
        if loss is None:
            self.loss = losses.PercentageError(self.targets.values)
            
    def __repr__(self):
        if hasattr(self, "sorted_data"):
            print(self.sorted_data.head(10))
        else:
            print(self.targets.head(10))
        
    @classmethod
    def from_file(cls, filepath: str, loss=None, labels=["A", "B", "C"]):
        """
        Initializes a `MoleculeLookup` object from a Pandas dataframe
        file saved to disk. The two supported formats are Pickle and
        CSV files, which are inferred from the `.pkl` and `.csv`
        file extensions.
        
        Parameters
        ----------
        filepath : str
            Path to the dataframe
        labels : list, optional
            List of labels to use for comparison, by default ["A", "B", "C"]
        
        Returns
        -------
        MoleculeLookup
            Instance of the `MoleculeLookup` object
        
        Raises
        ------
        Exception
            [description]
        """
        path = Path(filepath)
        assert path.exists() is True
        if "pkl" in path.suffix:
            parser = pd.read_pickle
        elif "csv" in path.suffix:
            parser = pd.read_csv
        else:
            raise Exception("File extension not recognized; must be .pkl or .csv!")
        mol_lookup = cls(parser(path), loss=loss, labels=labels)
        return mol_lookup
    
    def search_molecule(self, Y: np.ndarray, subset=["A", "B", "C", "kappa", "defect", "filename", "error"], nrows=10):
        """
        Look up the database for the nearest molecules matching the specified
        labels. The loss is computed with some predefined loss function, a few
        of which can be found in the `losses` module.
        
        A dataframe is then returned with the lowest errors at the top. The user
        can specify which labels to include in the return, which by default is
        a set of minimally descriptive values. The user can also specify the number
        of rows to return. The dataframe which holds all of this information is
        stored as the attribute `MoleculeLookup.sorted_data`.
        
        Parameters
        ----------
        Y : np.ndarray
            Array of experimental values to use for comparison
        subset : list, optional
            Subset of data to report, by default ["A", "B", "C", "kappa", "defect", "filename"]
        nrows : int, optional
            Number of rows to report, by default 10
        
        Returns
        -------
        pd.DataFrame
            DataFrame containing the closest rows to the experimental data
        """
        self.data["error"] = self.loss.compute_loss(Y)
        self.sorted_data = self.data.sort_values(["error"], ascending=True)
        self.sorted_data.reset_index(inplace=True, drop=True)
        return self.sorted_data[subset].head(nrows)