# Model Instances Commands

Commands for interacting with instances of Kaggle Models. A model instance typically represents a specific framework or variation of a parent model.

## `kaggle models instances init`

Initializes a metadata file (`model-instance-metadata.json`) for creating a new model instance.

**Usage:**

```bash
kaggle models instances init -p <FOLDER_PATH>
```

**Options:**

*   `-p, --path <FOLDER_PATH>`: The path to the folder where the `model-instance-metadata.json` file will be created (defaults to the current directory).

**Example:**

Initialize a model instance metadata file in the `tmp` folder:

```bash
kaggle models instances init -p tmp
```

**Purpose:**

This command creates a template `model-instance-metadata.json` file. You must edit this file with details such as the owner slug, the parent model slug, the instance slug (URL-friendly name for this instance), and the framework (e.g., `tensorflow`, `pytorch`, `jax`, `sklearn`) before creating the instance.

## `kaggle models instances create`

Creates a new model instance under an existing model on Kaggle.

**Usage:**

```bash
kaggle models instances create -p <FOLDER_PATH> [options]
```

**Options:**

*   `-p, --path <FOLDER_PATH>`: Path to the folder containing the model instance files and the `model-instance-metadata.json` file (defaults to the current directory).
*   `-q, --quiet`: Suppress verbose output.
*   `-r, --dir-mode <MODE>`: How to handle directories within the upload: `skip` (ignore), `zip` (compressed upload), `tar` (uncompressed upload) (default: `skip`).

**Example:**

Create a new model instance using the metadata and files in the `tmp` folder, quietly, skipping subdirectories. (Assumes `model-instance-metadata.json` in `tmp` has been properly edited):

```bash
# Example: Edit model-instance-metadata.json first
# sed -i 's/INSERT_OWNER_SLUG_HERE/your-username/' tmp/model-instance-metadata.json
# sed -i 's/INSERT_EXISTING_MODEL_SLUG_HERE/parent-model-slug/' tmp/model-instance-metadata.json
# sed -i 's/INSERT_INSTANCE_SLUG_HERE/my-instance-slug/' tmp/model-instance-metadata.json
# sed -i 's/INSERT_FRAMEWORK_HERE/jax/' tmp/model-instance-metadata.json
# echo "a,b,c,d" > tmp/data.csv # Example model file

kaggle models instances create -p tmp -q -r skip
```

**Purpose:**

This command uploads your local model files (e.g., weights, architecture definition) and the associated instance metadata to create a new instance under a specified parent model on Kaggle. This effectively creates the first version of this model instance.

## `kaggle models instances get`

Downloads the `model-instance-metadata.json` file for an existing model instance.

**Usage:**

```bash
kaggle models instances get <MODEL_INSTANCE> -p <FOLDER_PATH>
```

**Arguments:**

*   `<MODEL_INSTANCE>`: Model instance URL suffix in the format `owner/model-slug/framework/instance-slug` (e.g., `$KAGGLE_DEVELOPER/test-model/jax/main`).

**Options:**

*   `-p, --path <FOLDER_PATH>`: Folder to download the `model-instance-metadata.json` file to.

**Example:**

Download the metadata for model instance `$KAGGLE_DEVELOPER/test-model/jax/main` into the `tmp` folder:

```bash
kaggle models instances get $KAGGLE_DEVELOPER/test-model/jax/main -p tmp
```

**Purpose:**

This command retrieves the metadata file for an existing model instance. This can be useful for inspection or as a basis for an update.

## `kaggle models instances files`

Lists files for the current version of a model instance.

**Usage:**

```bash
kaggle models instances files <MODEL_INSTANCE> [options]
```

**Arguments:**

*   `<MODEL_INSTANCE>`: Model instance URL suffix (e.g., `$KAGGLE_DEVELOPER/test-model/jax/main`).

**Options:**

*   `-v, --csv`: Print results in CSV format.
*   `--page-size <SIZE>`: Number of items per page (default: 20).
*   `--page-token <TOKEN>`: Page token for results paging.

**Example:**

List the first 5 files for the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` in CSV format:

```bash
kaggle models instances files $KAGGLE_DEVELOPER/test-model/jax/main -v --page-size 5
```

**Purpose:**

Use this command to see the files associated with the latest version of a specific model instance.

## `kaggle models instances update`

Updates an existing model instance on Kaggle using a local `model-instance-metadata.json` file.

**Usage:**

```bash
kaggle models instances update -p <FOLDER_PATH>
```

**Options:**

*   `-p, --path <FOLDER_PATH>`: Path to the folder containing the `model-instance-metadata.json` file with the updated information (defaults to the current directory). Note: This command only updates the metadata of the instance, not the files. To update files, create a new version.

**Example:**

Update the model instance whose details are in `tmp/model-instance-metadata.json` (ensure the slugs and owner in the JSON match an existing model instance):

```bash
kaggle models instances update -p tmp
```

**Purpose:**

Use this command to change the metadata of an existing model instance, such as its description or other fields defined in the `model-instance-metadata.json` file. This does not upload new files or create a new version.

## `kaggle models instances delete`

Deletes a model instance from Kaggle.

**Usage:**

```bash
kaggle models instances delete <MODEL_INSTANCE> [options]
```

**Arguments:**

*   `<MODEL_INSTANCE>`: Model instance URL suffix in the format `owner/model-slug/framework/instance-slug` (e.g., `$KAGGLE_DEVELOPER/test-model/jax/main`).

**Options:**

*   `-y, --yes`: Automatically confirm deletion without prompting.

**Example:**

Delete the model instance `$KAGGLE_DEVELOPER/test-model/jax/main` and automatically confirm:

```bash
kaggle models instances delete $KAGGLE_DEVELOPER/test-model/jax/main -y
```

**Purpose:**

This command permanently removes one of your model instances (and all its versions) from Kaggle. Use with caution.
