# Datasets Commands (`kaggle datasets` or `kaggle d`)

This section describes commands for interacting with Kaggle datasets.

## `kaggle datasets list`

Lists available datasets.

**Usage:**

```bash
kaggle datasets list [options]
```

**Options:**

*   `--sort-by <SORT_BY>`: Sort results (e.g., `hottest`, `votes`).
*   `--size <SIZE_BYTES>`: (DEPRECATED) Filter by size. Use `--min-size` and `--max-size`.
*   `--file-type <FILE_TYPE>`: Filter by file type (e.g., `csv`, `sqlite`).
*   `--license <LICENSE_NAME>`: Filter by license (e.g., `cc`, `gpl`).
*   `--tags <TAG_IDS>`: Filter by tags (comma-separated).
*   `-s, --search <SEARCH_TERM>`: Search term.
*   `-m, --mine`: List only your datasets.
*   `--user <USER>`: Filter by owner username or organization.
*   `-p, --page <PAGE>`: Page number.
*   `-v, --csv`: Output in CSV format.
*   `--max-size <BYTES>`: Maximum dataset size in bytes.
*   `--min-size <BYTES>`: Minimum dataset size in bytes.

**Examples from `test_commands.sh`:**

1.  ```bash
    kaggle d list --size 10
    ```
    **Purpose:** Lists datasets. The `--size 10` is deprecated but was intended to filter by size.

2.  ```bash
    kaggle d list -m
    ```
    **Purpose:** Lists only the datasets owned by the authenticated user.

3.  ```bash
    kaggle d list --user oktayrdeki --csv
    ```
    **Purpose:** Lists datasets owned by the user 'oktayrdeki' and outputs the list in CSV format.

4.  ```bash
    kaggle d list --file-type csv --page 2 --sort-by updated -s student --min-size 13000 --max-size 15000
    ```
    **Purpose:** This command performs a complex search for datasets. It looks for datasets containing CSV files (`--file-type csv`), on the second page of results (`--page 2`), sorted by the last updated date (`--sort-by updated`), containing the term "student" (`-s student`), and with a size between 13000 and 15000 bytes.

5.  ```bash
    kaggle d list --license odb --tags internet --search telco
    ```
    **Purpose:** Lists datasets that have an 'odb' license, are tagged with 'internet', and contain the search term 'telco'.

## `kaggle datasets files`

Lists files within a specific dataset.

**Usage:**

```bash
kaggle datasets files <DATASET> [options]
```

*   `<DATASET>`: Dataset slug (e.g., `owner/dataset-name`).
*   `-v, --csv`: Output in CSV format.
*   `--page-size <SIZE>`: Number of items per page.
*   `--page-token <TOKEN>`: Page token for pagination.

**Example from `test_commands.sh`:**

```bash
kaggle datasets files kerneler/brazilian-bird-observation-metadata-from-wikiaves --page-size=7 --page-token=abcd
```

**Purpose:** Lists the files in the dataset 'kerneler/brazilian-bird-observation-metadata-from-wikiaves'. It shows 7 files per page and uses 'abcd' as a page token (likely for testing pagination).

## `kaggle datasets download`

Downloads dataset files.

**Usage:**

```bash
kaggle datasets download <DATASET> [options]
```

