Changelog
====

#### 1.3.9
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
