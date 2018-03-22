# Kaggle API

Official API for https://www.kaggle.com, accessible using a command line tool implemented in Python.

Beta release - Kaggle reserves the right to modify the API functionality currently offered.

## Installation

Ensure you have Python and the package manager `pip` installed.

Run the following command to access the Kaggle API using the command line:

`pip install kaggle`

or if you are using Python3 run the following command to access the Kaggle API using the command line: 

`pip3 install kaggle`

You can now use the `kaggle` command as shown in the examples below.

## API credentials

To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com. Then go to the 'Account' tab of your user profile (`https://www.kaggle.com/<username>/account`) and select 'Create API Token'. This will trigger the download of `kaggle.json`, a file containing your API credentials. Place this file in the location `~/.kaggle/kaggle.json` (on Windows in the location `C:\Users\<Windows-username>\.kaggle\kaggle.json`).

For your security, ensure that other users of your computer do not have read access to your credentials. On Unix-based systems you can do this with the following command: 

`chmod 600 ~/.kaggle/kaggle.json`

## Commands

The command line tool supports the following commands:

``` 
kaggle competitions {list, files, download, submit, submissions}
kaggle datasets {list, files, download, create, version, init}
kaggle config {view, set, unset}
```

See more details below for using each of these commands.

### Competitions

The API supports the following commands for Kaggle Competitions.

##### List competitions

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

`kaggle competitions list -s health`

##### List competition files

```
usage: kaggle competitions files [-h] [-c COMPETITION] [-v] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -c COMPETITION, --competition COMPETITION
                        Competition URL suffix (use "kaggle competitions list" to show options)
                        If empty, the default competition will be used (use "kaggle config set competition")"
  -v, --csv             Print results in CSV format (if not set print in table format)
  -q, --quiet           Suppress printing information about download progress
```

Example:

`kaggle competitions files -c favorita-grocery-sales-forecasting`

##### Download competition files

```
usage: kaggle competitions download [-h] [-c COMPETITION] [-f FILE] [-p PATH]
                                    [-w] [-o] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -c COMPETITION, --competition COMPETITION
                        Competition URL suffix (use "kaggle competitions list" to show options)
                        If empty, the default competition will be used (use "kaggle config set competition")"
  -f FILE, --file FILE  File name, all files downloaded if not provided
                        (use "kaggle competitions files -c <competition>" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to C:\Users\timoboz\.kaggle
  -w, --wp              Download files to current working path
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about download progress
 ```

Examples:

`kaggle competitions download -c favorita-grocery-sales-forecasting`

`kaggle competitions download -c favorita-grocery-sales-forecasting -f test.csv.7z`

Note: you will need to accept competition rules at `https://www.kaggle.com/c/<competition-name>/rules`.

##### Submit to a competition

```
usage: kaggle competitions submit [-h] [-c COMPETITION] -f FILE -m MESSAGE
                                  [-q]

required arguments:
  -f FILE, --file FILE  File for upload (full path)
  -m MESSAGE, --message MESSAGE
                        Message describing this submission

optional arguments:
  -h, --help            show this help message and exit
  -c COMPETITION, --competition COMPETITION
                        Competition URL suffix (use "kaggle competitions list" to show options)
                        If empty, the default competition will be used (use "kaggle config set competition")"
  -q, --quiet           Suppress printing information about download progress
```

Example: 

`kaggle competitions submit -c favorita-grocery-sales-forecasting -f sample_submission_favorita.csv.7z -m "My submission message"`

Note: you will need to accept competition rules at `https://www.kaggle.com/c/<competition-name>/rules`.

##### List competition submissions

```
usage: kaggle competitions submissions [-h] [-c COMPETITION] [-v] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -c COMPETITION, --competition COMPETITION
                        Competition URL suffix (use "kaggle competitions list" to show options)
                        If empty, the default competition will be used (use "kaggle config set competition")"
  -v, --csv             Print results in CSV format (if not set print in table format)
  -q, --quiet           Suppress printing information about download progress
 ```
 
Example:

`kaggle competitions submissions -c favorita-grocery-sales-forecasting`

