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

### Prequisites

We use [hatch](https://hatch.pypa.io) to manage this project.

Follow these [instructions](https://hatch.pypa.io/latest/install/) to install it.

### Dependencies

```sh
hatch run install-deps
```

### Compile

```sh
hatch run compile
```

The compiled files are generated in the 'kaggle/' directory and the root directory of this repository.

## License

The Kaggle API is released under the [Apache 2.0 license](LICENSE).
