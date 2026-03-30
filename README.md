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

- `datasets/data/PIADE/`: contains the two `csv` files of the PIADE dataset.
    - `raw_data.csv` contains the raw data.
    - `sequences_1h_data.csv` contains an aggregated version of the raw data
    where each pair of consecutive samples is distanced by 1h of time.
    - there are also all the directories containing the `PIADE` data divided by
    single machine
- `datasets/data/TEP_ACME`: this folder contains the data of the `TEP` dataset
- There are not data for the `CoffeeData` dataset because it's a confidential
dataset and we are not allowed to share its contents
- `ExIFFI_original`: Submodule that contains the original implementation of the
`ExIFFI` algorithm, in Python.
    - `utils_reboot`: Directory with the utility functions
    - `models_reboot`: Directory with the functions related to the models
    - `experiments`: Directory containing all the python scripts to launch the
    experiments.
- `ExIFFI_Core`: Submodule containing the enhanced implementation of `ExIFFI`.
Some of the functions used to fit the model and compute the importance scores
are written in C in order to be executed in parallel through the `openmp`
library.

## Launch Experiments

For the tutorial on how to run the experiments [check this guide](ExIFFI_original/exp_guide.md).

## Additional Results

Additional results not reported in the paper [are contained here](additional_results/results.md)
