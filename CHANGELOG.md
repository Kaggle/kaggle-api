Changelog
====

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
