# Kaggle API

## Installation

Ensure you have Python 3 and the package manager `pip` installed.

Run the following command to access the Kaggle API using the command line:

`pip install kaggle` (You may need to do `pip install --user kaggle` on Mac/Linux.  This is recommended if problems come up during the installation process.) Installations done through the root user (i.e. `sudo pip install kaggle`) will not work correctly unless you understand what you're doing.  Even then, they still might not work.  User installs are strongly recommended in the case of permissions errors.

You can now use the `kaggle` command as shown in the examples below.

If you run into a `kaggle: command not found` error, ensure that your python binaries are on your path.  You can see where `kaggle` is installed by doing `pip uninstall kaggle` and seeing where the binary is.  For a local user install on Linux, the default location is `~/.local/bin`.  On Windows, the default location is `$PYTHON_HOME/Scripts`.

IMPORTANT: We do not offer Python 2 support.  Please ensure that you are using Python 3 before reporting any issues.

## Usage

### Authenticate

To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com. Then go to the 'Account' tab of your user profile (`https://www.kaggle.com/<username>/account`) and select 'Create API Token'. This will trigger the download of `kaggle.json`, a file containing your API credentials. Place this file in the location `~/.kaggle/kaggle.json` (on Windows in the location `C:\Users\<Windows-username>\.kaggle\kaggle.json` - you can check the exact location, sans drive, with `echo %HOMEPATH%`). You can define a shell environment variable `KAGGLE_CONFIG_DIR` to change this location to `$KAGGLE_CONFIG_DIR/kaggle.json` (on Windows it will be `%KAGGLE_CONFIG_DIR%\kaggle.json`).

For your security, ensure that other users of your computer do not have read access to your credentials. On Unix-based systems you can do this with the following command: 

`chmod 600 ~/.kaggle/kaggle.json`

You can also choose to export your Kaggle username and token to the environment:

```bash
export KAGGLE_USERNAME=datadinosaur
export KAGGLE_KEY=xxxxxxxxxxxxxx
```
In addition, you can export any other configuration value that normally would be in
the `$HOME/.kaggle/kaggle.json` in the format 'KAGGLE_<VARIABLE>' (note uppercase).  
For example, if the file had the variable "proxy" you would export `KAGGLE_PROXY`
and it would be discovered by the client.

### Commands

The command line tool supports the following commands:

``` 
kaggle competitions {list, files, download, submit, submissions, leaderboard}
kaggle datasets {list, files, download, create, version, init, metadata, status}
kaggle kernels {list, init, push, pull, output, status}
kaggle models {get, list, init, create, delete, update}
kaggle models instances {get, init, create, delete, update}
kaggle models instances versions {init, create, download, delete}
kaggle models instances {get, init, create, delete, update}
kaggle config {view, set, unset}
```

See more details for using each of these commands in src/README.md

## Development

### Prequisites

We use [hatch](https://hatch.pypa.io) to manage this project.

Follow these [instructions](https://hatch.pypa.io/latest/install/) to install it.

### Tests

```sh
# Run all tests
hatch run test

# Run a single test file
hatch run test tests/test_<SOME_FILE>.py
```

### Integration Tests

To run integration tests on your local machine, you need to set up your Kaggle API credentials. You can do this in one of these two ways described in the earlier sections of this document. Refer to the sections: 
- [Using environment variables](#option-2-read-credentials-from-environment-variables)
- [Using credentials file](#option-3-read-credentials-from-kagglejson)

After setting up your credentials by any of these methods, you can run the integration tests as follows:

```sh
# Run all tests
hatch run integration-test
```


### Run `kagglehub` from source

```sh
# Download a model & print the path
hatch run python -c "import kagglehub; print('path: ', kagglehub.model_download('google/bert/tensorFlow2/answer-equivalence-bem'))"
```

### Lint / Format

```sh
# Lint check
hatch run lint:style
hatch run lint:typing
hatch run lint:all     # for both

# Format
hatch run lint:fmt
```

### Coverage report

```sh
hatch cov
```

### Build

```sh
hatch build
```

### Running `hatch` commands inside Docker

This is useful to run in a consistent environment and easily switch between Python versions.

The following shows how to run `hatch run lint:all` but this also works for any other hatch commands:

```
# Use default Python version
./docker-hatch run lint:all

# Use specific Python version (Must be a valid tag from: https://hub.docker.com/_/python)
./docker-hatch -v 3.9 run lint:all
```
