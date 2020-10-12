# Kaggle API

Official API for https://www.kaggle.com, accessible using a command line tool implemented in Python 3.  

Beta release - Kaggle reserves the right to modify the API functionality currently offered.

IMPORTANT: Competitions submissions using an API version prior to 1.5.0 may not work.  If you are encountering difficulties with submitting to competitions, please check your version with `kaggle --version`.  If it is below 1.5.0, please update with `pip install kaggle --upgrade`.

## Installation

Ensure you have Python 3 and the package manager `pip` installed.

Run the following command to access the Kaggle API using the command line:

`pip install kaggle` (You may need to do `pip install --user kaggle` on Mac/Linux.  This is recommended if problems come up during the installation process.) Installations done through the root user (i.e. `sudo pip install kaggle`) will not work correctly unless you understand what you're doing.  Even then, they still might not work.  User installs are strongly recommended in the case of permissions errors.

You can now use the `kaggle` command as shown in the examples below.

If you run into a `kaggle: command not found` error, ensure that your python binaries are on your path.  You can see where `kaggle` is installed by doing `pip uninstall kaggle` and seeing where the binary is.  For a local user install on Linux, the default location is `~/.local/bin`.  On Windows, the default location is `$PYTHON_HOME/Scripts`.

IMPORTANT: We do not offer Python 2 support.  Please ensure that you are using Python 3 before reporting any issues.

## API credentials

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


## Commands

The command line tool supports the following commands:

``` 
kaggle competitions {list, files, download, submit, submissions, leaderboard}
kaggle datasets {list, files, download, create, version, init}
kaggle kernels {list, init, push, pull, output, status}
kaggle config {view, set, unset}
```

See more details below for using each of these commands.

### Competitions

The API supports the following commands for Kaggle Competitions.

```
usage: kaggle competitions [-h]
                           {list,files,download,submit,submissions,leaderboard}
                           ...

optional arguments:
  -h, --help            show this help message and exit

commands:
  {list,files,download,submit,submissions,leaderboard}
    list                List available competitions
    files               List competition files
    download            Download competition files
    submit              Make a new competition submission
    submissions         Show your competition submissions
    leaderboard         Get competition leaderboard information
```

##### List competitions

```
usage: kaggle competitions list [-h] [--group GROUP] [--category CATEGORY] [--sort-by SORT_BY] [-p PAGE] [-s SEARCH] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --group GROUP         Search for competitions in a specific group. Default is 'general'. Valid options are 'general', 'entered', and 'inClass'
  --category CATEGORY   Search for competitions of a specific category. Default is 'all'. Valid options are 'all', 'featured', 'research', 'recruitment', 'gettingStarted', 'masters', and 'playground'
  --sort-by SORT_BY     Sort list results. Default is 'latestDeadline'. Valid options are 'grouped', 'prize', 'earliestDeadline', 'latestDeadline', 'numberOfTeams', and 'recentlyCreated'
  -p PAGE, --page PAGE  Page number for results paging. Page size is 20 by default 
  -s SEARCH, --search SEARCH
                        Term(s) to search for
  -v, --csv             Print results in CSV format
                        (if not set print in table format)
```

Example: 

`kaggle competitions list -s health`

`kaggle competitions list --category gettingStarted`

##### List competition files

```
usage: kaggle competitions files [-h] [-v] [-q] [competition]

optional arguments:
  -h, --help   show this help message and exit
  competition  Competition URL suffix (use "kaggle competitions list" to show options)
               If empty, the default competition will be used (use "kaggle config set competition")"
  -v, --csv    Print results in CSV format (if not set print in table format)
  -q, --quiet  Suppress printing information about the upload/download progress
```

Example:

`kaggle competitions files favorita-grocery-sales-forecasting`

##### Download competition files

```
usage: kaggle competitions download [-h] [-f FILE_NAME] [-p PATH] [-w] [-o]
                                    [-q]
                                    [competition]

optional arguments:
  -h, --help            show this help message and exit
  competition           Competition URL suffix (use "kaggle competitions list" to show options)
                        If empty, the default competition will be used (use "kaggle config set competition")"
  -f FILE_NAME, --file FILE_NAME
                        File name, all files downloaded if not provided
                        (use "kaggle competitions files -c <competition>" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about the upload/download progress
```

Examples:

`kaggle competitions download favorita-grocery-sales-forecasting`

