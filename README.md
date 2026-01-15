# Kaggle API

Official API for https://www.kaggle.com, accessible using a command line tool implemented in Python 3.  

[User documentation](docs/README.md)

## Installation

Ensure you have Python 3 and the package manager `pip` installed.

Run the following command to access the Kaggle API using the command line:

```sh
pip install kaggle
```

## Development

### Prerequisites

We use [hatch](https://hatch.pypa.io) to manage this project.

Follow these [instructions](https://hatch.pypa.io/latest/install/) to install it.

### Run `kaggle` from source

#### Option 1: Execute a one-liner of code from the command line

```sh
hatch run kaggle datasets list
```

#### Option 2: Run many commands in a shell

```sh
hatch shell

# Inside the shell, you can run many commands
kaggle datasets list
kaggle competitions list
...
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

### Tests

Note: These tests are not true unit tests and are calling the Kaggle web server.

```sh
# Run against kaggle.com
hatch run test:prod

# Run against a local web server (Kaggle engineers only)
hatch run test:local
```

### Integration Tests

To run integration tests on your local machine, you need to set up your Kaggle API credentials. You can do this in one of these two ways described [this doc](docs/README.md). Refer to the sections: 
- Using environment variables
- Using credentials file

After setting up your credentials by any of these methods, you can run the integration tests as follows:

```sh
hatch run test:integration
```

## License

The Kaggle API is released under the [Apache 2.0 license](LICENSE).
