#!/bin/bash

# Verify the new options are plumbed through to the MT.
# The second two competitions fail because permissions are denied but everything else works, although
# the new options are ignored.

# Pagination for listing of competitions, datasets, and kernels is out-of-scope for current work.

kaggle competitions files titanic --page-size=3 --page-token=abcd
kaggle kernels files hermengardo/ps4e4-ensemble-eda --page-size=5 # valid page token required
kaggle datasets files nelgiriyewithana/apple-quality --page-size=7 --page-token=abcd
kaggle models instances versions files google/gemma/pytorch/7b/2 --page-size=3 --page-token=abcd
