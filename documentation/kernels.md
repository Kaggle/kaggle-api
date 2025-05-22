# Kernels Commands (`kaggle kernels` or `kaggle k`)

This section describes commands for interacting with Kaggle Kernels (Notebooks and Scripts).

## `kaggle kernels list`

Lists available kernels.

**Usage:**

```bash
kaggle kernels list [options]
```

**Options:**

*   `-m, --mine`: List only your kernels.
*   `-p, --page <PAGE>`: Page number.
*   `--page-size <SIZE>`: Number of items per page.
*   `-s, --search <SEARCH_TERM>`: Search term.
*   `-v, --csv`: Output in CSV format.
*   `--parent <PARENT_KERNEL>`: Find children of a specific kernel.
*   `--competition <COMPETITION_SLUG>`: Filter by competition.
*   `--dataset <DATASET_SLUG>`: Filter by dataset.
*   `--user <USER>`: Filter by owner.
*   `--language <LANGUAGE>`: Filter by language (e.g., `python`, `r`).
*   `--kernel-type <TYPE>`: Filter by type (e.g., `script`, `notebook`).
*   `--output-type <TYPE>`: Filter by output type (e.g., `visualizations`, `data`).
*   `--sort-by <SORT_BY>`: Sort results (e.g., `hotness`, `dateRun`).

**Examples from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is an environment variable with your username)

1.  ```bash
    kaggle k list -m -s Exercise --page-size 5 -p 2 -v --sort-by dateRun
    ```
    **Purpose:** Lists your kernels (`-m`) that contain "Exercise" in their title (`-s Exercise`), showing 5 results per page (`--page-size 5`), displaying the second page (`-p 2`), in CSV format (`-v`), and sorted by the last run date (`--sort-by dateRun`).

2.  ```bash
    kaggle k list --parent $KAGGLE_DEVELOPER/exercise-lists
    ```
    **Purpose:** Lists kernels that are children (forks) of the kernel `$KAGGLE_DEVELOPER/exercise-lists`.

3.  ```bash
    kaggle k list --competition house-prices-advanced-regression-techniques --page-size 5
    ```
    **Purpose:** Lists kernels associated with the 'house-prices-advanced-regression-techniques' competition, showing 5 results per page.

4.  ```bash
    kaggle k list --dataset dansbecker/home-data-for-ml-course --page-size 5
    ```
    **Purpose:** Lists kernels that use the dataset 'dansbecker/home-data-for-ml-course', showing 5 results per page.

5.  ```bash
    kaggle k list --user $KAGGLE_DEVELOPER --language python --kernel-type notebook --output-type data
    ```
    **Purpose:** Lists Python notebooks created by `$KAGGLE_DEVELOPER` that produce data outputs.

## `kaggle kernels files`

Lists output files for a specific kernel.

**Usage:**

```bash
kaggle kernels files <KERNEL_SLUG> [options]
```

*   `<KERNEL_SLUG>`: Kernel slug (e.g., `owner/kernel-name`).
*   `-v, --csv`: Output in CSV format.
*   `--page-size <SIZE>`: Number of items per page.
*   `--page-token <TOKEN>`: Page token for pagination.

**Example from `test_commands.sh`:**

```bash
kaggle kernels files kerneler/sqlite-global-default -v --page-size=1
```

**Purpose:** Lists the output files of the kernel 'kerneler/sqlite-global-default', displaying results in CSV format and showing 1 file per page.

## `kaggle kernels init`

Initializes a new `kernel-metadata.json` file.

**Usage:**

```bash
kaggle kernels init -p <FOLDER_PATH>
```

*   `-p <FOLDER_PATH>`: Path to the folder where the metadata file will be created. Defaults to current directory.

**Example from `test_commands.sh`:**

```bash
kaggle k init -p tests/kernel
```

**Purpose:** Creates a template `kernel-metadata.json` file in the `tests/kernel` directory. This file is necessary for pushing new kernels or updating existing ones.

## `kaggle kernels push`

Pushes a kernel (code and metadata) to Kaggle. This will typically run the kernel on Kaggle servers.

**Usage:**

```bash
kaggle kernels push -p <FOLDER_PATH> [options]
```