`kaggle competitions download favorita-grocery-sales-forecasting -f test.csv.7z`

Note: you will need to accept competition rules at `https://www.kaggle.com/c/<competition-name>/rules`.

##### Submit to a competition

```
usage: kaggle competitions submit [-h] -f FILE_NAME -m MESSAGE [-q]
                                  [competition]

required arguments:
  -f FILE_NAME, --file FILE_NAME
                        File for upload (full path)
  -m MESSAGE, --message MESSAGE
                        Message describing this submission

optional arguments:
  -h, --help            show this help message and exit
  competition           Competition URL suffix (use "kaggle competitions list" to show options)
                        If empty, the default competition will be used (use "kaggle config set competition")"
  -q, --quiet           Suppress printing information about the upload/download progress
```

Example: 

`kaggle competitions submit favorita-grocery-sales-forecasting -f sample_submission_favorita.csv.7z -m "My submission message"`

Note: you will need to accept competition rules at `https://www.kaggle.com/c/<competition-name>/rules`.

##### List competition submissions

```
usage: kaggle competitions submissions [-h] [-v] [-q] [competition]

optional arguments:
  -h, --help   show this help message and exit
  competition  Competition URL suffix (use "kaggle competitions list" to show options)
               If empty, the default competition will be used (use "kaggle config set competition")"
  -v, --csv    Print results in CSV format (if not set print in table format)
  -q, --quiet  Suppress printing information about the upload/download progress
```
 
Example:

`kaggle competitions submissions favorita-grocery-sales-forecasting`

Note: you will need to accept competition rules at `https://www.kaggle.com/c/<competition-name>/rules`.

##### Get competition leaderboard

```
usage: kaggle competitions leaderboard [-h] [-s] [-d] [-p PATH] [-v] [-q]
                                       [competition]

optional arguments:
  -h, --help            show this help message and exit
  competition           Competition URL suffix (use "kaggle competitions list" to show options)
                        If empty, the default competition will be used (use "kaggle config set competition")"
  -s, --show            Show the top of the leaderboard
  -d, --download        Download entire leaderboard
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -v, --csv             Print results in CSV format (if not set print in table format)
  -q, --quiet           Suppress printing information about the upload/download progress
```

Example:

`kaggle competitions leaderboard favorita-grocery-sales-forecasting -s`


### Datasets

The API supports the following commands for Kaggle Datasets.

```
usage: kaggle datasets [-h]
                       {list,files,download,create,version,init,metadata,status} ...

optional arguments:
  -h, --help            show this help message and exit

commands:
  {list,files,download,create,version,init,metadata, status}
    list                List available datasets
    files               List dataset files
    download            Download dataset files
    create              Create a new dataset
    version             Create a new dataset version
    init                Initialize metadata file for dataset creation
    metadata            Download metadata about a dataset
    status              Get the creation status for a dataset
```

##### List datasets

```
usage: kaggle datasets list [-h] [--sort-by SORT_BY] [--size SIZE] [--file-type FILE_TYPE] [--license LICENSE_NAME] [--tags TaG_IDS] [-s SEARCH] [-m] [--user USER] [-p PAGE] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --sort-by SORT_BY     Sort list results. Default is 'hottest'. Valid options are 'hottest', 'votes', 'updated', and 'active'
  --size SIZE           Search for datasets of a specific size. Default is 'all'. Valid options are 'all', 'small', 'medium', and 'large'
  --file-type FILE_TYPE Search for datasets with a specific file type. Default is 'all'. Valid options are 'all', 'csv', 'sqlite', 'json', and 'bigQuery'. Please note that bigQuery datasets cannot be downloaded
  --license LICENSE_NAME 
                        Search for datasets with a specific license. Default is 'all'. Valid options are 'all', 'cc', 'gpl', 'odb', and 'other'
  --tags TAG_IDS        Search for datasets that have specific tags. Tag list should be comma separated                      
  -s SEARCH, --search SEARCH
                        Term(s) to search for
  -m, --mine            Display only my items
  --user USER           Find public datasets owned by a specific user or organization
  -p PAGE, --page PAGE  Page number for results paging. Page size is 20 by default
  -v, --csv             Print results in CSV format (if not set print in table format)
```

Example:

`kaggle datasets list -s demographics`

`kaggle datasets list --sort-by votes`

##### List files for a dataset

