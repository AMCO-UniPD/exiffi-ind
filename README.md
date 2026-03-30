# Towards Transparent and Efficient Anomaly Detection in Industrial Processes through ExIFFI

This repository contains the code and data used in the paper ["Towards
Transparent and Efficient Anomaly Detection in Industrial Processes through
ExIFFI"](https://arxiv.org/abs/2405.01158).

>[!info]
> This paper is an extension of ["Interpretable Data-driven Anomaly Detection in Industrial Processes with
> ExIFFI"](https://arxiv.org/abs/2405.01158), presented at IEEE RTSI 2024 (18-20
> September 2024, Lecco, Italy).

# Usage

We use `uv` to handle python dependencies. In order to reproduce the paper
results install `uv` with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then clone the repository using the `--recurse-submodules` option to also
include and initialize submodules:

```bash
git clone --recurse-submodules https://github.com/FrancescoBorsatti/ExIFFI_Industrial_Test.git
```

>[!warning]
> In the `ExIFFI_Core` submodule be sure to be checked out at the `exiffi_core` branch
> which contains the working version of the code.

Finally synchronize the packages by running:

```bash
uv sync
```

In order to activate the python virtual environment use (in the project root
directory):

```bash
source .venv/bin/activate
```

## Repository Structure

The repository is organized as follows:

### Data

All publicly available datasets are contained inside `datasets/data`. More
details on their organization [here](datasets/readme.md).

### `ExIFFI_Core`

In the `ExIFFI_Core` submodule the enhanced implementation of `ExIFFI` is contained.
Some of the functions used to fit the model and compute the importance scores
are written in C in order to be executed in parallel through the `openmp`
library.

>[!note]
> More details [here](ExIFFI_Core/README.md)

### Experiments

All the code launch experiments is contained in the `ExIFFI_original` folder.
For the tutorial on how to run the experiments [check this
guide](ExIFFI_original/exp_guide.md).

### Additional Results

Additional results not reported in the paper [are contained here](additional_results/results.md)
