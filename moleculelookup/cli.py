
import click

from moleculelookup.main import MoleculeLookup


@click.command()
@click.argument("filepath", type=click.Path(exists=True))
@click.argument("constants", nargs=3)
@click.option(
    "-n",
    "--nitems",
    "nitems",
    default=10,
    help="Number of rows to return with the optimal answer",
    show_default=True
)
def search_constants(filepath, constants, nitems):
    """
    Search a DataFrame for a set of target rotational constants.
    The constants must be in a set of three corresponding to A, B, C
    in that specific order.
    
    The error reported here corresponds to the average percentage
    error across A, B, and C.
    
    Parameters
    ----------
    filepath : str
        A filepath to the DataFrame to lookup. The file extension is
        used to determine the parser to use: either `.pkl` or `.csv`.
    constants : float
        Three rotational constants one after another as floats.
        These correspond to A, B, C in that order.
    nitems : int
        Number of rows to return with the lowest error.
    """
    mol_lookup = MoleculeLookup.from_file(filepath)
    try:
        constants = [float(constant) for constant in constants]
    except ValueError:
        raise ValueError(f"Could not convert {constants} to floats.")
    print(mol_lookup.search_molecule(constants))
    