```
usage: kaggle datasets files [-h] [-v] [dataset]

optional arguments:
  -h, --help  show this help message and exit
  dataset     Dataset URL suffix in format <owner>/<dataset-name> (use "kaggle datasets list" to show options)
  -v, --csv   Print results in CSV format (if not set print in table format)
```

Example:

`kaggle datasets files zillow/zecon`

##### Download dataset files

```
usage: kaggle datasets download [-h] [-f FILE_NAME] [-p PATH] [-w] [--unzip]
                                [-o] [-q]
                                [dataset]

optional arguments:
  -h, --help            show this help message and exit
  dataset               Dataset URL suffix in format <owner>/<dataset-name> (use "kaggle datasets list" to show options)
  -f FILE_NAME, --file FILE_NAME
                        File name, all files downloaded if not provided
                        (use "kaggle datasets files -d <dataset>" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  --unzip               Unzip the downloaded file. Will delete the zip file when completed.
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about the upload/download progress
```


Examples:

`kaggle datasets download zillow/zecon`

`kaggle datasets download zillow/zecon -f State_time_series.csv`

Please note that BigQuery datasets cannot be downloaded.

##### Initialize metadata file for dataset creation

```
usage: kaggle datasets init [-h] [-p FOLDER]

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special dataset-metadata.json file (https://github.com/Kaggle/kaggle-api/wiki/Dataset-Metadata). Defaults to current working directory
```

Example:

`kaggle datasets init -p /path/to/dataset`

##### Create a new dataset

If you want to create a new dataset, you need to initiate metadata file at first. You could fulfill this by running `kaggle datasets init` as describe above.

```
usage: kaggle datasets create [-h] [-p FOLDER] [-u] [-q] [-t] [-r {skip,zip,tar}]

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special dataset-metadata.json file (https://github.com/Kaggle/kaggle-api/wiki/Dataset-Metadata). Defaults to current working directory
  -u, --public          Create publicly (default is private)
  -q, --quiet           Suppress printing information about the upload/download progress
  -t, --keep-tabular    Do not convert tabular files to CSV (default is to convert)
  -r {skip,zip,tar}, --dir-mode {skip,zip,tar}
                        What to do with directories: "skip" - ignore; "zip" - compressed upload; "tar" - uncompressed upload
```

Example:

`kaggle datasets create -p /path/to/dataset`

##### Create a new dataset version

```
usage: kaggle datasets version [-h] -m VERSION_NOTES [-p FOLDER] [-q] [-t]
                               [-r {skip,zip,tar}] [-d]

required arguments:
  -m VERSION_NOTES, --message VERSION_NOTES
                        Message describing the new version

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special dataset-metadata.json file (https://github.com/Kaggle/kaggle-api/wiki/Dataset-Metadata). Defaults to current working directory
  -q, --quiet           Suppress printing information about the upload/download progress
  -t, --keep-tabular    Do not convert tabular files to CSV (default is to convert)
  -r {skip,zip,tar}, --dir-mode {skip,zip,tar}
                        What to do with directories: "skip" - ignore; "zip" - compressed upload; "tar" - uncompressed upload
  -d, --delete-old-versions
                        Delete old versions of this dataset
```

Example:

`kaggle datasets version -p /path/to/dataset -m "Updated data"`


##### Download metadata for an existing dataset

```
usage: kaggle datasets metadata [-h] [-p PATH] [dataset]

optional arguments:
  -h, --help            show this help message and exit
  dataset               Dataset URL suffix in format <owner>/<dataset-name> (use "kaggle datasets list" to show options)
  -p PATH, --path PATH  Location to download dataset metadata to. Defaults to current working directory
```

Example:

`kaggle datasets metadata -p /path/to/download zillow/zecon`


##### Get dataset creation status 

```
usage: kaggle datasets status [-h] [dataset]

optional arguments:
  -h, --help  show this help message and exit
  dataset     Dataset URL suffix in format <owner>/<dataset-name> (use "kaggle datasets list" to show options)
```

Example:

`kaggle datasets status zillow/zecon`


### Kernels

The API supports the following commands for Kaggle Kernels.

```
usage: kaggle kernels [-h] {list,init,push,pull,output,status} ...

optional arguments:
  -h, --help            show this help message and exit

commands:
  {list,init,push,pull,output,status}
    list                List available kernels
    init                Initialize metadata file for a kernel
    push                Push new code to a kernel and run the kernel
    pull                Pull down code from a kernel
    output              Get data output from the latest kernel run
    status              Display the status of the latest kernel run
```

