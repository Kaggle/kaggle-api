# Models Instances Commands (`kaggle models instances` or `kaggle mi`)

This section describes commands for managing specific instances of Kaggle Models (e.g., a particular framework version like TensorFlow or PyTorch).

## `kaggle models instances init`

Initializes a new `model-instance-metadata.json` file in the specified folder. This file is used for creating or updating model instances.

**Usage:**

```bash
kaggle models instances init -p <FOLDER_PATH>
```

*   `-p <FOLDER_PATH>`: The path to the folder where the `model-instance-metadata.json` file will be created. Defaults to the current directory.

**Example from `test_commands.sh`:**
(Assumes `tmp` directory exists)
```bash
kaggle m instances init -p tmp
```

**Purpose:** Creates a template `model-instance-metadata.json` file inside the `tmp` directory. This file needs to be populated with details about the model instance, such as the parent model, instance slug, and framework.

## `kaggle models instances create`

Creates a new model instance under an existing model on Kaggle.

**Usage:**

```bash
kaggle models instances create -p <FOLDER_PATH> [options]
```

*   `-p <FOLDER_PATH>`: Path to the folder containing the `model-instance-metadata.json` file and any instance files. Defaults to the current directory.
*   `-q, --quiet`: Suppress progress output.
*   `-r, --dir-mode <MODE>`: How to handle directories containing instance files (`skip`, `zip`, `tar`). Default is `skip`.

**Example from `test_commands.sh`:**
(Assumes `model-instance-metadata.json` has been initialized in `tmp` and modified with necessary details, and `data.csv` exists in `tmp`)
```bash
# Setup: Modify the metadata file and create a dummy data file (lines from test script)
# sed -i s/INSERT_OWNER_SLUG_HERE/$KAGGLE_DEVELOPER/ tmp/model-instance-metadata.json
# sed -i s/INSERT_EXISTING_MODEL_SLUG_HERE/test-model/ tmp/model-instance-metadata.json
# sed -i s/INSERT_INSTANCE_SLUG_HERE/main/ tmp/model-instance-metadata.json
# sed -i s/INSERT_FRAMEWORK_HERE/jax/ tmp/model-instance-metadata.json
# echo "a,b,c,d" > tmp/data.csv

kaggle models instances create -p tmp -q -r skip
```

**Purpose:** Creates a new model instance for the model `test-model` (owned by `$KAGGLE_DEVELOPER`) with framework `jax` and instance slug `main`. It uses the metadata from `tmp/model-instance-metadata.json` and uploads files from the `tmp` directory (like `data.csv`). It operates quietly (`-q`) and skips subdirectories (`-r skip`).

## `kaggle models instances get`

Downloads the `model-instance-metadata.json` file for an existing model instance.

**Usage:**

```bash
kaggle models instances get <MODEL_INSTANCE_SLUG> -p <FOLDER_PATH>
```

*   `<MODEL_INSTANCE_SLUG>`: Model instance slug in the format `owner/model-name/framework/instance-slug`.
*   `-p <FOLDER_PATH>`: Path to the folder where the `model-instance-metadata.json` will be saved. Defaults to the current directory.

**Example from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is set and the specified model instance exists)
```bash
kaggle models instances get $KAGGLE_DEVELOPER/test-model/jax/main -p tmp
```

**Purpose:** Downloads the `model-instance-metadata.json` for the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` and saves it into the `tmp` directory.

## `kaggle models instances files`

Lists files for the current version of a model instance.

**Usage:**

```bash
kaggle models instances files <MODEL_INSTANCE_SLUG> [options]
```

*   `<MODEL_INSTANCE_SLUG>`: Model instance slug (e.g., `owner/model-name/framework/instance-slug`).
*   `-v, --csv`: Output in CSV format.
*   `--page-size <SIZE>`: Number of items per page.
*   `--page-token <TOKEN>`: Page token for pagination.

**Example from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is set and the specified model instance exists)
```bash
kaggle models instances files $KAGGLE_DEVELOPER/test-model/jax/main -v --page-size 5
```

**Purpose:** Lists the files associated with the latest version of the model instance `$KAGGLE_DEVELOPER/test-model/jax/main`. It outputs in CSV format (`-v`) and shows 5 files per page.

## `kaggle models instances update`

Updates an existing model instance on Kaggle using a local `model-instance-metadata.json` file and any associated instance files.

**Usage:**

```bash
kaggle models instances update -p <FOLDER_PATH>
```

*   `-p <FOLDER_PATH>`: Path to the folder containing the `model-instance-metadata.json` file (with the `instanceId` of the instance to update) and any new/updated instance files. Defaults to the current directory.

**Example from `test_commands.sh`:**
(Assumes `tmp/model-instance-metadata.json` exists and refers to an existing model instance)
```bash
kaggle models instances update -p tmp
```

**Purpose:** Updates the model instance on Kaggle based on the contents of `tmp/model-instance-metadata.json` and any files in the `tmp` directory. This typically creates a new version of the model instance.

## `kaggle models instances delete`

Deletes a model instance from Kaggle. This will delete all versions of the instance.

**Usage:**

```bash
kaggle models instances delete <MODEL_INSTANCE_SLUG> [options]
```

*   `<MODEL_INSTANCE_SLUG>`: Model instance slug to delete (e.g., `owner/model-name/framework/instance-slug`).
*   `-y, --yes`: Skip confirmation prompt.

**Examples from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is set and the specified model instance exists)
1.  ```bash
    kaggle m instances delete $KAGGLE_DEVELOPER/test-model/jax/main
    ```
    **Purpose:** Attempts to delete the model instance `$KAGGLE_DEVELOPER/test-model/jax/main`. It will prompt for confirmation.

2.  ```bash
    kaggle m instances delete $KAGGLE_DEVELOPER/test-model/jax/main -y
    ```
    **Purpose:** Deletes the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` without prompting for confirmation (`--yes`).

---

For managing specific versions of model instances, see:
*   [Models Instances Versions](./models_instances_versions.md)
