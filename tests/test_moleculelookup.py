from moleculelookup import __version__
from moleculelookup import main


def test_version():
    assert __version__ == '0.1.0'


def test_parser():
    mol_lookup = main.MoleculeLookup.from_file("mol_dataframe.pkl")
    assert len(mol_lookup.data) == 78
    headers = [
        "A", "B", "C", "u_A", "u_B", "u_C", "kappa", "defect"
    ]
    for header in headers:
        assert header in mol_lookup.data.columns
    
    
def test_class():
    """
    Test to ensure that the algorithm is working correctly by finding
    an exact match.
    """
    mol_lookup = main.MoleculeLookup.from_file("mol_dataframe.pkl")
    test = [11003.111047, 949.49747, 878.817313]
    search = mol_lookup.search_molecule(test)
    assert search.iloc[0]["filename"] == "Structure0022-1"