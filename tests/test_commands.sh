#!/bin/bash

# Verify the new options are plumbed through to the MT.
# The second two competitions fail because permissions are denied but everything else works, although
# the new options are ignored.

# Pagination for listing of competitions, datasets, and kernels is out-of-scope for current work.

# kaggle competitions list --page-size=3 --page-token=abcd
kaggle competitions files -c competitions/titanic --page-size=4 --page-token=abcd
# kaggle competitions submissions competitions/titanic --page-size=5 --page-token=abcd
# kaggle kernels list --page-size=3 --page-token=abcd
# kaggle datasets list --page-size=6 --page-token=abcd
kaggle datasets files nelgiriyewithana/apple-quality --page-size=7 --page-token=abcd
