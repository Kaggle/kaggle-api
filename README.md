# Kaggle API

## API credentials

To use the Kaggle API go to `https://www.kaggle.com/<username>/account` and select 'Create API Token'. This will trigger the download of kaggle.json, a file containing your API credentials. Place this file in the folder `<your user home directory>/.kaggle` (e.g. `C:\Users\<username>\.kaggle`).

## Installation

Run `python setup.py install`. Then navigate to the location where your Python package manager stores scripts (e.g. C:\Anaconda\Scripts) and find `kaggle.exe`.

Within that folder (or adding that folder to your path), run `kaggle` followed by the desired command as shown in the examples below.

## Requirements

Python 3

## Competitions

### List competitions

```
usage: kaggle competitions list [-h] [--page PAGE] [--csv] [--search SEARCH]

optional arguments:
  -h, --help            show this help message and exit
  --page PAGE, -p PAGE  page number
  --csv, -s             print in CSV format
                        (if not set print in table format)
  --search SEARCH, -e SEARCH
                        term(s) to search for
```

Example: 

`kaggle competitions list -e music`

### Submit to a competition

```
usage: kaggle competitions submit [-h] --competition COMPETITION --file FILE
                                  --description DESCRIPTION

optional arguments:
  -h, --help            show this help message and exit
  --competition COMPETITION, -c COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)
  --file FILE, -f FILE  file for upload, including path
  --description DESCRIPTION, -d DESCRIPTION
                        description message for this submission
```

Example: 

`kaggle competitions submit -c favorita-grocery-sales-forecasting -f sample_submission_favorita.csv.7z -d "My submission message"`

### List competition submissions

```
usage: kaggle competitions submissions [-h] --competition COMPETITION [--csv]

optional arguments:
  -h, --help            show this help message and exit
  --competition COMPETITION, -c COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)
  --csv, -s             print in CSV format
                        (if not set print in table format)
 ```
 
Example:

`kaggle competitions submissions -c favorita-grocery-sales-forecasting`

### List competition files

```
usage: kaggle competitions list-files [-h] --competition COMPETITION [--csv]

optional arguments:
  -h, --help            show this help message and exit
  --competition COMPETITION, -c COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)
  --csv, -s             print in CSV format
                        (if not set print in table format)
```

Example:

`kaggle competitions list-files -c favorita-grocery-sales-forecasting`

### Download a competition file

```
usage: kaggle competitions download-file [-h] --competition COMPETITION --file
                                         FILE [--path PATH] [--force]
                                         [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --competition COMPETITION, -c COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)
  --file FILE, -f FILE  file name
                        (use "kaggle competitions list-files -c <competition>" to show options)
  --path PATH, -p PATH  folder where file(s) will be downloaded, defaults to C:\Users\dpmcna\.kaggle
  --force, -o           skip check whether local version of file is up to date, force file download
  --verbose, -v         print information about download progress
 ```

Example:

`kaggle competitions download-file -c favorita-grocery-sales-forecasting -f test.csv.7z`

### Download all competition files

```
usage: kaggle competitions download-files [-h] --competition COMPETITION
                                          [--path PATH] [--force] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --competition COMPETITION, -c COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)
  --path PATH, -p PATH  folder where file(s) will be downloaded, defaults to C:\Users\dpmcna\.kaggle
  --force, -o           skip check whether local version of file is up to date, force file download
  --verbose, -v         print information about download progress
```

Example:

`kaggle competitions download-files -c favorita-grocery-sales-forecasting`

## Datasets

### List datasets

```
usage: kaggle datasets list [-h] [--page PAGE] [--csv] [--search SEARCH]

optional arguments:
  -h, --help            show this help message and exit
  --page PAGE, -p PAGE  page number
  --csv, -s             print in CSV format
                        (if not set print in table format)
  --search SEARCH, -e SEARCH
                        term(s) to search for
```

Example:

`kaggle datasets list -e wine`

### List files for a dataset

```
usage: kaggle datasets list-files [-h] --dataset DATASET [--csv]

optional arguments:
  -h, --help            show this help message and exit
  --dataset DATASET, -d DATASET
                        dataset URL suffix in format <owner>/<dataset-name>
                        (use "kaggle datasets list" to show options)
  --csv, -s             print in CSV format
                        (if not set print in table format)
 ```

Example:

`kaggle datasets list-files -d zynicide/wine-reviews`

### Download a dataset file

```
usage: kaggle datasets download-file [-h] --dataset DATASET --file FILE
                                     [--path PATH] [--force] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --dataset DATASET, -d DATASET
                        dataset URL suffix in format <owner>/<dataset-name>
                        (use "kaggle datasets list" to show options)
  --file FILE, -f FILE  file name
                        (use "kaggle datasets list-files -d <dataset>" to show options)
  --path PATH, -p PATH  folder where file(s) will be downloaded, defaults to C:\Users\dpmcna\.kaggle
  --force, -o           skip check whether local version of file is up to date, force file download
  --verbose, -v         print information about download progress
```

Example:

`kaggle datasets download-file -d zynicide/wine-reviews -f winemag-data-130k-v2.csv`

### Download all files for a dataset

```
usage: kaggle datasets download-files [-h] --dataset DATASET [--path PATH]
                                      [--force] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --dataset DATASET, -d DATASET
                        dataset URL suffix in format <owner>/<dataset-name>
                        (use "kaggle datasets list" to show options)
  --path PATH, -p PATH  folder where file(s) will be downloaded, defaults to C:\Users\dpmcna\.kaggle
  --force, -o           skip check whether local version of file is up to date, force file download
  --verbose, -v         print information about download progress
```

Example:

`kaggle datasets download-files -d zynicide/wine-reviews`

