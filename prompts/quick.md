Modify the code in kaggle/cli.py and kaggle/api/kaggle_api_extended.py to add an
optional parameter named "quick" to the command `kaggle kernels push`. It should
be abbreviated to "k" as well. If the new parameter is included then a bool should
be passed into a new parameter to KaggleApi.kernels_push(). When that new parameter
to `kernels_push()` is `True` then use the enum value `KernelVersionType.QUICK` as
the value to a new property in the ApiSaveKernelRequest, named kernel_version_type.
If the new parameter is not specified (or is `False`) use
`KernelVersionType.BATCH` instead. Add a new section in `tests/unit_tests.py` to 
test it. The new code can be added to `test_kernels_c_push()` before the existing
call to `kernels_push()`. Add a small delay, like sleep for one second.
