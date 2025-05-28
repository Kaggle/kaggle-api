ABOUTME: This file documents the Kaggle CLI commands for model instance versions.
ABOUTME: It covers creating, downloading, listing files for, and deleting model instance versions.

# Model Instance Versions Commands

Commands for managing versions of a specific Kaggle Model Instance. Each version represents a snapshot of the model instance files at a point in time.

## `kaggle models instances versions create`

Creates a new version of an existing model instance.

**Usage:**

```bash
kaggle models instances versions create <MODEL_INSTANCE> -p <FOLDER_PATH> [options]
```

**Arguments:**

*   `<MODEL_INSTANCE>`: The target model instance URL suffix for the new version (format: `owner/model-slug/framework/instance-slug`, e.g., `$KAGGLE_DEVELOPER/test-model/jax/main`).

**Options:**

*   `-p, --path <FOLDER_PATH>`: Path to the folder containing the files for this new version (defaults to the current directory).
*   `-n, --version-notes <NOTES>`: Notes describing this version.
*   `-q, --quiet`: Suppress verbose output.
*   `-r, --dir-mode <MODE>`: How to handle directories within the upload: `skip` (ignore), `zip` (compressed upload), `tar` (uncompressed upload) (default: `skip`).

**Example:**

Create a new version for the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` using files from the `tmp` folder, with version notes "Updated model files", quietly, and skipping subdirectories:

```bash
# Ensure tmp folder contains the new files for the version, e.g., data_v2.csv
# echo "e,f,g,h" > tmp/data_v2.csv

kaggle models instances versions create $KAGGLE_DEVELOPER/test-model/jax/main -p tmp -n "Updated model files" -q -r skip
```

**Purpose:**

This command uploads a new set of files to an existing model instance, creating a new, numbered version. This allows you to track changes and revert to previous versions of your model instance files.

## `kaggle models instances versions download`

Downloads files for a specific version of a model instance.

**Usage:**

```bash
kaggle models instances versions download <MODEL_INSTANCE_VERSION> [options]
```

**Arguments:**

*   `<MODEL_INSTANCE_VERSION>`: Model instance version URL suffix in the format `owner/model-slug/framework/instance-slug/version-number` (e.g., `$KAGGLE_DEVELOPER/test-model/jax/main/1`).

**Options:**

*   `-p, --path <PATH>`: Folder to download files to (defaults to current directory).
*   `--untar`: Untar the downloaded file if it's a `.tar` archive (deletes the `.tar` file afterwards).
*   `--unzip`: Unzip the downloaded file if it's a `.zip` archive (deletes the `.zip` file afterwards).
*   `-f, --force`: Force download, overwriting existing files.
*   `-q, --quiet`: Suppress verbose output.

**Example:**

Download version 1 of the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` into the `tmp` folder, untar if applicable, force overwrite, and do it quietly:

```bash
kaggle models instances versions download $KAGGLE_DEVELOPER/test-model/jax/main/1 -p tmp -q -f --untar
```

**Purpose:**

This command allows you to retrieve the specific files associated with a particular version of a model instance.

## `kaggle models instances versions files`

Lists files for a specific version of a model instance.

**Usage:**

```bash
kaggle models instances versions files <MODEL_INSTANCE_VERSION> [options]
```

**Arguments:**

*   `<MODEL_INSTANCE_VERSION>`: Model instance version URL suffix (e.g., `google/gemma/pytorch/7b/2`).

**Options:**

*   `-v, --csv`: Print results in CSV format.
*   `--page-size <SIZE>`: Number of items per page (default: 20).
*   `--page-token <TOKEN>`: Page token for results paging.

**Example:**

List the first 3 files for version 2 of the model instance `google/gemma/pytorch/7b` in CSV format:

```bash
kaggle models instances versions files google/gemma/pytorch/7b/2 -v --page-size=3
```

**Purpose:**

Use this command to see the individual files that constitute a specific version of a model instance before downloading.

## `kaggle models instances versions delete`

Deletes a specific version of a model instance from Kaggle.

**Usage:**

```bash
kaggle models instances versions delete <MODEL_INSTANCE_VERSION> [options]
```

**Arguments:**

*   `<MODEL_INSTANCE_VERSION>`: Model instance version URL suffix in the format `owner/model-slug/framework/instance-slug/version-number` (e.g., `$KAGGLE_DEVELOPER/test-model/jax/main/1`).

**Options:**

*   `-y, --yes`: Automatically confirm deletion without prompting.

**Example:**

Delete version 1 of the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` and automatically confirm:

```bash
kaggle models instances versions delete $KAGGLE_DEVELOPER/test-model/jax/main/1 -y
```

**Purpose:**

This command permanently removes a specific version of your model instance from Kaggle. Use with caution. If it's the only version, this may lead to the deletion of the model instance itself if no other versions exist.