Note: you will need to accept competition rules at `https://www.kaggle.com/c/<competition-name>/rules`.



### Datasets

The API supports the following commands for Kaggle Datasets.

##### List datasets

```
usage: kaggle datasets list [-h] [-p PAGE] [-s SEARCH] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -p PAGE, --page PAGE  Page number for results paging
  -s SEARCH, --search SEARCH
                        Term(s) to search for
  -v, --csv             Print results in CSV format (if not set print in table format)
```

Example:

`kaggle datasets list -s demographics`

##### List files for a dataset

```
usage: kaggle datasets files [-h] -d DATASET [-v]

required arguments:
  -d DATASET, --dataset DATASET
                        Dataset URL suffix in format <owner>/<dataset-name> (use "kaggle datasets list" to show options)

optional arguments:
  -h, --help            show this help message and exit
  -v, --csv             Print results in CSV format (if not set print in table format)
 ```

Example:

`kaggle datasets files -d zillow/zecon`

##### Download dataset files

```
usage: kaggle datasets download [-h] -d DATASET [-f FILE] [-p PATH] [-w] [-o]
                                [-q]

required arguments:
  -d DATASET, --dataset DATASET
                        Dataset URL suffix in format <owner>/<dataset-name> (use "kaggle datasets list" to show options)

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File name, all files downloaded if not provided
                        (use "kaggle datasets files -d <dataset>" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to C:\Users\timoboz\.kaggle
  -w, --wp              Download files to current working path
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about download progress
```

Examples:

`kaggle datasets download -d zillow/zecon`

`kaggle datasets download -d zillow/zecon -f State_time_series.csv`


##### Create a new dataset

```
usage: kaggle datasets create [-h] -p FOLDER [-u] [-q]

required arguments:
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special datapackage.json file (https://github.com/Kaggle/kaggle-api/wiki/Metadata)

optional arguments:
  -h, --help            show this help message and exit
  -u, --public          Create the Dataset publicly (default is private)
  -q, --quiet           Suppress printing information about download progress
```

Example:

`kaggle datasets create -r -p /path/to/dataset`


##### Create a new dataset version

```
usage: kaggle datasets version [-h] -m VERSION_NOTES -p FOLDER [-q]

required arguments:
  -m VERSION_NOTES, --message VERSION_NOTES
                        Message describing the new version
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special datapackage.json file (https://github.com/Kaggle/kaggle-api/wiki/Metadata)

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           Suppress printing information about download progress
```

Example:

`kaggle datasets version -p /path/to/dataset -m "Updated data"`


##### Initialize metadata file for dataset creation

```
usage: kaggle datasets init [-h] -p FOLDER

required arguments:
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special datapackage.json file (https://github.com/Kaggle/kaggle-api/wiki/Metadata)

optional arguments:
  -h, --help            show this help message and exit
```

Example:

`kaggle datasets init -p /path/to/dataset`


### Config

##### View current config values

```
usage: kaggle config path [-h] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  folder where file(s) will be downloaded, defaults to ~/.kaggle
```

Example:

`kaggle config path -p C:\`

##### View current config values

```
usage: kaggle config view [-h]

optional arguments:
  -h, --help  show this help message and exit
```

Example:

`kaggle config view`


##### Set a configuration value

```
usage: kaggle config set [-h] -n NAME -v VALUE

required arguments:
  -n NAME, --name NAME  Name of the configuration parameter
                        (one of competition, path, proxy)
  -v VALUE, --value VALUE
                        Value of the configuration parameter, valid values depending on name
                        - competition: Competition URL suffix (use "kaggle competitions list" to show options)
                        - path: Folder where file(s) will be downloaded, defaults to C:\Users\timoboz\.kaggle
                        - proxy: Proxy for HTTP requests
```

Example:

`kaggle config set -n competition -v titanic`


##### Clear a configuration value

```
usage: kaggle config unset [-h] -n NAME

required arguments:
  -n NAME, --name NAME  Name of the configuration parameter
                        (one of competition, path, proxy)
```

Example:

`kaggle config unset -n competition`


## License

The Kaggle API is released under the Apache 2.0 license.
