# Other Commands

This section covers miscellaneous commands not fitting into the main categories.

## Files (`kaggle files` or `kaggle f`)

### `kaggle files upload`

Uploads one or more local files to a Kaggle inbox path. This is a more generic file upload mechanism compared to dataset or model-specific uploads.

**Usage:**

```bash
kaggle files upload <LOCAL_PATH_1> [<LOCAL_PATH_2> ...] [options]
```

**Options:**

*   `-i, --inbox-path <INBOX_PATH>`: Virtual path on the server where files will be stored (e.g., a temporary location for further processing or linking). Defaults to an empty path, meaning files are uploaded to a root or default inbox location.
*   `local_paths`: One or more paths to local files or directories to upload. Directories are zipped by default.
*   `--no-resume`: Disable resumable uploads.
*   `--no-compress`: If uploading directories, use TAR instead of ZIP (uploads uncompressed).

**Note:** The `test_commands.sh` script does not currently contain direct examples for `kaggle files upload`.

**Conceptual Example:**

```bash
# Create some dummy files
echo "content1" > file1.txt
mkdir my_data
echo "content2" > my_data/file2.txt

# Upload file1.txt and the my_data directory (which will be zipped to my_data.zip)
# to a virtual server path "project_alpha/raw_data"
kaggle files upload file1.txt my_data -i "project_alpha/raw_data"

# Upload without compressing the directory
kaggle files upload my_data -i "project_alpha/uncompressed" --no-compress

# Clean up dummy files
rm file1.txt
rm -r my_data
```

**Purpose:** To upload arbitrary files or directories to a specified location in your Kaggle inbox. This can be useful for staging data, sharing temporary files, or for workflows where files are not yet part of a formal dataset or model structure.

## Version

### `kaggle --version` or `kaggle -v`

Prints the installed Kaggle API version.

**Example from `test_commands.sh`:**

```bash
kaggle --version
```

**Purpose:** To check the current version of the Kaggle CLI tool. This is useful for debugging, ensuring compatibility, or checking if an update is needed.