*   `-p <FOLDER_PATH>`: Path to the folder containing the kernel file (e.g., `.ipynb`, `.Rmd`, `.py`) and `kernel-metadata.json`. Defaults to current directory.
*   `-t, --timeout <SECONDS>`: Timeout for the kernel run in seconds.

**Example from `test_commands.sh`:**
(Assumes `kernel-metadata.json` and a kernel file like `exercise-as-with.ipynb` are in `tests/kernel`, and the metadata file has been modified to point to a new kernel slug `exercise-delete`)
```bash
# Setup: Modify the notebook file name (part of the test script)
# sed -i s/exercise-as-with/exercise-delete/ tests/kernel/exercise-as-with.ipynb

kaggle kernels push -p tests/kernel
```

**Purpose:** Pushes the kernel code and metadata from the `tests/kernel` directory to Kaggle. The `kernel-metadata.json` file in this directory defines the kernel's properties, including its title, slug, language, and associated data sources. This command will create a new kernel or update an existing one based on the metadata.

## `kaggle kernels pull`

Pulls the code and metadata of a kernel from Kaggle.

**Usage:**

```bash
kaggle kernels pull <KERNEL_SLUG> [options]
```

*   `<KERNEL_SLUG>`: Kernel slug (e.g., `owner/kernel-name`).
*   `-p, --path <PATH>`: Path to download the kernel files to.
*   `-w, --wp`: Download to current working path.
*   `-m, --metadata`: Download/generate metadata file as well.

**Examples from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is an environment variable with your username)

1.  ```bash
    kaggle k pull -p tests/kernel $KAGGLE_DEVELOPER/exercise-as-with -m
    ```
    **Purpose:** Pulls the kernel `$KAGGLE_DEVELOPER/exercise-as-with` (both code and metadata file because of `-m`) into the `tests/kernel` directory.

2.  ```bash
    kaggle k pull --wp $KAGGLE_DEVELOPER/exercise-as-with
    ```
    **Purpose:** Pulls the kernel `$KAGGLE_DEVELOPER/exercise-as-with` (code only) into the current working directory.

## `kaggle kernels output`

Downloads the output files from the latest run of a kernel.

**Usage:**

```bash
kaggle kernels output <KERNEL_SLUG> [options]
```

*   `<KERNEL_SLUG>`: Kernel slug.
*   `-p, --path <PATH>`: Path to download output files to.
*   `-w, --wp`: Download to current working path.
*   `-o, --force`: Force download, overwriting existing files.
*   `-q, --quiet`: Suppress progress output.

**Example from `test_commands.sh`:**

```bash
kaggle k output kerneler/sqlite-global-default -o
```

**Purpose:** Downloads the output files from the kernel 'kerneler/sqlite-global-default' to the current working directory, overwriting any existing files (`-o`).

## `kaggle kernels status`

Displays the status of the latest run of a kernel.

**Usage:**

```bash
kaggle kernels status <KERNEL_SLUG>
```

*   `<KERNEL_SLUG>`: Kernel slug.

**Example from `test_commands.sh`:**

```bash
kaggle k status kerneler/sqlite-global-default
```

**Purpose:** Shows the current status (e.g., running, complete, error) of the latest execution of the kernel 'kerneler/sqlite-global-default'.

## `kaggle kernels delete`

Deletes a kernel from Kaggle.

**Usage:**

```bash
kaggle kernels delete <KERNEL_SLUG> [options]
```

*   `<KERNEL_SLUG>`: Kernel slug to delete.
*   `-y, --yes`: Skip confirmation prompt.

**Examples from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is an environment variable with your username and a kernel named `exercise-delete` exists under your account)
1.  ```bash
    kaggle k delete $KAGGLE_DEVELOPER/exercise-delete
    ```
    **Purpose:** Attempts to delete the kernel `$KAGGLE_DEVELOPER/exercise-delete`. It will prompt for confirmation.

2.  ```bash
    kaggle k delete $KAGGLE_DEVELOPER/exercise-delete --yes
    ```
    **Purpose:** Deletes the kernel `$KAGGLE_DEVELOPER/exercise-delete` without prompting for confirmation (`--yes`).
