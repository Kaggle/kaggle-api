# Models Instances Versions Commands (`kaggle models instances versions` or `kaggle miv`)

This section describes commands for managing specific versions of Kaggle Model Instances.

## `kaggle models instances versions create`

Creates a new version of an existing model instance.

**Usage:**

```bash
kaggle models instances versions create <MODEL_INSTANCE_SLUG> -p <FOLDER_PATH> [options]
```

*   `<MODEL_INSTANCE_SLUG>`: The slug of the model instance to version (e.g., `owner/model-name/framework/instance-slug`).
*   `-p <FOLDER_PATH>`: Path to the folder containing the files for this new version. Defaults to the current working directory.
*   `-n, --version-notes <NOTES>`: Notes describing this version.
*   `-q, --quiet`: Suppress progress output.
*   `-r, --dir-mode <MODE>`: How to handle directories containing instance files (`skip`, `zip`, `tar`). Default is `skip`.

**Example from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is set, the model instance `test-model/jax/main` exists, and `tmp` contains files for the new version)
```bash
kaggle models instances versions create -p tmp -q -r skip -n VersionNotes $KAGGLE_DEVELOPER/test-model/jax/main
```

**Purpose:** Creates a new version for the model instance `$KAGGLE_DEVELOPER/test-model/jax/main`. It uploads files from the `tmp` directory, adds "VersionNotes" as the version description, operates quietly (`-q`), and skips subdirectories (`-r skip`).

## `kaggle models instances versions files`

Lists files for a specific version of a model instance.

**Usage:**

```bash
kaggle models instances versions files <MODEL_INSTANCE_VERSION_SLUG> [options]
```

*   `<MODEL_INSTANCE_VERSION_SLUG>`: Model instance version slug (e.g., `owner/model-name/framework/instance-slug/version-number`).
*   `-v, --csv`: Output in CSV format.
*   `--page-size <SIZE>`: Number of items per page.
*   `--page-token <TOKEN>`: Page token for pagination.

**Example from `test_commands.sh`:**

```bash
kaggle models instances versions files google/gemma/pytorch/7b/2 -v --page-size=3 --page-token=abcd
```

**Purpose:** Lists the files associated with version 2 of the 'google/gemma/pytorch/7b' model instance. It outputs in CSV format (`-v`), shows 3 files per page, and uses 'abcd' as a page token (likely for testing pagination).

## `kaggle models instances versions download`

Downloads files for a specific version of a model instance.

**Usage:**

```bash
kaggle models instances versions download <MODEL_INSTANCE_VERSION_SLUG> [options]
```

*   `<MODEL_INSTANCE_VERSION_SLUG>`: Model instance version slug (e.g., `owner/model-name/framework/instance-slug/version-number`).
*   `-p, --path <PATH>`: Path to download files to. Defaults to current working directory.
*   `--untar`: Untar the downloaded file (if it's a tar archive).
*   `-f, --force`: Force download, overwriting existing files.
*   `-q, --quiet`: Suppress progress output.

**Example from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is set and the specified model instance version exists)
```bash
kaggle models instances versions download -p tmp -q -f --untar $KAGGLE_DEVELOPER/test-model/jax/main/1
```

**Purpose:** Downloads the files for version 1 of the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` into the `tmp` directory. It does this quietly (`-q`), forces overwrite (`-f`), and attempts to untar the downloaded content (`--untar`).

## `kaggle models instances versions delete`

Deletes a specific version of a model instance from Kaggle.

**Usage:**

```bash
kaggle models instances versions delete <MODEL_INSTANCE_VERSION_SLUG> [options]
```

*   `<MODEL_INSTANCE_VERSION_SLUG>`: Model instance version slug to delete (e.g., `owner/model-name/framework/instance-slug/version-number`).
*   `-y, --yes`: Skip confirmation prompt.

**Examples from `test_commands.sh`:**
(Assumes `$KAGGLE_DEVELOPER` is set and the specified model instance version exists)
1.  ```bash
    kaggle m instances versions delete $KAGGLE_DEVELOPER/test-model/jax/main/1
    ```
    **Purpose:** Attempts to delete version 1 of the model instance `$KAGGLE_DEVELOPER/test-model/jax/main`. It will prompt for confirmation.

2.  ```bash
    kaggle m instances versions delete $KAGGLE_DEVELOPER/test-model/jax/main/1 -y
    ```
    **Purpose:** Deletes version 1 of the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` without prompting for confirmation (`--yes`).

---

*   Back to [Models Instances](./models_instances.md)
*   Back to [Models](./models.md)
