# `MoleculeLookup`

This Python package automates the lookup of rotational constants from a
DataFrame, typically produced by Kelvin's `g16-isomers` code which parses
a whole bunch of Gaussian '16 calculations into a Pandas DataFrame.

Everything is written in a object-oriented way which might be overkill,
but does support some extensibility in a few fronts including implementing
custom loss functions used to calculate distance.

## Installation

`MoleculeLookup` requires the packager `poetry` -- the details of installing
this !(can be found here)[https://poetry.eustace.io/docs/].

After you install `poetry`, you just need to clone this repository, navigate
into the directory with `pyproject.toml` and run:

```
poetry install

pip install .
```

## Running the tool

After installing, you will be able to interact with the command-line interface.
You can call it for help by adding the `--help` flag like so:

```
> search_constants --help

Usage: search_constants [OPTIONS] FILEPATH CONSTANTS...

  Search a DataFrame for a set of target rotational constants. The constants
  must be in a set of three corresponding to A, B, C in that specific order.

  The error reported here corresponds to the average percentage error across
  A, B, and C.

  Parameters ---------- filepath : str     A filepath to the DataFrame to
  lookup. The file extension is     used to determine the parser to use:
  either `.pkl` or `.csv`. constants : float     Three rotational constants
  one after another as floats.     These correspond to A, B, C in that
  order. nitems : int     Number of rows to return with the lowest error.

Options:
  -n, --nitems INTEGER  Number of rows to return with the optimal answer
                        [default: 10]
  --help                Show this message and exit.

```

To search, you need a formatted DataFrame and a set of three rotational constants;
in this example, we're going to use a `mol_dataframe.pkl` file in our directory
as a reference, and search for a molecule with rotational constants 8000, 5000, 3000:

```
> search_constants mol_dataframe.pkl 8000. 5000. 3000.

             A            B            C     kappa   defect         filename     error
0  4751.149467  3702.129618  3252.063601 -0.399546 -312.388  Structure0078-1  0.318956
1  4525.208447  3778.267622  3446.955735 -0.385465 -352.908  Structure0020-1  0.320522
2  4581.632214  3718.060678  3310.861574 -0.359130 -334.210  Structure0017-1  0.332333
3  6035.978397  2949.957087  2793.142024 -0.903285 -264.650  Structure0054-1  0.364795
4  7134.269775  2809.552829  2403.059020 -0.828165 -144.309  Structure0077-1  0.383133
5  5350.350832  3355.969198  2471.618771 -0.385597 -144.897  Structure0090-1  0.399630
6  5350.360233  3355.962682  2471.616565 -0.385603 -144.897  Structure0099-1  0.399631
7  6591.068208  2887.607506  2336.012887 -0.740734 -126.238  Structure0066-1  0.409847
8  4608.566731  3588.184752  2298.736164  0.116488 -109.473  Structure0001-1  0.478142
9  6602.936603  2816.360135  2025.089639 -0.654305  -22.939  Structure0023-1  0.489446
```