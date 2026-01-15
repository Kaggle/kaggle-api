# Kaggle CLI Configuration

The Kaggle CLI uses a configuration file to store settings such as your API credentials and default values for commands.

## Configuration Commands

### `config view`

Displays the current configuration values.

**Usage:**

```bash
kaggle config view
```

**Purpose:**

This command allows you to inspect the current settings of your Kaggle CLI, such as the configured API endpoint, proxy settings, and default competition.

### `config set`

Sets a specific configuration value.

**Usage:**

```bash
kaggle config set -n <NAME> -v <VALUE>
```

**Arguments:**

*   `-n, --name <NAME>`: The name of the configuration parameter to set. Valid options are `competition`, `path`, and `proxy`.
*   `-v, --value <VALUE>`: The value to set for the configuration parameter.
    *   For `competition`: The competition URL suffix (e.g., `titanic`).
    *   For `path`: The default folder where files will be downloaded.
    *   For `proxy`: The proxy server URL.

**Example:**

Set the default competition to "titanic":

```bash
kaggle config set -n competition -v titanic
```

**Purpose:**

Use this command to customize the behavior of the Kaggle CLI, such as setting a default competition to avoid specifying it in every command, defining a default download path, or configuring a proxy server.

### `config unset`

Clears a specific configuration value, reverting it to its default.

**Usage:**

```bash
kaggle config unset -n <NAME>
```

**Arguments:**

*   `-n, --name <NAME>`: The name of the configuration parameter to clear. Valid options are `competition`, `path`, and `proxy`.

**Example:**

Clear the default competition:

```bash
kaggle config unset -n competition
```

**Purpose:**

This command removes a previously set configuration value, allowing the CLI to use its default behavior or prompt for the value if required.

## Configuration File Location

The Kaggle CLI configuration is typically stored in a file named `kaggle.json` located in the `~/.kaggle/` directory on Linux and macOS, or `C:\Users\<Windows-username>\.kaggle\` on Windows.

This file contains your API username and key:

```json
{"username":"YOUR_USERNAME","key":"YOUR_API_KEY"}
```

You can download this file from your Kaggle account page (`https://www.kaggle.com/<YOUR_USERNAME>/account`) and place it in the correct directory.

Alternatively, you can set the `KAGGLE_USERNAME` and `KAGGLE_KEY` environment variables.
