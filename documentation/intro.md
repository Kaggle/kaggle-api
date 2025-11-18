.. _kaggle:

# Kaggle CLI Documentation

Welcome to the Kaggle CLI documentation. This guide provides detailed information on how to use the Kaggle command-line interface to interact with Kaggle's platform.

## Getting Started

Before you begin, ensure you have the Kaggle CLI installed and configured with your API credentials. You can find your API token on your Kaggle account page.

### Installation

Ensure you have Python 3 and the package manager `pip` installed.

Run the following command to access the Kaggle API using the command line:

`pip install kaggle`
(You may need to do `pip install --user kaggle` on Mac/Linux.  This is recommended if problems come up during the installation process.)
Installations done through the root user (i.e. `sudo pip install kaggle`) will not work correctly unless you understand what you're doing.  Even then, they still might not work.  User installs are strongly recommended in the case of permissions errors.

You can now use the `kaggle` command as shown in the examples below.

If you run into a `kaggle: command not found` error, ensure that your python binaries are on your path.  You can see where `kaggle` is installed by doing `pip uninstall kaggle` and seeing where the binary is (then cancel the uninstall when prompted).  For a local user install on Linux, the default location is `~/.local/bin`.  On Windows, the default location is `$PYTHON_HOME/Scripts`.

IMPORTANT: We do not offer Python 2 support.  Please ensure that you are using Python 3 before reporting any issues.

### API credentials

To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com. Then go to the 'Account' tab of your user profile (`https://www.kaggle.com/<username>/account`) and select 'Generate New Token'.

You can export your Kaggle username and token to the environment:

```bash
export KAGGLE_USERNAME=datadinosaur
export KAGGLE_API_TOKEN=xxxxxxxxxxxxxx
```

## Tutorials

Explore these tutorials to learn how to perform common tasks:

*   [Tutorials](./tutorials.md)
    *   [Create a Dataset](./tutorials.md#tutorial-create-a-dataset)
    *   [Find and Download a Dataset](./tutorials.md#tutorial-find-and-download-a-dataset)
    *   [Create a Model](./tutorials.md#tutorial-create-a-model)
    *   [Create a Model Variation](./tutorials.md#tutorial-create-a-model-variation)
    *   [Create a Model Variation Version](./tutorials.md#tutorial-create-a-model-variation-version)
    *   [How to Submit to a Competition](./tutorials.md#tutorial-how-to-submit-to-a-competition)
    *   [How to Submit to a Code Competition](./tutorials.md#tutorial-how-to-submit-to-a-code-competition)

## CLI Reference

The Kaggle CLI is organized into several command groups:

*   [Competitions](./competitions.md): Manage and participate in Kaggle competitions.
*   [Datasets](./datasets.md): Search, download, and manage Kaggle datasets.
*   [Kernels](./kernels.md): Interact with Kaggle Kernels (notebooks and scripts).
*   [Models](./models.md): Manage your Kaggle Models.
*   [Model Variations](./model_instances.md): Manage variations of your Kaggle Models.
*   [Model Variation Versions](./model_instances_versions.md): Manage versions of your Kaggle Model Variations.
*   [Configuration](./configuration.md): Configure the Kaggle CLI.

## Python API Reference

The Kaggle CLI provides a Python API for interacting with Kaggle's platform. You can access the API using the `kaggle` module:

```python
import kaggle
```

For more information about the Python API, see the
<a href="./source/kaggle.api.html" target="_blank" rel="alternate">Kaggle Python API documentation</a>.