"""
Python script to produce a nice looking multi score plot
for synthetic datasets hard coding the values
"""

import matplotlib.pyplot as plt
import numpy as np
import os

#NOTE: Hard coded data for EIF+_EXIFFI+

# xy_features = [0, 1, 3, 4, 5, 2]
# xy_values   = [3.822, 3.744, 3.055, 3.036, 3.030, 3.011]
#
# hm_features = [1, 0, 3, 4, 2, 5]
# hm_values   = [1.708, 1.701, 1.668, 1.665, 1.660, 1.647]

#NOTE: Hard coded data for IF_DIFFI

xy_features = [4, 2, 5, 0, 1, 3]
xy_values   = [1.977, 1.889, 1.858, 1.825, 1.8, 1.75]

hm_features = [4, 5, 3, 2, 1, 0]
hm_values   = [2.417, 2.277, 2.194, 2.134, 1.498, 1.279]

# Color scheme per feature (from the reference image)
feature_colors = {
    0: '#1f77b4',   # blue
    1: '#e8e82a',   # yellow
    2: '#1a1a1a',   # black
    3: '#2ca02c',   # green
    4: '#87ceeb',   # light blue
    5: '#ff7f0e',   # orange
}

def normalize(values, floor=0.05):
    """Min-max normalize to [0, 1], with a floor so the smallest bar is visible."""
    arr = np.array(values, dtype=float)
    lo, hi = arr.min(), arr.max()
    if hi == lo:
        return np.ones_like(arr)
    normed = (arr - lo) / (hi - lo)
    # Give the minimum a small visible width instead of 0
    normed = normed * (1.0 - floor) + floor
    return normed

fig, axes = plt.subplots(1, 2, figsize=(6, 2.2), sharey=True)

# ---- Left subplot: xy_axis ----
ax = axes[0]
x_pos = np.arange(len(xy_features))
normed = normalize(xy_values)
colors = [feature_colors[f] for f in xy_features]

ax.bar(x_pos, normed, color=colors)
ax.set_xticks(x_pos)
ax.set_xticklabels(xy_features)
ax.set_title("xy_axis")
ax.set_ylabel("Importance Score")
ax.set_xlabel("Features")

# ---- Right subplot: half_moon ----
ax = axes[1]
x_pos = np.arange(len(hm_features))
normed = normalize(hm_values)
colors = [feature_colors[f] for f in hm_features]

ax.bar(x_pos, normed, color=colors)
ax.set_xticks(x_pos)
ax.set_xticklabels(hm_features)
ax.set_title("half_moon")
ax.set_xlabel("Features")

#NOTE: Hard coded path

filename="multi_score_plot_diffi.png"
plot_path="/home/df/papers/exiffi-ind-presentation/img/datasets/diffi/syn_data"

plt.tight_layout(pad=0)
plt.savefig(os.path.join(plot_path,filename), dpi=300, bbox_inches='tight', pad_inches=0)
