# Additional Results

In this section we report results from the [`exiffi-ind` Conference
Paper](https://ieeexplore.ieee.org/document/10761374) and from the [latest
version of `exiffi-ind`](https://arxiv.org/abs/2405.01158), submitted to IEEE
Transaction on Industry Applications.

The reason for this section is that not all the experimental results are
contained in the two papers. Some results reported in the conference paper were
removed from the journal one for the sake of space and some additional results
for the extended journal version could not make it in the paper for the sake of
space.

>[!note]
> In any case all the results reported here are reproducible using the codebase,
> [following the quick guide provided](ExIFFI_original/README.md).

## `TEP` Dataset

### Local Scoremaps

The local scoremaps produced for the `TEP` dataset are contained in
[`exiffi-ind` Conference
Paper](https://ieeexplore.ieee.org/document/10761374). For a detailed
description check Figure 2 and Section C. `Case Study 1: TEP Dataset`.

#### `xmeas_11` vs `xmeas_12`

![Local Scoremap `xmeas_11` vs `xmeas_12`](img/TEP/local_scoremaps/scoremap_TEP_xmeas_11_12.png)

#### `xmeas_11` vs `xmeas_22`

![Local Scoremap `xmeas_11` vs `xmeas_22`](img/TEP/local_scoremaps/scoremap_TEP_xmeas_11_22.png)

#### `xmeas_11` vs `xmeas_7`

![Local Scoremap `xmeas_11` vs `xmeas_7`](img/TEP/local_scoremaps/scoremap_TEP_xmeas_11_7.png)

### Feature Selection Plots

For the sake of space the Feature Selection plots reported in [latest version
of `exiffi-ind`](https://arxiv.org/abs/2405.01158) cover only some
`model-interpretation` pairs. In this section results for other
`model-interpretation` pairs are reported.

>[!note]
> As in the paper in all these plots the model used to evaluate the
> average precisions for all the feature subsets is `EIF+`.

#### `EIF_EXIFFI`

![Feature Selection `EIF_EXIFFI`](img/TEP/fs_plots/EIF/EXIFFI/fs_plot_EIF_EXIFFI.png)

#### `EIF_ACME`

![Feature Selection `EIF_ACME`](img/TEP/fs_plots/EIF/ACME/fs_plot_EIF_ACME.png)

#### `IF_ACME`

![Feature Selection `IF_ACME`](img/TEP/fs_plots/IF/ACME/fs_plot_IF_ACME.2.png)

#### `IF_KernelSHAP`

![Feature Selection `IF_KernelSHAP`](img/TEP/fs_plots/IF/KernelSHAP/17-03-2026_14-00-39_TEP_ACME_EIF+_IF_KernelSHAP_feature_selection_2.png)

#### `AE_ACME`

![Feature Selection `AE_ACME`](img/TEP/fs_plots/AE/ACME/22-03-2026_20-16-08_TEP_ACME_EIF+_AE_ACME_feature_selection_2.png)

#### `SVDD_ACME`

![Feature Selection `SVDD_ACME`](img/TEP/fs_plots/SVDD/ACME/22-03-2026_20-16-37_TEP_ACME_EIF+_SVDD_ACME_feature_selection_2.png)

## `PIADE` Dataset

### Local Scoremaps

The local scoremaps produced for the `PIADE` dataset (in particular `piade_s2`)
are contained in [`exiffi-ind` Conference
Paper](https://ieeexplore.ieee.org/document/10761374). For a detailed
description check Figure 5 and Section D. `Case Study 2: PIADE Dataset`.

#### `%scheduled_downtime` vs `A_010`

![Local Scoremap `%scheduled_downtime` vs `A_010`](img/PIADE/local_scoremaps/scoremap_PIADE_downtime_A_10.png)

#### `%scheduled_downtime` vs `A_017`

![Local Scoremap `%scheduled_downtime` vs `A_017`](img/PIADE/local_scoremaps/scoremap_PIADE_downtime_A_17.png)

#### `%scheduled_downtime` vs `%idle`

![Local Scoremap `%scheduled_downtime` vs `%idle`](img/PIADE/local_scoremaps/scoremap_PIADE_downtime_idle.png)

## `SMD` Dataset

For the sake of space in the paper the `SMD` dataset was used just to test the
scalability of `ExIFFI` in terms of performances and computational complexity
on a larger dataset. However experiments with `ExIFFI` were also performed and
are reported here.

>[!info]
> Also in this case we will focus on the `machine-1-1` subset of `SMD`.

The `SMD` dataset also provides ground truths on the features contributing to
each anomalous time interval recorded in the test set. For `machine-1-1` the
ground truths are the following:

```txt
15849-16368:1,9,10,12,13,14,15
16963-17517:1,2,3,4,6,7,9,10,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36
18071-18528:1,2,9,10,12,13,14,15
19367-20088:1,2,3,4,9,10,11,12,13,14,15,16,25,28
20786-21195:1,9,10,12,13,14,15
24679-24682:9,13,14,15
26114-26116:9,13,14,15
27554-27556:9,13,14,15
```

### `EIF+_EXIFFI+`

#### Score Plot

The Score Plot is in accordance with the ground truths since feature 9 is
present in the list of important features in all the anomalous segments and
it's correctly placed at the top of the ranking by `ExIFFI`.

![Score Plot `EIF+_EXIFFI+`](img/SMD/score_plots/EIF+/EXIFFI+/19-03-2026_16-48-18_GFI_Score_plot_machine-1-1_EXIFFI+_2.png)

#### Local Scoremap

The local scoremap confirms the importance of feature 9 as it shows how the
majority of the outliers are aligned along this axis.

![Local Scoremap `EIF+_EXIFFI+`](img/SMD/local_scoremaps/EIF+/EXIFFI+/20-03-2026_18-28-49_importance_map_machine-1-1_EXIFFI+_2_feat_9_5_1.5_9_300.png)

#### Feature Selection

A positive value of the $AUC_{FS}$ score confirms the correct `GFI` ranking
produced by the model. The average precision trend starts to decrease in the
last 4 iterations.

![Feature Selection `EIF+_EXIFFI+`](img/SMD/fs_plots/EIF+/EXIFFI+/20-03-2026_11-36-03_machine-1-1_EIF+_EXIFFI+_feature_selection_2.png)

### `EIF_EXIFFI`

#### Score Plot

When `ExIFFI` is used to interpret the `EIF` model (i.e. without the hyperplane
partition modification introduced in `EIF+`) the relevance of feature 9 is even
more pronounced.

![Score Plot `EIF_EXIFFI`](img/SMD/score_plots/EIF/EXIFFI/19-03-2026_18-17-20_GFI_Score_plot_machine-1-1_EXIFFI_2.png)

#### Local Scoremap

Similar result to `EIF+_EXIFFI+`.

![Local Scoremap `EIF_EXIFFI`](img/SMD/local_scoremaps/EIF/EXIFFI/20-03-2026_18-28-58_importance_map_machine-1-1_EXIFFI_2_feat_9_5_1.5_9_300.png)

#### Feature Selection

Similar result to `EIF+_EXIFFI+`.

![Feature Selection `EIF_EXIFFI`](img/SMD/fs_plots/EIF/EXIFFI/20-03-2026_15-58-06_machine-1-1_EIF+_EIF_EXIFFI_feature_selection_2.png)

