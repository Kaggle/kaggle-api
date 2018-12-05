Changelog
====

#### 1.5.1.1
Release date: 12/5/18
* Add missing cli option for dataset subfolders

#### 1.5.1
Release date: 12/5/18
* Allow custom ca_cert files
* Support uplodaing datasets with subfolders
* Fix kaggle.json permissions warning

#### 1.5.0
Release date: 10/19/18
* Update API to work with new competitions submissions backend.  This change will force old API clients to update.  
* Update error message when config file is not found.

#### 1.4.7.1
Release date: 8/28/18
* Fix host

#### 1.4.7
Release date: 8/28/18
* Make dataset version `-p` argument actually optinal
* Don't require the `resources` field when updating a dataset
* Don't automatically unzip datasets
* Add an unzip option for dataset downloads
* Add validation for kernel title and slug length
* Give a warning if kernel title does not resolve to the specified slug
* Show kernel version number after pushing
* Respect `code_file` value in kernel metadata when pulling kernels

#### 1.4.6
Release date: 8/7/18
* Allow setting config values through environmental variables

#### 1.4.5
Release date: 8/1/18
* Add error if dataset metadata repeats files

#### 1.4.4
Release date: 7/30/18
* Fix issue with reading kernel metadata

#### 1.4.3
Release date: 7/30/18
* Add more competitions list options
* Add more datasets list options
* Add a couple more fields to kernels list display
* Add support for kernel and dataset ID's
* Allow generating metadata for an existing dataset
* Fix issue with downloading from datasets whose titles don't match their slugs
* Use kernel slug as filename for kernel output
* Make upload and download directory default to current working directory 
* Use a default username on downloading kernel or dataset data if none is specified
* Support extended data types on datasets
* Stop requiring `-c`, `-d`, and `-k` arguments
* Don't require `resources` field in dataset metadata

#### 1.4.2
Release date: 7/20/18
* Validate dataset slug and title length before uploading
* Fix issue with dataset metadata file detection
* Cleaned up KeyboardInterrupt errors
* Validate all specified files in a dataset exist prior to uploading
* Make ApiExceptions (slightly) less ugly

#### 1.4.1
Release date: 7/20/18
* Add python 3.7 compatibility

#### 1.4.0
Release date: 7/19/18
* Add kernels support
** List and search kernels
** Push kernels code
** Pull kernels code
** Download kernel output
** Get latest kernel run status

#### 1.3.12
Release date: 6/25/18
* Allow setting a `'KAGGLE_CONFIG_DIR'` environmental token
* Return metadata file after creating
* Alert users that dataset creation takes time

#### 1.3.11.1
* Fix other invalid tags check

#### 1.3.11
Release date: 6/12/18
* Improve version check
* Fix invalid tags check

#### 1.3.10
Release date: 6/10/18
* Restrict urllib3's version due to requests dependency problem

#### 1.3.9.1
Release date: 6/9/18
* Fix bug with competitions submissions.

#### 1.3.9
Release date: 6/8/18
* Improve error message for closed competitions
* Remove stacktrace on errors
* Print any invalid tags
* Warn if there are no competition files to download
* Implement resumable uploads
* Add subtitle metadata to dataset uploads
* Add progress bars for uploads and downloads
* Add command for downloading competitions leaderboard
* Add command for viewing the top of the leaderboard

#### 1.3.8
Release date: 5/18/18
* Add option to delete all previous dataset versions

#### 1.3.7
Release date: 5/18/18
* Add aliases for subcommands (ex. `kaggle c` is the same thing as `kaggle competitions`)
* Add version command
* Show full download path for files
* Remove file size limitation from uploads

#### 1.3.6
Release date: 5/7/18
* Give the option to add tags to datasets.
  * Known limitiation - you cannot delete tags through the API.  Those changes must be done through the website.

#### 1.3.5
Release date: 5/4/18
* Fix schema declaration in dataset resources

#### 1.3.4
Release date: 4/30/18
* Rename `columns` to `fields`

#### 1.3.3
Release date: 4/26/18
* Fix UnicodeEncodeError for certain datasets
* Include Swagger yaml and config files

#### 1.3.2.1
Release date: 4/24/18
* Fix bug with column metadata

#### 1.3.2
Release date: 4/24/18
* Give the option to specify a schema for uploaded datasets
* Give the option to set the dataset description during updates

#### 1.3.1
Release date: 4/19/18
* Give the option to set dataset file descriptions
* Give the option to not convert tabular datasets to csv

#### 1.3.0
Release date: 4/18/18

* Give the option to set the dataset description during creation

#### 1.2.1
Release date: 4/17/18

* [Issue #5](https://github.com/Kaggle/kaggle-api/issues/5) -  Reformat code for consistency and to align with [Google's python coding style](https://google.github.io/styleguide/pyguide.html).  Most of the changes are cosmetic, but most cases of `camelCasing` other than class names have been changed to `snake_case`.  This is a breaking change for anyone directly using the python code rather than simply using the command line.
