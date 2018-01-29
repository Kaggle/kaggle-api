# Kaggle API

## Installation

Ensure you have Python 3 installed.

Clone this repo by running `git clone https://github.com/Kaggle/kaggle-api.git`.

Run `python setup.py install`. Then navigate to the location where your Python package manager stores scripts (e.g. `C:\Anaconda\Scripts`) and find `kaggle.exe`.

Within that folder (or adding that folder to your system path), run `kaggle` followed by the desired command as shown in the examples below.

## API credentials

To use the Kaggle API go to `https://www.kaggle.com/<username>/account` and select 'Create API Token'. This will trigger the download of kaggle.json, a file containing your API credentials. Place this file in the folder `<your user home directory>/.kaggle` (e.g. `C:\Users\<username>\.kaggle`).

## Competitions

### List competitions

```
usage: kaggle competitions list [-h] [-p PAGE] [-s SEARCH] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -p PAGE, --page PAGE  page number
  -s SEARCH, --search SEARCH
                        term(s) to search for
  -v, --csv             print in CSV format
                        (if not set print in table format)
```

Example: 

`kaggle competitions list -s music`

### Submit to a competition

```
usage: kaggle competitions submit [-h] -c COMPETITION -f FILE -m MESSAGE

required arguments:
  -c COMPETITION, --competition COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)
  -f FILE, --file FILE  file for upload, including path
  -m MESSAGE, --message MESSAGE
                        message describing this submission

optional arguments:
  -h, --help            show this help message and exit
```

Example: 

`kaggle competitions submit -c favorita-grocery-sales-forecasting -f sample_submission_favorita.csv.7z -m "My submission message"`

### List competition submissions

```
usage: kaggle competitions submissions [-h] -c COMPETITION [-v]

required arguments:
  -c COMPETITION, --competition COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)

optional arguments:
  -h, --help            show this help message and exit
  -v, --csv             print in CSV format
                        (if not set print in table format)
 ```
 
Example:

`kaggle competitions submissions -c favorita-grocery-sales-forecasting`

### List competition files

```
usage: kaggle competitions files [-h] -c COMPETITION [-v]

required arguments:
  -c COMPETITION, --competition COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)

optional arguments:
  -h, --help            show this help message and exit
  -v, --csv             print in CSV format
                        (if not set print in table format)
```

Example:

`kaggle competitions files -c favorita-grocery-sales-forecasting`

### Download competition files

```
usage: kaggle competitions download [-h] -c COMPETITION [-f FILE] [-p PATH]
                                    [-w] [-o] [-q]

required arguments:
  -c COMPETITION, --competition COMPETITION
                        competition URL suffix
                        (use "kaggle competitions list" to show options)

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  file name, all files downloaded if not provided
                        (use "kaggle competitions files -c <competition>" to show options)
  -p PATH, --path PATH  folder where file(s) will be downloaded, defaults to <your user home directory>/.kaggle
  -w, --wp              download to current working path
  -o, --force           skip check whether local version of file is up to date, force file download
  -q, --quiet           suppress printing information about download progress
 ```

Examples:

`kaggle competitions download -c favorita-grocery-sales-forecasting`

`kaggle competitions download -c favorita-grocery-sales-forecasting -f test.csv.7z`





## Datasets

### List datasets

```
usage: kaggle datasets list [-h] [-p PAGE] [-s SEARCH] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -p PAGE, --page PAGE  page number
  -s SEARCH, --search SEARCH
                        term(s) to search for
  -v, --csv             print in CSV format
                        (if not set print in table format)
```

Example:

`kaggle datasets list -s wine`

### List files for a dataset

```
usage: kaggle datasets files [-h] -d DATASET [-v]

required arguments:
  -d DATASET, --dataset DATASET
                        dataset URL suffix in format <owner>/<dataset-name>
                        (use "kaggle datasets list" to show options)

optional arguments:
  -h, --help            show this help message and exit
  -v, --csv             print in CSV format
                        (if not set print in table format)
 ```

Example:

`kaggle datasets files -d zynicide/wine-reviews`

### Download dataset files

```
usage: kaggle datasets download [-h] -d DATASET [-f FILE] [-p PATH] [-w] [-o]
                                [-q]

required arguments:
  -d DATASET, --dataset DATASET
                        dataset URL suffix in format <owner>/<dataset-name>
                        (use "kaggle datasets list" to show options)

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  file name, all files downloaded if not provided
                        (use "kaggle datasets files -d <dataset>" to show options)
  -p PATH, --path PATH  folder where file(s) will be downloaded, defaults to <your user home directory>/.kaggle
  -w, --wp              download to current working path
  -o, --force           skip check whether local version of file is up to date, force file download
  -q, --quiet           suppress printing information about download progress
```

Examples:

`kaggle datasets download -d zynicide/wine-reviews`

`kaggle datasets download -d zynicide/wine-reviews -f winemag-data-130k-v2.csv`


## Config

### Set or check path where files are downloaded

```
usage: kaggle config path [-h] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  folder where file(s) will be downloaded, defaults to <your user home directory>/.kaggle
```

Example:

`kaggle config path -p C:\`

