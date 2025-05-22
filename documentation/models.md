# Models Commands (`kaggle models` or `kaggle m`)

This section describes commands for interacting with Kaggle Models.

## `kaggle models list`

Lists available models.

**Usage:**

```bash
kaggle models list [options]
```

**Options:**

*   `--sort-by <SORT_BY>`: Sort results (e.g., `hotness`, `downloadCount`, `createTime`).
*   `-s, --search <SEARCH_TERM>`: Search term.
*   `--owner <OWNER>`: Filter by owner username or organization.
*   `--page-size <SIZE>`: Number of items per page.
*   `--page-token <TOKEN>`: Page token for pagination.
*   `-v, --csv`: Output in CSV format.

**Examples from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is an environment variable with your username)

1.  ```bash
    kaggle m list --owner $KAGGLE_DEVELOPER --sort-by createTime -v
    ```
    **Purpose:** Lists models owned by `$KAGGLE_DEVELOPER`, sorted by their creation time, and outputs the list in CSV format.

2.  ```bash
    kaggle m list -s gemini --page-size 5
    ```
    **Purpose:** Searches for models with "gemini" in their name or description, displaying 5 results per page.

## `kaggle models init`

Initializes a new `model-metadata.json` file in the specified folder. This file is used for creating or updating models.

**Usage:**

```bash
kaggle models init -p <FOLDER_PATH>
```

*   `-p <FOLDER_PATH>`: The path to the folder where the `model-metadata.json` file will be created. Defaults to the current directory.

**Example from `test_commands.sh`:**

```bash
mkdir tmp
kaggle m init -p tmp
```

**Purpose:** Creates a directory `tmp` and then initializes a template `model-metadata.json` file inside it.

## `kaggle models create`

Creates a new model on Kaggle.

**Usage:**

```bash
kaggle models create -p <FOLDER_PATH>
```

*   `-p <FOLDER_PATH>`: Path to the folder containing the `model-metadata.json` file. Defaults to the current directory. The metadata file must be populated with model details like owner, title, and slug.

**Example from `test_commands.sh`:**
(Assumes `model-metadata.json` has been initialized in `tmp` and modified with necessary details)
```bash
# Setup: Modify the metadata file (these lines are part of the test script)
# sed -i s/INSERT_OWNER_SLUG_HERE/$KAGGLE_DEVELOPER/ tmp/model-metadata.json
# sed -i s/INSERT_TITLE_HERE/ModelTitle/ tmp/model-metadata.json
# sed -i s/INSERT_SLUG_HERE/test-model/ tmp/model-metadata.json

kaggle m create -p tmp
```

**Purpose:** Creates a new model on Kaggle using the information provided in `tmp/model-metadata.json`.

## `kaggle models get`

Downloads the `model-metadata.json` file for an existing model.

**Usage:**

```bash
kaggle models get <MODEL_SLUG> -p <FOLDER_PATH>
```

*   `<MODEL_SLUG>`: Model slug in the format `owner/model-name`.
*   `-p <FOLDER_PATH>`: Path to the folder where the `model-metadata.json` will be saved. Defaults to the current directory.

**Example from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is an environment variable with your username and a model `test-model` exists)
```bash
kaggle m get -p tmp $KAGGLE_DEVELOPER/test-model
```

**Purpose:** Downloads the `model-metadata.json` for the model `$KAGGLE_DEVELOPER/test-model` and saves it into the `tmp` directory.

## `kaggle models update`

Updates an existing model on Kaggle using a local `model-metadata.json` file.

**Usage:**

```bash
kaggle models update -p <FOLDER_PATH>
```

*   `-p <FOLDER_PATH>`: Path to the folder containing the `model-metadata.json` file with updated information. The `id` field in the JSON must point to the existing model to be updated. Defaults to the current directory.

**Example from `test_commands.sh`:**
(Assumes `tmp/model-metadata.json` exists and refers to an existing model owned by `$KAGGLE_DEVELOPER`)
```bash
kaggle m update -p tmp
```

**Purpose:** Updates the model on Kaggle based on the contents of `tmp/model-metadata.json`.

## `kaggle models delete`

Deletes a model from Kaggle.

**Usage:**

```bash
kaggle models delete <MODEL_SLUG> [options]
```

*   `<MODEL_SLUG>`: Model slug to delete (e.g., `owner/model-name`).
*   `-y, --yes`: Skip confirmation prompt.

**Examples from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is an environment variable with your username and a model `test-model` exists)
1.  ```bash
    kaggle m delete $KAGGLE_DEVELOPER/test-model
    ```
    **Purpose:** Attempts to delete the model `$KAGGLE_DEVELOPER/test-model`. It will prompt for confirmation.

2.  ```bash
    kaggle m delete $KAGGLE_DEVELOPER/test-model -y
    ```
    **Purpose:** Deletes the model `$KAGGLE_DEVELOPER/test-model` without prompting for confirmation (`--yes`).

---

For managing model instances and their versions, see:
*   [Models Instances](./models_instances.md)
*   [Models Instances Versions](./models_instances_versions.md)
