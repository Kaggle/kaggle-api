# Models Commands

Commands for interacting with Kaggle Models.

## `kaggle models list`

Lists available models.

**Usage:**

```bash
kaggle models list [options]
```

**Options:**

*   `--owner <OWNER>`: Filter by a specific user or organization.
*   `--sort-by <SORT_BY>`: Sort results. Valid options: `hotness`, `downloadCount`, `voteCount`, `notebookCount`, `createTime` (default: `hotness`).
*   `-s, --search <SEARCH_TERM>`: Search term.
*   `--page-size <SIZE>`: Number of items per page (default: 20).
*   `--page-token <TOKEN>`: Page token for results paging.
*   `-v, --csv`: Print results in CSV format.

**Examples:**

1.  List models owned by `$KAGGLE_DEVELOPER` (replace with your username), sorted by creation time, in CSV format:

    ```bash
    kaggle models list --owner $KAGGLE_DEVELOPER --sort-by createTime -v
    ```

2.  List the first 5 models matching the search term "gemini":

    ```bash
    kaggle models list -s gemini --page-size 5
    ```

**Purpose:**

This command helps you find models on Kaggle, filtering by owner or searching by keywords, and sorting by various criteria.

## `kaggle models init`

Initializes a metadata file (`model-metadata.json`) for creating a new model.

**Usage:**

```bash
kaggle models init -p <FOLDER_PATH>
```

**Options:**

*   `-p, --path <FOLDER_PATH>`: The path to the folder where the `model-metadata.json` file will be created (defaults to the current directory).

**Example:**

Initialize a model metadata file in a new temporary folder `tmp`:

```bash
mkdir tmp
kaggle models init -p tmp
```

**Purpose:**

This command creates a template `model-metadata.json` file. You must edit this file with your model's details, such as owner slug, title, model slug (URL-friendly version of the title), and a description, before creating the model on Kaggle.

## `kaggle models create`

Creates a new model on Kaggle.

**Usage:**

```bash
kaggle models create -p <FOLDER_PATH>
```

**Options:**

*   `-p, --path <FOLDER_PATH>`: Path to the folder containing the `model-metadata.json` file (defaults to the current directory). This folder should also contain your model files that you intend to upload as part of the first model instance.

**Example:**

Create a new model using the metadata in `tmp/model-metadata.json`. (Assumes the metadata file has been edited with owner, title, and slug):

```bash
# Example: Edit model-metadata.json first
# sed -i 's/INSERT_OWNER_SLUG_HERE/your-username/' tmp/model-metadata.json
# sed -i 's/INSERT_TITLE_HERE/My Awesome Model/' tmp/model-metadata.json
# sed -i 's/INSERT_SLUG_HERE/my-awesome-model/' tmp/model-metadata.json

kaggle models create -p tmp
```

**Purpose:**

This command registers a new model on Kaggle using the provided metadata. After this, you will typically create model instances and versions.

## `kaggle models get`

Downloads the `model-metadata.json` file for an existing model.

**Usage:**

```bash
kaggle models get <MODEL> -p <FOLDER_PATH>
```

**Arguments:**

*   `<MODEL>`: Model URL suffix in the format `owner/model-slug` (e.g., `$KAGGLE_DEVELOPER/test-model`).

**Options:**

*   `-p, --path <FOLDER_PATH>`: Folder to download the `model-metadata.json` file to.

**Example:**

Download the metadata for model `$KAGGLE_DEVELOPER/test-model` into the `tmp` folder:

```bash
kaggle models get -p tmp $KAGGLE_DEVELOPER/test-model
```

**Purpose:**

This command retrieves the metadata file for an existing model, which can be useful for inspection or as a basis for an update.

## `kaggle models update`

Updates an existing model on Kaggle using a local `model-metadata.json` file.

**Usage:**

```bash
kaggle models update -p <FOLDER_PATH>
```

**Options:**

*   `-p, --path <FOLDER_PATH>`: Path to the folder containing the `model-metadata.json` file with the updated information (defaults to the current directory).

**Example:**

Update the model whose details are in `tmp/model-metadata.json` (ensure the slug and owner in the JSON match an existing model):

```bash
kaggle models update -p tmp
```

**Purpose:**

Use this command to change the metadata of an existing model, such as its title, description, or other fields defined in the `model-metadata.json` file.

## `kaggle models delete`

Deletes a model from Kaggle.

**Usage:**

```bash
kaggle models delete <MODEL> [options]
```

**Arguments:**

*   `<MODEL>`: Model URL suffix in the format `owner/model-slug` (e.g., `$KAGGLE_DEVELOPER/test-model`).

**Options:**

*   `-y, --yes`: Automatically confirm deletion without prompting.

**Example:**

Delete the model `$KAGGLE_DEVELOPER/test-model` and automatically confirm:

```bash
kaggle models delete $KAGGLE_DEVELOPER/test-model -y
```

**Purpose:**

This command permanently removes one of your models (and all its instances and versions) from Kaggle. Use with caution.