*   `<DATASET>`: Dataset slug.
*   `-f, --file <FILE_NAME>`: Specific file to download.
*   `-p, --path <PATH>`: Path to download files to.
*   `-w, --wp`: Download to current working path.
*   `--unzip`: Unzip the downloaded file (if it's a zip).
*   `-o, --force`: Force download, overwriting existing files.
*   `-q, --quiet`: Suppress progress output.

**Examples from `test_commands.sh`:**

1.  ```bash
    kaggle datasets download -d willianoliveiragibin/pixar-films
    ```
    **Purpose:** Downloads all files for the dataset 'willianoliveiragibin/pixar-films' to the current directory.

2.  ```bash
    kaggle d download goefft/public-datasets-with-file-types-and-columns -p tmp --unzip -o -q
    ```
    **Purpose:** Downloads the dataset 'goefft/public-datasets-with-file-types-and-columns' into a directory named `tmp`, unzips it (`--unzip`), overwrites if exists (`-o`), and does so quietly (`-q`).

3.  ```bash
    kaggle d download goefft/public-datasets-with-file-types-and-columns -f dataset_results.csv -w -q -o
    ```
    **Purpose:** Downloads only the `dataset_results.csv` file from 'goefft/public-datasets-with-file-types-and-columns' to the current working directory (`-w`), quietly (`-q`), and overwriting if it exists (`-o`).

## `kaggle datasets init`

Initializes a new `dataset-metadata.json` file in the specified folder.

**Usage:**

```bash
kaggle datasets init -p <FOLDER_PATH>
```

*   `-p <FOLDER_PATH>`: The path to the folder where the metadata file will be created. Defaults to the current directory.

**Example from `test_commands.sh`:**

```bash
kaggle d init -p tests/dataset
```

**Purpose:** Creates a template `dataset-metadata.json` file in the `tests/dataset` directory. This file is necessary for creating or updating datasets.

## `kaggle datasets create`

Creates a new dataset on Kaggle.

**Usage:**

```bash
kaggle datasets create -p <FOLDER_PATH> [options]
```

*   `-p <FOLDER_PATH>`: Path to the folder containing data files and `dataset-metadata.json`.
*   `-u, --public`: Make the dataset public (default is private).
*   `-q, --quiet`: Suppress progress output.
*   `-t, --keep-tabular`: Do not convert tabular files to CSV.
*   `-r, --dir-mode <MODE>`: How to handle directories (`skip`, `zip`, `tar`). Default is `skip`.

**Example from `test_commands.sh`:**
(Assumes `dataset-metadata.json` has been prepared in `tests/dataset`)
```bash
# Setup: Modify the metadata file (these lines are part of the test script)
# export SLUG=testing
# sed -i s/INSERT_TITLE_HERE/TitleHere/ tests/dataset/dataset-metadata.json
# sed -i s/INSERT_SLUG_HERE/$SLUG/ tests/dataset/dataset-metadata.json

kaggle d create -p tests/dataset --public -q -t -r skip
```

**Purpose:** Creates a new public dataset on Kaggle using the files and metadata found in the `tests/dataset` folder. It suppresses output (`-q`), keeps tabular files as they are (`-t`), and skips any subdirectories (`-r skip`).

## `kaggle datasets version`

Creates a new version of an existing dataset. (Alias: `kaggle datasets update`)

**Usage:**

```bash
kaggle datasets version -p <FOLDER_PATH> -m <VERSION_NOTES> [options]
```

*   `-p <FOLDER_PATH>`: Path to the folder containing data files and `dataset-metadata.json`.
*   `-m, --message <VERSION_NOTES>`: Notes describing the new version (required).
*   `-q, --quiet`: Suppress progress output.
*   `-t, --keep-tabular`: Do not convert tabular files to CSV.
*   `-r, --dir-mode <MODE>`: How to handle directories (`skip`, `zip`, `tar`).
*   `-d, --delete-old-versions`: Delete previous versions of the dataset.

**Example from `test_commands.sh`:**
(Assumes `dataset-metadata.json` in `tests/dataset` points to an existing dataset)
```bash
kaggle d version -m VersionNotesGoHere -p tests/dataset -q -t -r skip -d
```

**Purpose:** Creates a new version of the dataset specified in `tests/dataset/dataset-metadata.json`. It includes "VersionNotesGoHere" as version notes, processes files similarly to `create`, and deletes old versions of the dataset (`-d`).

## `kaggle datasets metadata`

Downloads or updates metadata for a dataset.

**Usage:**

```bash
kaggle datasets metadata <DATASET> [options]
```

*   `<DATASET>`: Dataset slug.
*   `-p <PATH>`: Path to download/update metadata file(s). Defaults to current directory.
*   `--update`: Update existing metadata file(s) with remote values.

**Example from `test_commands.sh`:**

```bash
kaggle datasets metadata goefft/public-datasets-with-file-types-and-columns -p tests/dataset
```

**Purpose:** Downloads the metadata for the dataset 'goefft/public-datasets-with-file-types-and-columns' and saves it into the `tests/dataset` directory. If a `dataset-metadata.json` already exists there for this dataset, it would be overwritten.

## `kaggle datasets status`

Gets the creation/update status of a dataset.

**Usage:**

```bash
kaggle datasets status <DATASET>
```

*   `<DATASET>`: Dataset slug.

**Example from `test_commands.sh`:**

```bash
kaggle d status goefft/public-datasets-with-file-types-and-columns
```

**Purpose:** Checks and displays the current status (e.g., processing, complete, error) of the dataset 'goefft/public-datasets-with-file-types-and-columns'.

## `kaggle datasets delete`

Deletes a dataset from Kaggle.

**Usage:**

```bash
kaggle datasets delete <DATASET> [options]
```

*   `<DATASET>`: Dataset slug to delete.
*   `-y, --yes`: Skip confirmation prompt.

**Examples from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is an environment variable with your username and `$SLUG` is `testing`)
1.  ```bash
    kaggle d delete $KAGGLE_DEVELOPER/$SLUG
    ```
    **Purpose:** Attempts to delete the dataset `$KAGGLE_DEVELOPER/$SLUG`. It will prompt for confirmation.

2.  ```bash
    kaggle d delete $KAGGLE_DEVELOPER/$SLUG --yes
    ```
    **Purpose:** Deletes the dataset `$KAGGLE_DEVELOPER/$SLUG` without prompting for confirmation (`--yes`).
