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

After you install `poetry`, you just need to clone this repository, and run
