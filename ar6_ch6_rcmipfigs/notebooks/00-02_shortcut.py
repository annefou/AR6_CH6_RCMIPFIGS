# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from IPython.display import clear_output

# %% [markdown]
# ## Preprocess:

# %%
import runpy

runpy.run_path('0_database-generation.py')
runpy.run_path('1_preprocess_data.py')
runpy.run_path('2_compute_delta_T.ipynb.py')
clear_output()

# %% [markdown]
# ## Create table on delta T dependence on ECS:

# %%
runpy.run_path('2-1_compute_delta_T_sensitivity.py')

# %% [markdown]
# ## Create plots etc:

# %%
runpy.run_path('3_delta_T_plot.py')
runpy.run_path('3-1_delta_T_plot_SLCF_sum.py')
runpy.run_path('3-2_delta_T_plot_bar_stacked.py')
runpy.run_path('3-2_delta_T_plot_contribution_total.py')
