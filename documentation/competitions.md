# Competitions Commands (`kaggle competitions` or `kaggle c`)

This section describes commands for interacting with Kaggle competitions.

## `kaggle competitions list`

Lists available competitions.

**Usage:**

```bash
kaggle competitions list [options]
```

**Options:**

*   `--group <GROUP>`: Filter by group (e.g., `general`, `entered`, `inClass`).
*   `--category <CATEGORY>`: Filter by category (e.g., `featured`, `research`).
*   `--sort-by <SORT_BY>`: Sort results (e.g., `prize`, `latestDeadline`).
*   `-p, --page <PAGE>`: Page number for results.
*   `-s, --search <SEARCH_TERM>`: Search term.
*   `-v, --csv`: Output in CSV format.

**Example from `test_commands.sh`:**

```bash
kaggle competitions list --group general --category featured --sort-by prize
```

**Purpose:** This command lists competitions, filtered to show only 'featured' competitions in the 'general' group, sorted by the prize amount. It helps users discover relevant competitions.

## `kaggle competitions files`

Lists files for a specific competition.

**Usage:**

```bash
kaggle competitions files <COMPETITION> [options]
```

*   `<COMPETITION>`: The competition URL suffix (e.g., `titanic`).
*   `-v, --csv`: Output in CSV format.
*   `-q, --quiet`: Suppress progress output.
*   `--page-size <SIZE>`: Number of items per page.
*   `--page-token <TOKEN>`: Page token for pagination.

**Example from `test_commands.sh`:**

```bash
kaggle competitions files titanic --page-size=3 --page-token=abcd -v -q
```

**Purpose:** This command lists the files available for the 'titanic' competition. It displays 3 files per page, uses 'abcd' as a page token (likely for testing pagination), outputs in CSV format (`-v`), and suppresses progress messages (`-q`). This is useful for understanding the data provided for a competition.

## `kaggle competitions download`

Downloads competition files.

**Usage:**

```bash
kaggle competitions download <COMPETITION> [options]
```

*   `<COMPETITION>`: The competition URL suffix.
*   `-f, --file <FILE_NAME>`: Specific file to download.
*   `-p, --path <PATH>`: Path to download files to.
*   `-w, --wp`: Download to current working path.
*   `-o, --force`: Force download, overwriting existing files.
*   `-q, --quiet`: Suppress progress output.

**Examples from `test_commands.sh`:**

1.  ```bash
    kaggle c download titanic -w -o -q
    ```
    **Purpose:** Downloads all files for the 'titanic' competition to the current working directory (`-w`), overwrites existing files (`-o`), and does so quietly (`-q`).

2.  ```bash
    kaggle c download titanic -f test.csv -p tost
    ```
    **Purpose:** Downloads only the `test.csv` file from the 'titanic' competition into a directory named `tost`.

## `kaggle competitions submit`

Submits a prediction file to a competition.

**Usage:**

```bash
kaggle competitions submit <COMPETITION> -f <FILE_PATH> -m <MESSAGE> [options]
```

*   `<COMPETITION>`: The competition URL suffix.
*   `-f, --file <FILE_PATH>`: Path to the submission file.
*   `-m, --message <MESSAGE>`: Message describing the submission.
*   `-k, --kernel <KERNEL_SLUG>`: Kernel to submit from.
*   `-v, --version <VERSION>`: Kernel version to submit.
*   `-q, --quiet`: Suppress progress output.

**Example from `test_commands.sh`:**

```bash
# First, download a sample submission file (setup for the test)
kaggle c download house-prices-advanced-regression-techniques -f sample_submission.csv

# Then, submit it
kaggle c submit house-prices-advanced-regression-techniques -f sample_submission.csv -m "Test message"
```

**Purpose:** This sequence first downloads `sample_submission.csv` for the 'house-prices-advanced-regression-techniques' competition. Then, it submits this file with the message "Test message". This illustrates how to make a submission to a competition.

## `kaggle competitions submissions`

Lists your past submissions for a competition.

**Usage:**

```bash
kaggle competitions submissions <COMPETITION> [options]
```

*   `<COMPETITION>`: The competition URL suffix.
*   `-v, --csv`: Output in CSV format.
*   `-q, --quiet`: Suppress progress output.

**Example from `test_commands.sh`:**

```bash
kaggle c submissions house-prices-advanced-regression-techniques -v -q
```

**Purpose:** This command lists all your previous submissions for the 'house-prices-advanced-regression-techniques' competition, displaying the output in CSV format (`-v`) and suppressing progress messages (`-q`). It's useful for tracking your submission history and scores.

## `kaggle competitions leaderboard`

View or download the competition leaderboard.

**Usage:**

```bash
kaggle competitions leaderboard <COMPETITION> [options]
```

*   `<COMPETITION>`: The competition URL suffix.
*   `-s, --show`: Show the top of the leaderboard in the console.
*   `-d, --download`: Download the entire leaderboard as a CSV.
*   `-p, --path <PATH>`: Path to download the leaderboard to (if `-d` is used).
*   `-v, --csv`: Output in CSV format (used with `-s`).
*   `-q, --quiet`: Suppress progress output.

**Examples from `test_commands.sh`:**

1.  ```bash
    kaggle c leaderboard titanic -v -q -d -p leaders
    ```
    **Purpose:** Downloads the entire leaderboard for the 'titanic' competition into a directory named `leaders`. The `-v` likely ensures CSV format for the downloaded file, and `-q` suppresses output.

2.  ```bash
    kaggle c leaderboard titanic -s > leaderboard.txt
    ```
    **Purpose:** Shows the top of the 'titanic' competition leaderboard (`-s`) and redirects the output to a file named `leaderboard.txt`. This is useful for a quick view of the top rankings.
