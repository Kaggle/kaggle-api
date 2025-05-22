# Configuration

The Kaggle CLI requires authentication to interact with your Kaggle account.

## Authentication

Authentication is typically handled by placing a `kaggle.json` file in your `~/.kaggle/` directory. This file contains your API username and key.

You can download this file from your Kaggle account page: `https://www.kaggle.com/<YOUR-USERNAME>/account` (scroll to the API section).

The `kaggle.json` file should look like this:

```json
{"username":"YOUR_USERNAME","key":"YOUR_API_KEY"}
```

Ensure this file has appropriate permissions (e.g., `600`) to protect your API key.

## Environment Variables

Alternatively, you can set the following environment variables:

*   `KAGGLE_USERNAME`: Your Kaggle username.
*   `KAGGLE_KEY`: Your Kaggle API key.

## Configuration Commands

The `kaggle config` command group allows you to view and manage CLI configuration settings.

### `kaggle config view`

Displays the current configuration values.

**Example:**

```bash
kaggle config view
```

**Purpose:** To check the current settings for parameters like the default download path, competition, or proxy.

### `kaggle config set`

Sets a specific configuration value.

**Usage:**

```bash
kaggle config set -n <NAME> -v <VALUE>
```

*   `-n <NAME>`: The name of the configuration parameter (e.g., `competition`, `path`, `proxy`).
*   `-v <VALUE>`: The value to set for the parameter.

**Example:**

```bash
kaggle config set -n competition -v titanic
```

**Purpose:** To set a default competition, download path, or proxy server. For instance, setting `competition` to `titanic` means subsequent competition-specific commands (like `kaggle competitions files`) will default to the `titanic` competition if not otherwise specified.

### `kaggle config unset`

Clears a specific configuration value, reverting it to its default.

**Usage:**

```bash
kaggle config unset -n <NAME>
```

*   `-n <NAME>`: The name of the configuration parameter to clear (e.g., `competition`, `path`, `proxy`).

**Example:**

```bash
kaggle config unset -n competition
```

**Purpose:** To remove a previously set configuration value, such as a default competition or proxy.
