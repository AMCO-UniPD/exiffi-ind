# `exiffi-ind` Datasets

In this section some information on the datasets used in the experiments are
provided.

## `PIADE` Dataset

Directory `datasets/data/PIADE/` contains the two `csv` files of the PIADE dataset.
- `raw_data.csv` contains the raw data.
- `sequences_1h_data.csv` contains an aggregated version of the raw data
where each pair of consecutive samples is distanced by 1h of time.
- there are also all the directories containing the `PIADE` data divided by
single machine. In particular there are two version of the `PIADE` dataset:
    - `piade_s*` → entire set of data for a certain packaging machine
    - `piade_s*_alarms_no_zeros` → the alarm columns containing only 0
    values (i.e. alarm never triggered) are removed.

## `TEP` Dataset

Directory `datasets/data/TEP_ACME` contains the data of the `TEP` dataset.

The dataset was constructed as follows:
- 70 normal simulations were randomly extracted from the pool of normal
simulations.
- 3 faulty simulations were randomly extracted within the simulations with
`faultNumber=12`.

## `SMD` Dataset

The data for the `SMD` dataset are contained in
`datasets/data/SerrverMachineDataset` which was retrieved from [the
`OmniAnomaly` repository](https://github.com/NetManAIOps/OmniAnomaly).

## `CoffeeData` Dataset

There are not data for the `CoffeeData` dataset because it's a confidential
dataset and we are not allowed to share its contents
