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

### Dependencies

```sh
hatch run install-deps
```

### Compile

```sh
hatch run compile
```

The compiled files are generated in the `kaggle/` directory from the `src/` directory.

All the changes must be done in the `src/` directory.

### Run

You can also run the code in python directly:

```sh
hatch run python
```

```python
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.model_list_cli()

Next Page Token = [...]
[...]

```

Or in a single command:

```sh
hatch run python -c "import kaggle; from kaggle.api.kaggle_api_extended import KaggleApi; api = KaggleApi(); api.authenticate(); api.model_list_cli()"
```

### Example

Let's change the `model_list_cli` method in the source file: 

```sh
❯ git diff src/kaggle/api/kaggle_api_extended.py
[...]
+        print('hello Kaggle CLI update')^M
         models = self.model_list(sort_by, search, owner, page_size, page_token)
[...]

❯ hatch run compile
[...]

❯ hatch run python -c "import kaggle; from kaggle.api.kaggle_api_extended import KaggleApi; api = KaggleApi(); api.authenticate(); api.model_list_cli()"
hello Kaggle CLI update
Next Page Token = [...]
```

## License

The Kaggle API is released under the [Apache 2.0 license](LICENSE).