##### List kernels

```
usage: kaggle kernels list [-h] [-m] [-p PAGE] [--page-size PAGE_SIZE] [-s SEARCH] [-v]
                           [--parent PARENT] [--competition COMPETITION]
                           [--dataset DATASET]
                           [--user USER] [--language LANGUAGE]
                           [--kernel-type KERNEL_TYPE]
                           [--output-type OUTPUT_TYPE] [--sort-by SORT_BY]

optional arguments:
  -h, --help            show this help message and exit
  -m, --mine            Display only my items
  -p PAGE, --page PAGE  Page number for results paging. Page size is 20 by default
  --page-size PAGE_SIZE Number of items to show on a page. Default size is 20, max is 100
  -s SEARCH, --search SEARCH
                        Term(s) to search for
  -v, --csv             Print results in CSV format (if not set print in table format)
  --parent PARENT       Find children of the specified parent kernel
  --competition COMPETITION
                        Find kernels for a given competition
  --dataset DATASET     Find kernels for a given dataset
  --user USER           Find kernels created by a given user
  --language LANGUAGE   Specify the language the kernel is written in. Default is 'all'. Valid options are 'all', 'python', 'r', 'sqlite', and 'julia'
  --kernel-type KERNEL_TYPE
                        Specify the type of kernel. Default is 'all'. Valid options are 'all', 'script', and 'notebook'
  --output-type OUTPUT_TYPE
                        Search for specific kernel output types. Default is 'all'. Valid options are 'all', 'visualizations', and 'data'
  --sort-by SORT_BY     Sort list results. Default is 'hotness'.  Valid options are 'hotness', 'commentCount', 'dateCreated', 'dateRun', 'relevance', 'scoreAscending', 'scoreDescending', 'viewCount', and 'voteCount'. 'relevance' is only applicable if a search term is specified.
```

Example:

`kaggle kernels list -s titanic`

`kaggle kernels list --language python`

##### Initialize metadata file for a kernel

```
usage: kaggle kernels init [-h] [-p FOLDER]

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special kernel-metadata.json file (https://github.com/Kaggle/kaggle-api/wiki/Kernel-Metadata). Defaults to current working directory
```

Example:

`kaggle kernels init -p /path/to/kernel`
  
##### Push a kernel

```
usage: kaggle kernels push [-h] -p FOLDER

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special kernel-metadata.json file (https://github.com/Kaggle/kaggle-api/wiki/Kernel-Metadata). Defaults to current working directory
```

Example:

`kaggle kernels push -p /path/to/kernel`

##### Pull a kernel

```
usage: kaggle kernels pull [-h] [-p PATH] [-w] [-m] [kernel]

optional arguments:
  -h, --help            show this help message and exit
  kernel                Kernel URL suffix in format <owner>/<kernel-name> (use "kaggle kernels list" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  -m, --metadata        Generate metadata when pulling kernel
```

Example:

`kaggle kernels pull rtatman/list-of-5-day-challenges -p /path/to/dest`

##### Retrieve a kernel's output

```
usage: kaggle kernels output [-h] [-p PATH] [-w] [-o] [-q] [kernel]

optional arguments:
  -h, --help            show this help message and exit
  kernel                Kernel URL suffix in format <owner>/<kernel-name> (use "kaggle kernels list" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about the upload/download progress
```

Example:

`kaggle kernels output mrisdal/exploring-survival-on-the-titanic -p /path/to/dest`

##### Get the status of the latest kernel run

```
usage: kaggle kernels status [-h] [kernel]

optional arguments:
  -h, --help  show this help message and exit
  kernel      Kernel URL suffix in format <owner>/<kernel-name> (use "kaggle kernels list" to show options)
```

Example:

`kaggle kernels status mrisdal/exploring-survival-on-the-titanic`

### Config

The API supports the following commands for configuration.

```
usage: kaggle config [-h] {view,set,unset} ...

optional arguments:
  -h, --help        show this help message and exit

commands:
  {view,set,unset}
    view            View current config values
    set             Set a configuration value
    unset           Clear a configuration value
```

##### View current config values

```
usage: kaggle config path [-h] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  folder where file(s) will be downloaded, defaults to current working directory
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
                        - path: Folder where file(s) will be downloaded, defaults to current working directory
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

The Kaggle API is released under the [Apache 2.0 license](LICENSE).
