# Kaggle CLI Tutorials

These tutorials illustrate how to use a sequence of Kaggle CLI commands to accomplish common tasks.

## Introduction

Before starting these tutorials, please make sure you have:

1.  Installed the Kaggle CLI.
2.  Downloaded your `kaggle.json` API token from your Kaggle account page (e.g., `https://www.kaggle.com/settings`) and placed it in the `~/.kaggle/` directory (or `C:\Users\<Windows-username>\.kaggle\` on Windows).
3.  Logged in to your kaggle.com account in a web browser. This will allow you to easily verify the results of the CLI commands in the "Your Work" section of your Kaggle profile.

## Tutorial: Create a Dataset

This tutorial walks you through creating a new dataset on Kaggle.

1.  **Start from an empty directory.** Create a new directory for your dataset files and navigate into it.

    ```bash
    mkdir my-new-dataset
    cd my-new-dataset
    ```

2.  **Create a sample data file.** For this example, create a CSV file named `sample_data.csv` with an index column and three random data columns, and a few rows of data.

    ```bash
    echo "id,col_a,col_b,col_c" > sample_data.csv
    echo "1,0.5,0.2,0.8" >> sample_data.csv
    echo "2,0.1,0.7,0.3" >> sample_data.csv
    echo "3,0.9,0.4,0.6" >> sample_data.csv
    ```

3.  **Initialize dataset metadata.** This creates a `dataset-metadata.json` file in your current directory.

    ```bash
    kaggle datasets init
    ```

4.  **Edit the metadata file.** Open `dataset-metadata.json` in a text editor and make the following changes:
    *   Replace `"INSERT_TITLE_HERE"` with your desired dataset title, e.g., `"My Sample Dataset"`.
    *   Replace `"INSERT_SLUG_HERE"` with a URL-friendly version of your title, e.g., `"my-sample-dataset"`. The URL-friendly version is made by converting the title to lower-case and changing spaces to dashes.
    *   You can also add licenses, descriptions, and other relevant information.

    *Example using `sed` (for Linux/macOS):*
    ```bash
    sed -i 's/INSERT_TITLE_HERE/My Sample Dataset/' dataset-metadata.json
    sed -i 's/INSERT_SLUG_HERE/my-sample-dataset/' dataset-metadata.json
    ```

5.  **Create the dataset.** This command uploads your `sample_data.csv` and `dataset-metadata.json` to Kaggle.

    ```bash
    kaggle datasets create -p .
    ```
    You can add `--public` to make it public immediately.

6.  **Verify on Kaggle.com.** Go to your Kaggle profile and check the "Datasets" tab in the "Your Work" section. You should see "My Sample Dataset".

## Tutorial: Download a Dataset and Prepare for Analysis

This tutorial explains how to find, download, and prepare a Kaggle dataset for local analysis using the CLI.

1.  **Search for a Dataset (Optional).**
    *   If you know the dataset you want, you can skip this step. Otherwise, you can search for datasets. For example, to search for datasets related to "iris":
        ```bash
        kaggle datasets list -s iris
        ```
    *   This command will list datasets matching your search query. Note the dataset's "ref" (e.g., `uciml/iris`) which you'll use for downloading.

2.  **Choose a Dataset and Create a Directory.**
    *   For this tutorial, we'll use the classic "Iris" dataset, which has the ref `uciml/iris`.
    *   Create a new directory for your dataset and navigate into it:
        ```bash
        mkdir iris-dataset-analysis
        cd iris-dataset-analysis
        ```

3.  **Download the Dataset.**
    *   Use the `kaggle datasets download` command with the dataset's ref.
        ```bash
        kaggle datasets download -d uciml/iris
        ```
    *   This will download the dataset files, typically as a ZIP archive (e.g., `iris.zip`), into your current directory (`iris-dataset-analysis`).

4.  **Unzip the Dataset.**
    *   Note: you could skip this step by using the `--unzip` flag on the previous command.
    *   Most datasets are downloaded as ZIP files. You'll need to unzip the archive to access the data files (e.g., CSV files).
        ```bash
        # Make sure you have unzip installed, or use your OS's GUI to extract
        # The actual zip file name might vary based on the dataset.
        # For uciml/iris, it's iris.zip
        unzip iris.zip
        ```
    *   After unzipping, you should see the data files (e.g., `Iris.csv`, `database.sqlite`).

5.  **Prepare for Analysis.**
    *   The dataset is now downloaded and extracted. The primary data file for the Iris dataset is `Iris.csv`.
    *   You can now use your preferred tools (e.g., Python with libraries like Pandas and Scikit-learn, R, etc.) to load and analyze the data.
    *   For example, in a Python script within the `iris-dataset-analysis` directory, you might load the data using Pandas:
        ```python
        import pandas as pd
        df = pd.read_csv('Iris.csv')
        print(df.head())
        print(df.info())
        ```

This completes the process of downloading a dataset and preparing it for analysis using the Kaggle CLI.
You can adapt these steps for any dataset on Kaggle.

## Tutorial: Update a Kernel (Notebook)

This tutorial shows how to download an existing kernel, modify it, and push the changes back to Kaggle.

1.  **Create or identify a kernel on Kaggle.com.**
    *   Log in to kaggle.com.
    *   Find an existing notebook (or create one). For this tutorial, let's assume its title is "My CLI Test Kernel".
    *   If the notebook has not been saved before, make a small change and **save a version** of the notebook on Kaggle.com (e.g., click "Save Version" and choose "Save & Run All (Commit)"). You cannot pull or push a kernel that is only in draft form.
    *   Note the kernel slug from the browser's address bar. It will be something like `YOUR_USERNAME/my-cli-test-kernel`.

2.  **Create a new local directory for your kernel.**

    ```bash
    mkdir my-kernel-project
    cd my-kernel-project
    ```

3.  **Pull the kernel.** Use the `kaggle kernels pull` command with your username and the kernel slug. The `-m` flag includes the `kernel-metadata.json` file, which is required for pushing updates.

    ```bash
    # Replace YOUR_USERNAME with your actual Kaggle username
    kaggle kernels pull YOUR_USERNAME/my-cli-test-kernel -m
    ```
    This will download `my-cli-test-kernel.ipynb` (or `.py`/`.Rmd`) and `kernel-metadata.json`.

4.  **Edit the kernel or metadata.**
    *   Open the downloaded notebook file (e.g., `my-cli-test-kernel.ipynb`) and make some changes to the code or content.
    *   Open `kernel-metadata.json`. Let's add "benchmark" to the keywords. Find the `"keywords": []` line and change it to `"keywords": ["benchmark"]`.
    *   *Note: While you can edit keywords here, it's often best to manage them on kaggle.com, as there might be a restricted list of allowed keywords.*

5.  **Push the kernel.** This uploads your changes and the updated metadata, then runs the kernel on Kaggle.

    ```bash
    kaggle kernels push -p .
    ```

6.  **Verify on Kaggle.com.** Refresh the notebook page on kaggle.com. You should see your code changes and the "benchmark" tag added to the kernel settings.

## Tutorial: Create a Model

This tutorial guides you through creating a new model on Kaggle.

1.  **Start from an empty directory.** Create a new directory for your model files and navigate into it.

    ```bash
    mkdir my-new-model
    cd my-new-model
    ```

2.  **Copy your model definition files (optional for this step).** If you have files that define your model (e.g., Python scripts, model weights), copy them into this directory. For the `kaggle models create` step, only the metadata is strictly required, but you'll need files when you create a model instance.

3.  **Initialize model metadata.** This creates a `model-metadata.json` file.

    ```bash
    kaggle models init
    ```

4.  **Edit the metadata file.** Open `model-metadata.json` and make the following changes:
    *   Replace `"INSERT_OWNER_SLUG_HERE"` with your Kaggle username (e.g., `"YOUR_USERNAME"`).
    *   Replace `"INSERT_TITLE_HERE"` with your model's title (e.g., `"My Awesome AI Model"`).
    *   Replace `"INSERT_SLUG_HERE"` with a URL-friendly version of the title (e.g., `"my-awesome-ai-model"`).
    *   Fill out the `"description"` field and other relevant sections like `"licenses"`.

    *Example using `sed` (for Linux/macOS):*
    ```bash
    # Replace YOUR_USERNAME with your actual Kaggle username
    sed -i 's/INSERT_OWNER_SLUG_HERE/YOUR_USERNAME/' model-metadata.json
    sed -i 's/INSERT_TITLE_HERE/My Awesome AI Model/' model-metadata.json
    sed -i 's/INSERT_SLUG_HERE/my-awesome-ai-model/' model-metadata.json
    ```

5.  **Create the model.**

    ```bash
    kaggle models create -p .
    ```

6.  **Verify on Kaggle.com.** Go to your Kaggle profile and check the "Models" tab in the "Your Work" section. You should see "My Awesome AI Model".

## Tutorial: Create a Model Instance

This tutorial shows how to create an instance under an existing model. A model instance usually represents the model implemented in a specific framework (like TensorFlow, PyTorch, JAX, etc.) and includes the actual model files.

1.  **Ensure you have a parent model.** Follow the "Create a Model" tutorial if you haven't already. Let's assume your model slug is `my-awesome-ai-model` and your username is `YOUR_USERNAME`.

2.  **Prepare your model instance files.** In your model directory (e.g., `my-new-model`), create or place the files for this specific instance. For example, a JAX model might have a `flax_model.params` file.

    ```bash
    # In the my-new-model directory
    echo "This is a placeholder for JAX model parameters" > flax_model.params
    ```

3.  **Initialize model instance metadata.** This creates `model-instance-metadata.json`.

    ```bash
    # Still in the my-new-model directory
    kaggle models instances init
    ```

4.  **Edit the instance metadata file.** Open `model-instance-metadata.json` and make changes:
    *   Replace `"INSERT_OWNER_SLUG_HERE"` with your Kaggle username (e.g., `"YOUR_USERNAME"`).
    *   Replace `"INSERT_EXISTING_MODEL_SLUG_HERE"` with your parent model's slug (e.g., `"my-awesome-ai-model"`).
    *   Replace `"INSERT_INSTANCE_SLUG_HERE"` with a slug for this instance (e.g., `"jax-implementation"`).
    *   Replace `"INSERT_FRAMEWORK_HERE"` with the model framework (e.g., `"jax"`, `"tensorflow"`, `"pytorch"`, `"sklearn"`).
    *   Update the `"instance_size_bytes"` if known, and add a `"description"`.

    *Example using `sed` (for Linux/macOS):*
    ```bash
    # Replace YOUR_USERNAME and my-awesome-ai-model accordingly
    sed -i 's/INSERT_OWNER_SLUG_HERE/YOUR_USERNAME/' model-instance-metadata.json
    sed -i 's/INSERT_EXISTING_MODEL_SLUG_HERE/my-awesome-ai-model/' model-instance-metadata.json
    sed -i 's/INSERT_INSTANCE_SLUG_HERE/jax-implementation/' model-instance-metadata.json
    sed -i 's/INSERT_FRAMEWORK_HERE/jax/' model-instance-metadata.json
    ```

5.  **Create the model instance.** This uploads the files in the current directory (e.g., `flax_model.params`) along with the instance metadata.

    ```bash
    kaggle models instances create -p .
    ```

6.  **Verify on Kaggle.com.** Go to your model's page on Kaggle. You should see a new "jax-implementation" instance listed, and it will have one version containing `flax_model.params`.

## Tutorial: Create a Model Instance Version

This tutorial explains how to add a new version to an existing model instance, for example, when you have updated model weights or files.

1.  **Ensure you have a model instance.** Follow the "Create a Model Instance" tutorial. Let's assume your instance is `YOUR_USERNAME/my-awesome-ai-model/jax/jax-implementation`.

2.  **Prepare your updated files.** In your model instance directory (e.g., `my-new-model`), update or add new files for this version. For example, create `flax_model_v2.params`.

    ```bash
    # In the my-new-model directory
    echo "Updated JAX model parameters for V2" > flax_model_v2.params
    # You might also remove or update flax_model.params if it's being replaced
    ```

3.  **Create the new model instance version.** You need to specify the parent model instance and provide version notes. The files from the `-p` path will form the contents of this new version.

    ```bash
    # Replace YOUR_USERNAME and model/instance slugs accordingly
    kaggle models instances versions create YOUR_USERNAME/my-awesome-ai-model/jax/jax-implementation -p . -n "Second version with updated parameters"
    ```
    *Note: The `-p .` means all files in the current directory will be uploaded as part of this new version. If you only want to upload `flax_model_v2.params`, ensure only it (and any other V2 files) are in a directory and point `-p` to that directory, or manage your files carefully.*

4.  **Verify on Kaggle.com.** Go to your model instance page on Kaggle (e.g., `YOUR_USERNAME/my-awesome-ai-model/jax/jax-implementation`). You should see a new version (e.g., version 2) listed with your notes and the new files.

## Tutorial: How to Submit to a Competition

This tutorial walks you through the process of making a submission to a Kaggle competition using the CLI.

1.  **Find a Competition and Accept Rules.**
    *   First, you need to find a competition. You can list active competitions using `kaggle competitions list`.
    *   For this tutorial, we'll use the "titanic" competition, which is a common starting point. You can find it at `https://www.kaggle.com/c/titanic`.
    *   **Important**: Before you can download data or submit, you *must* accept the competition's rules on the Kaggle website. Navigate to the competition page (e.g., `https://www.kaggle.com/c/titanic/rules`) and accept the terms.

2.  **Create a Directory and Download Competition Files.**
    *   Create a new directory for your competition files and navigate into it.
        ```bash
        mkdir titanic-competition
        cd titanic-competition
        ```
    *   Download the competition files. This usually includes training data, test data, and a sample submission file.
        ```bash
        kaggle competitions download -c titanic
        ```
    *   This will download `titanic.zip`. You'll need to unzip it to see the files (e.g., `train.csv`, `test.csv`, `gender_submission.csv`).
        ```bash
        # Make sure you have unzip installed, or use your OS's GUI to extract
        # The actual zip file name might vary based on the dataset.
        unzip titanic.zip
        ```

3.  **Create Your Submission File.**
    *   The required format for the submission file is specific to each competition. You can find this information on the competition's "Evaluation" page or by examining the sample submission file (e.g., `gender_submission.csv` for the Titanic competition).
    *   For the Titanic competition, the submission file needs two columns: `PassengerId` and `Survived`. The `Survived` column should contain your predictions (0 for deceased, 1 for survived).
    *   Let's create a very simple submission file based on the `gender_submission.csv` (which predicts survival based on gender). For this tutorial, we'll just copy it and use it as our submission. In a real scenario, you would generate this file from your model's predictions on the `test.csv` data.
        ```bash
        cp gender_submission.csv my_submission.csv
        ```
    *   Your `my_submission.csv` should look something like this:
        ```csv
        PassengerId,Survived
        892,0
        893,1
        894,0
        ...
        ```

4.  **Submit to the Competition.**
    *   Use the `kaggle competitions submit` command. You need to specify:
        *   The competition ID (`-c titanic`).
        *   The path to your submission file (`-f my_submission.csv`).
        *   A message describing your submission (`-m "My first submission via CLI"`).
        ```bash
        kaggle competitions submit -c titanic -f my_submission.csv -m "My first submission via CLI"
        ```

5.  **Check Your Submission Status.**
    *   After submitting, you'll get a message indicating success or failure.
    *   You can check your submission's score and status on the "My Submissions" tab of the competition page on Kaggle.com (e.g., `https://www.kaggle.com/c/titanic/submissions`).
    *   You can also list your recent submissions and their scores via the CLI:
        ```bash
        kaggle competitions submissions -c titanic
        ```
    *   This command will show your submission, its status (e.g., `complete`, `error`), and your public/private scores if available.

This completes the process of submitting to a Kaggle competition using the CLI!
