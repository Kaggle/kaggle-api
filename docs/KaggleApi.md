# kaggle.KaggleApi

All URIs are relative to *https://www.kaggle.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**competition_download_leaderboard**](KaggleApi.md#competition_download_leaderboard) | **GET** /competitions/{id}/leaderboard/download | Download competition leaderboard
[**competition_view_leaderboard**](KaggleApi.md#competition_view_leaderboard) | **GET** /competitions/{id}/leaderboard/view | VIew competition leaderboard
[**competitions_data_download_file**](KaggleApi.md#competitions_data_download_file) | **GET** /competitions/data/download/{id}/{fileName} | Download competition data file
[**competitions_data_download_files**](KaggleApi.md#competitions_data_download_files) | **GET** /competitions/data/download-all/{id} | Download all competition data files
[**competitions_data_list_files**](KaggleApi.md#competitions_data_list_files) | **GET** /competitions/data/list/{id} | List competition data files
[**competitions_list**](KaggleApi.md#competitions_list) | **GET** /competitions/list | List competitions
[**competitions_submissions_list**](KaggleApi.md#competitions_submissions_list) | **GET** /competitions/submissions/list/{id} | List competition submissions
[**competitions_submissions_submit**](KaggleApi.md#competitions_submissions_submit) | **POST** /competitions/submissions/submit/{id} | Submit to competition
[**competitions_submissions_upload**](KaggleApi.md#competitions_submissions_upload) | **POST** /competitions/submissions/upload/{guid}/{contentLength}/{lastModifiedDateUtc} | Upload competition submission file
[**competitions_submissions_url**](KaggleApi.md#competitions_submissions_url) | **POST** /competitions/{id}/submissions/url/{contentLength}/{lastModifiedDateUtc} | Generate competition submission URL
[**create_inbox_file**](KaggleApi.md#create_inbox_file) | **POST** /inbox/files/create | Creates (aka \&quot;drops\&quot;) a new file into the inbox.
[**datasets_create_new**](KaggleApi.md#datasets_create_new) | **POST** /datasets/create/new | Create a new dataset
[**datasets_create_version**](KaggleApi.md#datasets_create_version) | **POST** /datasets/create/version/{ownerSlug}/{datasetSlug} | Create a new dataset version
[**datasets_create_version_by_id**](KaggleApi.md#datasets_create_version_by_id) | **POST** /datasets/create/version/{id} | Create a new dataset version by id
[**datasets_download**](KaggleApi.md#datasets_download) | **GET** /datasets/download/{ownerSlug}/{datasetSlug} | Download dataset file
[**datasets_download_file**](KaggleApi.md#datasets_download_file) | **GET** /datasets/download/{ownerSlug}/{datasetSlug}/{fileName} | Download dataset file
[**datasets_list**](KaggleApi.md#datasets_list) | **GET** /datasets/list | List datasets
[**datasets_list_files**](KaggleApi.md#datasets_list_files) | **GET** /datasets/list/{ownerSlug}/{datasetSlug} | List dataset files
[**datasets_status**](KaggleApi.md#datasets_status) | **GET** /datasets/status/{ownerSlug}/{datasetSlug} | Get dataset creation status
[**delete_model**](KaggleApi.md#delete_model) | **POST** /models/{ownerSlug}/{modelSlug}/delete | Delete a model
[**delete_model_instance**](KaggleApi.md#delete_model_instance) | **POST** /models/{ownerSlug}/{modelSlug}/{framework}/{instanceSlug}/delete | Delete a model instance
[**delete_model_instance_version**](KaggleApi.md#delete_model_instance_version) | **POST** /models/{ownerSlug}/{modelSlug}/{framework}/{instanceSlug}/{versionNumber}/delete | Delete a model instance version
[**get_model**](KaggleApi.md#get_model) | **GET** /models/{ownerSlug}/{modelSlug}/get | Get a model
[**get_model_instance**](KaggleApi.md#get_model_instance) | **GET** /models/{ownerSlug}/{modelSlug}/{framework}/{instanceSlug}/get | Get a model instance
[**kernel_output**](KaggleApi.md#kernel_output) | **GET** /kernels/output | Download the latest output from a kernel
[**kernel_pull**](KaggleApi.md#kernel_pull) | **GET** /kernels/pull | Pull the latest code from a kernel
[**kernel_push**](KaggleApi.md#kernel_push) | **POST** /kernels/push | Push a new kernel version.  Can be used to create a new kernel and update an existing one.
[**kernel_status**](KaggleApi.md#kernel_status) | **GET** /kernels/status | Get the status of the latest kernel version
[**kernels_list**](KaggleApi.md#kernels_list) | **GET** /kernels/list | List kernels
[**kernels_list_files**](KaggleApi.md#kernels_list_files) | **GET** /kernels/files | List kernel files
[**metadata_get**](KaggleApi.md#metadata_get) | **GET** /datasets/metadata/{ownerSlug}/{datasetSlug} | Get the metadata for a dataset
[**metadata_post**](KaggleApi.md#metadata_post) | **POST** /datasets/metadata/{ownerSlug}/{datasetSlug} | Update the metadata for a dataset
[**model_instance_files**](KaggleApi.md#model_instance_files) | **GET** /models/{ownerSlug}/{modelSlug}/{framework}/{instanceSlug}/files | List model instance files for the current version
[**model_instance_version_files**](KaggleApi.md#model_instance_version_files) | **GET** /models/{ownerSlug}/{modelSlug}/{framework}/{instanceSlug}/{versionNumber}/files | List model instance version files
[**model_instance_versions_download**](KaggleApi.md#model_instance_versions_download) | **GET** /models/{ownerSlug}/{modelSlug}/{framework}/{instanceSlug}/{versionNumber}/download | Download model instance version files
[**models_create_instance**](KaggleApi.md#models_create_instance) | **POST** /models/{ownerSlug}/{modelSlug}/create/instance | Create a new model instance
[**models_create_instance_version**](KaggleApi.md#models_create_instance_version) | **POST** /models/{ownerSlug}/{modelSlug}/{framework}/{instanceSlug}/create/version | Create a new model instance version
[**models_create_new**](KaggleApi.md#models_create_new) | **POST** /models/create/new | Create a new model
[**models_list**](KaggleApi.md#models_list) | **GET** /models/list | Lists models
[**update_model**](KaggleApi.md#update_model) | **POST** /models/{ownerSlug}/{modelSlug}/update | Update a model
[**update_model_instance**](KaggleApi.md#update_model_instance) | **POST** /models/{ownerSlug}/{modelSlug}/{framework}/{instanceSlug}/update | Update a model
[**upload_file**](KaggleApi.md#upload_file) | **POST** /blobs/upload | Start uploading a file


# **competition_download_leaderboard**
> Result competition_download_leaderboard(id)

Download competition leaderboard

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
id = 'id_example' # str | Competition name

try:
    # Download competition leaderboard
    api_response = api_instance.competition_download_leaderboard(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competition_download_leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Competition name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competition_view_leaderboard**
> Result competition_view_leaderboard(id)

VIew competition leaderboard

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
id = 'id_example' # str | Competition name

try:
    # VIew competition leaderboard
    api_response = api_instance.competition_view_leaderboard(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competition_view_leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Competition name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_data_download_file**
> Result competitions_data_download_file(id, file_name)

Download competition data file

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
id = 'id_example' # str | Competition name
file_name = 'file_name_example' # str | Competition name

try:
    # Download competition data file
    api_response = api_instance.competitions_data_download_file(id, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_data_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Competition name | 
 **file_name** | **str**| Competition name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_data_download_files**
> Result competitions_data_download_files(id)

Download all competition data files

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
id = 'id_example' # str | Competition name

try:
    # Download all competition data files
    api_response = api_instance.competitions_data_download_files(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_data_download_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Competition name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_data_list_files**
> Result competitions_data_list_files(id, page_token=page_token, page_size=page_size)

List competition data files

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
id = 'id_example' # str | Competition name
page_token = 'page_token_example' # str | Page token for pagination (optional)
page_size = 20 # int | Number of items per page (default 20) (optional) (default to 20)

try:
    # List competition data files
    api_response = api_instance.competitions_data_list_files(id, page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_data_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Competition name | 
 **page_token** | **str**| Page token for pagination | [optional] 
 **page_size** | **int**| Number of items per page (default 20) | [optional] [default to 20]

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_list**
> Result competitions_list(group=group, category=category, sort_by=sort_by, page=page, search=search)

List competitions

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
group = 'general' # str | Filter competitions by a particular group (optional) (default to general)
category = 'all' # str | Filter competitions by a particular category (optional) (default to all)
sort_by = 'latestDeadline' # str | Sort the results (optional) (default to latestDeadline)
page = 1 # int | Page number (optional) (default to 1)
search = '' # str | Search terms (optional) (default to )

try:
    # List competitions
    api_response = api_instance.competitions_list(group=group, category=category, sort_by=sort_by, page=page, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Filter competitions by a particular group | [optional] [default to general]
 **category** | **str**| Filter competitions by a particular category | [optional] [default to all]
 **sort_by** | **str**| Sort the results | [optional] [default to latestDeadline]
 **page** | **int**| Page number | [optional] [default to 1]
 **search** | **str**| Search terms | [optional] [default to ]

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_submissions_list**
> Result competitions_submissions_list(id, page=page)

List competition submissions

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
id = 'id_example' # str | Competition name
page = 1 # int | Page number (optional) (default to 1)

try:
    # List competition submissions
    api_response = api_instance.competitions_submissions_list(id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_submissions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Competition name | 
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_submissions_submit**
> Result competitions_submissions_submit(blob_file_tokens, submission_description, id)

Submit to competition

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
blob_file_tokens = 'blob_file_tokens_example' # str | Token identifying location of uploaded submission file
submission_description = 'submission_description_example' # str | Description of competition submission
id = 'id_example' # str | Competition name

try:
    # Submit to competition
    api_response = api_instance.competitions_submissions_submit(blob_file_tokens, submission_description, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_submissions_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_file_tokens** | **str**| Token identifying location of uploaded submission file | 
 **submission_description** | **str**| Description of competition submission | 
 **id** | **str**| Competition name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_submissions_upload**
> Result competitions_submissions_upload(file, guid, content_length, last_modified_date_utc)

Upload competition submission file

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
file = '/path/to/file.txt' # file | Competition submission file
guid = 'guid_example' # str | Location where submission should be uploaded
content_length = 56 # int | Content length of file in bytes
last_modified_date_utc = 56 # int | Last modified date of file in seconds since epoch in UTC

try:
    # Upload competition submission file
    api_response = api_instance.competitions_submissions_upload(file, guid, content_length, last_modified_date_utc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_submissions_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Competition submission file | 
 **guid** | **str**| Location where submission should be uploaded | 
 **content_length** | **int**| Content length of file in bytes | 
 **last_modified_date_utc** | **int**| Last modified date of file in seconds since epoch in UTC | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_submissions_url**
> Result competitions_submissions_url(id, content_length, last_modified_date_utc, file_name=file_name)

Generate competition submission URL

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
id = 'id_example' # str | Competition name, as it appears in the competition's URL
content_length = 56 # int | Content length of file in bytes
last_modified_date_utc = 56 # int | Last modified date of file in seconds since epoch in UTC
file_name = 'file_name_example' # str | Competition submission file name (optional)

try:
    # Generate competition submission URL
    api_response = api_instance.competitions_submissions_url(id, content_length, last_modified_date_utc, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_submissions_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Competition name, as it appears in the competition&#39;s URL | 
 **content_length** | **int**| Content length of file in bytes | 
 **last_modified_date_utc** | **int**| Last modified date of file in seconds since epoch in UTC | 
 **file_name** | **str**| Competition submission file name | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inbox_file**
> Result create_inbox_file(create_inbox_file_request)

Creates (aka \"drops\") a new file into the inbox.

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
create_inbox_file_request = kaggle.CreateInboxFileRequest() # CreateInboxFileRequest | 

try:
    # Creates (aka \"drops\") a new file into the inbox.
    api_response = api_instance.create_inbox_file(create_inbox_file_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->create_inbox_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inbox_file_request** | [**CreateInboxFileRequest**](CreateInboxFileRequest.md)|  | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_create_new**
> Result datasets_create_new(dataset_new_request)

Create a new dataset

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
dataset_new_request = kaggle.DatasetNewRequest() # DatasetNewRequest | Information for creating a new dataset

try:
    # Create a new dataset
    api_response = api_instance.datasets_create_new(dataset_new_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_create_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_new_request** | [**DatasetNewRequest**](DatasetNewRequest.md)| Information for creating a new dataset | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_create_version**
> Result datasets_create_version(owner_slug, dataset_slug, dataset_new_version_request)

Create a new dataset version

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Dataset owner
dataset_slug = 'dataset_slug_example' # str | Dataset name
dataset_new_version_request = kaggle.DatasetNewVersionRequest() # DatasetNewVersionRequest | Information for creating a new dataset version

try:
    # Create a new dataset version
    api_response = api_instance.datasets_create_version(owner_slug, dataset_slug, dataset_new_version_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_create_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Dataset owner | 
 **dataset_slug** | **str**| Dataset name | 
 **dataset_new_version_request** | [**DatasetNewVersionRequest**](DatasetNewVersionRequest.md)| Information for creating a new dataset version | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_create_version_by_id**
> Result datasets_create_version_by_id(id, dataset_new_version_request)

Create a new dataset version by id

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
id = 56 # int | Dataset ID
dataset_new_version_request = kaggle.DatasetNewVersionRequest() # DatasetNewVersionRequest | Information for creating a new dataset version

try:
    # Create a new dataset version by id
    api_response = api_instance.datasets_create_version_by_id(id, dataset_new_version_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_create_version_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Dataset ID | 
 **dataset_new_version_request** | [**DatasetNewVersionRequest**](DatasetNewVersionRequest.md)| Information for creating a new dataset version | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_download**
> Result datasets_download(owner_slug, dataset_slug, dataset_version_number=dataset_version_number)

Download dataset file

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Dataset owner
dataset_slug = 'dataset_slug_example' # str | Dataset name
dataset_version_number = 'dataset_version_number_example' # str | Dataset version number (optional)

try:
    # Download dataset file
    api_response = api_instance.datasets_download(owner_slug, dataset_slug, dataset_version_number=dataset_version_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Dataset owner | 
 **dataset_slug** | **str**| Dataset name | 
 **dataset_version_number** | **str**| Dataset version number | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: file

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_download_file**
> Result datasets_download_file(owner_slug, dataset_slug, file_name, dataset_version_number=dataset_version_number)

Download dataset file

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Dataset owner
dataset_slug = 'dataset_slug_example' # str | Dataset name
file_name = 'file_name_example' # str | File name
dataset_version_number = 'dataset_version_number_example' # str | Dataset version number (optional)

try:
    # Download dataset file
    api_response = api_instance.datasets_download_file(owner_slug, dataset_slug, file_name, dataset_version_number=dataset_version_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Dataset owner | 
 **dataset_slug** | **str**| Dataset name | 
 **file_name** | **str**| File name | 
 **dataset_version_number** | **str**| Dataset version number | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: file

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_list**
> Result datasets_list(group=group, sort_by=sort_by, size=size, filetype=filetype, license=license, tagids=tagids, search=search, user=user, page=page, max_size=max_size, min_size=min_size)

List datasets

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
group = 'public' # str | Display datasets by a particular group (optional) (default to public)
sort_by = 'hottest' # str | Sort the results (optional) (default to hottest)
size = 'all' # str | (DEPRECATED). Please use --max-size and --min-size to filter dataset sizes. (optional) (default to all)
filetype = 'all' # str | Display datasets of a specific file type (optional) (default to all)
license = 'all' # str | Display datasets with a specific license (optional) (default to all)
tagids = 'tagids_example' # str | A comma separated list of tags to filter by (optional)
search = '' # str | Search terms (optional) (default to )
user = 'user_example' # str | Display datasets by a specific user or organization (optional)
page = 1 # int | Page number (optional) (default to 1)
max_size = 789 # int | Max Dataset Size (bytes) (optional)
min_size = 789 # int | Max Dataset Size (bytes) (optional)

try:
    # List datasets
    api_response = api_instance.datasets_list(group=group, sort_by=sort_by, size=size, filetype=filetype, license=license, tagids=tagids, search=search, user=user, page=page, max_size=max_size, min_size=min_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Display datasets by a particular group | [optional] [default to public]
 **sort_by** | **str**| Sort the results | [optional] [default to hottest]
 **size** | **str**| (DEPRECATED). Please use --max-size and --min-size to filter dataset sizes. | [optional] [default to all]
 **filetype** | **str**| Display datasets of a specific file type | [optional] [default to all]
 **license** | **str**| Display datasets with a specific license | [optional] [default to all]
 **tagids** | **str**| A comma separated list of tags to filter by | [optional] 
 **search** | **str**| Search terms | [optional] [default to ]
 **user** | **str**| Display datasets by a specific user or organization | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **max_size** | **int**| Max Dataset Size (bytes) | [optional] 
 **min_size** | **int**| Max Dataset Size (bytes) | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_list_files**
> Result datasets_list_files(owner_slug, dataset_slug, dataset_version_number=dataset_version_number, page_token=page_token, page_size=page_size)

List dataset files

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Dataset owner
dataset_slug = 'dataset_slug_example' # str | Dataset name
dataset_version_number = 'dataset_version_number_example' # str | Dataset version number (optional)
page_token = 'page_token_example' # str | Page token for pagination (optional)
page_size = 20 # int | Number of items per page (default 20) (optional) (default to 20)

try:
    # List dataset files
    api_response = api_instance.datasets_list_files(owner_slug, dataset_slug, dataset_version_number=dataset_version_number, page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Dataset owner | 
 **dataset_slug** | **str**| Dataset name | 
 **dataset_version_number** | **str**| Dataset version number | [optional] 
 **page_token** | **str**| Page token for pagination | [optional] 
 **page_size** | **int**| Number of items per page (default 20) | [optional] [default to 20]

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_status**
> Result datasets_status(owner_slug, dataset_slug)

Get dataset creation status

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Dataset owner
dataset_slug = 'dataset_slug_example' # str | Dataset name

try:
    # Get dataset creation status
    api_response = api_instance.datasets_status(owner_slug, dataset_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Dataset owner | 
 **dataset_slug** | **str**| Dataset name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> Result delete_model(owner_slug, model_slug)

Delete a model

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name

try:
    # Delete a model
    api_response = api_instance.delete_model(owner_slug, model_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->delete_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_instance**
> Result delete_model_instance(owner_slug, model_slug, framework, instance_slug)

Delete a model instance

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name
framework = 'framework_example' # str | Model instance framework
instance_slug = 'instance_slug_example' # str | Model instance slug

try:
    # Delete a model instance
    api_response = api_instance.delete_model_instance(owner_slug, model_slug, framework, instance_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->delete_model_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 
 **framework** | **str**| Model instance framework | 
 **instance_slug** | **str**| Model instance slug | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_instance_version**
> Result delete_model_instance_version(owner_slug, model_slug, framework, instance_slug, version_number)

Delete a model instance version

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name
framework = 'framework_example' # str | Model instance framework
instance_slug = 'instance_slug_example' # str | Model instance slug
version_number = 'version_number_example' # str | Model instance version number

try:
    # Delete a model instance version
    api_response = api_instance.delete_model_instance_version(owner_slug, model_slug, framework, instance_slug, version_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->delete_model_instance_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 
 **framework** | **str**| Model instance framework | 
 **instance_slug** | **str**| Model instance slug | 
 **version_number** | **str**| Model instance version number | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Result get_model(owner_slug, model_slug)

Get a model

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name

try:
    # Get a model
    api_response = api_instance.get_model(owner_slug, model_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_instance**
> Result get_model_instance(owner_slug, model_slug, framework, instance_slug)

Get a model instance

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name
framework = 'framework_example' # str | Model instance framework
instance_slug = 'instance_slug_example' # str | Model instance slug

try:
    # Get a model instance
    api_response = api_instance.get_model_instance(owner_slug, model_slug, framework, instance_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->get_model_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 
 **framework** | **str**| Model instance framework | 
 **instance_slug** | **str**| Model instance slug | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kernel_output**
> Result kernel_output(user_name, kernel_slug)

Download the latest output from a kernel

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
user_name = 'user_name_example' # str | Kernel owner
kernel_slug = 'kernel_slug_example' # str | Kernel name

try:
    # Download the latest output from a kernel
    api_response = api_instance.kernel_output(user_name, kernel_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->kernel_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Kernel owner | 
 **kernel_slug** | **str**| Kernel name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kernel_pull**
> Result kernel_pull(user_name, kernel_slug)

Pull the latest code from a kernel

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
user_name = 'user_name_example' # str | Kernel owner
kernel_slug = 'kernel_slug_example' # str | Kernel name

try:
    # Pull the latest code from a kernel
    api_response = api_instance.kernel_pull(user_name, kernel_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->kernel_pull: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Kernel owner | 
 **kernel_slug** | **str**| Kernel name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kernel_push**
> Result kernel_push(kernel_push_request)

Push a new kernel version.  Can be used to create a new kernel and update an existing one.

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
kernel_push_request = kaggle.KernelPushRequest() # KernelPushRequest | Information for pushing a new kernel version

try:
    # Push a new kernel version.  Can be used to create a new kernel and update an existing one.
    api_response = api_instance.kernel_push(kernel_push_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->kernel_push: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kernel_push_request** | [**KernelPushRequest**](KernelPushRequest.md)| Information for pushing a new kernel version | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kernel_status**
> Result kernel_status(user_name, kernel_slug)

Get the status of the latest kernel version

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
user_name = 'user_name_example' # str | Kernel owner
kernel_slug = 'kernel_slug_example' # str | Kernel name

try:
    # Get the status of the latest kernel version
    api_response = api_instance.kernel_status(user_name, kernel_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->kernel_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Kernel owner | 
 **kernel_slug** | **str**| Kernel name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kernels_list**
> Result kernels_list(page=page, page_size=page_size, search=search, group=group, user=user, language=language, kernel_type=kernel_type, output_type=output_type, sort_by=sort_by, dataset=dataset, competition=competition, parent_kernel=parent_kernel)

List kernels

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
page_size = 20 # int | Number of items per page (default 20) (optional) (default to 20)
search = '' # str | Search terms (optional) (default to )
group = 'everyone' # str | Display only your kernels (optional) (default to everyone)
user = 'user_example' # str | Display kernels by a particular group (optional)
language = 'all' # str | Display kernels in a specific language (optional) (default to all)
kernel_type = 'all' # str | Display kernels of a specific type (optional) (default to all)
output_type = 'all' # str | Display kernels with a specific output type (optional) (default to all)
sort_by = 'hotness' # str | Sort the results. 'relevance' only works if there is a search query (optional) (default to hotness)
dataset = 'dataset_example' # str | Display kernels using the specified dataset (optional)
competition = 'competition_example' # str | Display kernels using the specified competition (optional)
parent_kernel = 'parent_kernel_example' # str | Display kernels that have forked the specified kernel (optional)

try:
    # List kernels
    api_response = api_instance.kernels_list(page=page, page_size=page_size, search=search, group=group, user=user, language=language, kernel_type=kernel_type, output_type=output_type, sort_by=sort_by, dataset=dataset, competition=competition, parent_kernel=parent_kernel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->kernels_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default 20) | [optional] [default to 20]
 **search** | **str**| Search terms | [optional] [default to ]
 **group** | **str**| Display only your kernels | [optional] [default to everyone]
 **user** | **str**| Display kernels by a particular group | [optional] 
 **language** | **str**| Display kernels in a specific language | [optional] [default to all]
 **kernel_type** | **str**| Display kernels of a specific type | [optional] [default to all]
 **output_type** | **str**| Display kernels with a specific output type | [optional] [default to all]
 **sort_by** | **str**| Sort the results. &#39;relevance&#39; only works if there is a search query | [optional] [default to hotness]
 **dataset** | **str**| Display kernels using the specified dataset | [optional] 
 **competition** | **str**| Display kernels using the specified competition | [optional] 
 **parent_kernel** | **str**| Display kernels that have forked the specified kernel | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kernels_list_files**
> Result kernels_list_files(user_name, kernel_slug, kernel_version_number=kernel_version_number, page_size=page_size, page_token=page_token)

List kernel files

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
user_name = 'user_name_example' # str | Kernel owner
kernel_slug = 'kernel_slug_example' # str | Kernel name
kernel_version_number = 'kernel_version_number_example' # str | Kernel version number (optional)
page_size = 20 # int | Number of items per page (default 20) (optional) (default to 20)
page_token = 'page_token_example' # str | Page token for pagination (optional)

try:
    # List kernel files
    api_response = api_instance.kernels_list_files(user_name, kernel_slug, kernel_version_number=kernel_version_number, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->kernels_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Kernel owner | 
 **kernel_slug** | **str**| Kernel name | 
 **kernel_version_number** | **str**| Kernel version number | [optional] 
 **page_size** | **int**| Number of items per page (default 20) | [optional] [default to 20]
 **page_token** | **str**| Page token for pagination | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_get**
> Result metadata_get(owner_slug, dataset_slug)

Get the metadata for a dataset

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Dataset owner
dataset_slug = 'dataset_slug_example' # str | Dataset name

try:
    # Get the metadata for a dataset
    api_response = api_instance.metadata_get(owner_slug, dataset_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Dataset owner | 
 **dataset_slug** | **str**| Dataset name | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_post**
> Result metadata_post(owner_slug, dataset_slug, settings)

Update the metadata for a dataset

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Dataset owner
dataset_slug = 'dataset_slug_example' # str | Dataset name
settings = kaggle.DatasetUpdateSettingsRequest() # DatasetUpdateSettingsRequest | Dataset metadata to update

try:
    # Update the metadata for a dataset
    api_response = api_instance.metadata_post(owner_slug, dataset_slug, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Dataset owner | 
 **dataset_slug** | **str**| Dataset name | 
 **settings** | [**DatasetUpdateSettingsRequest**](DatasetUpdateSettingsRequest.md)| Dataset metadata to update | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_instance_files**
> Result model_instance_files(owner_slug, model_slug, framework, instance_slug, page_size=page_size, page_token=page_token)

List model instance files for the current version

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name
framework = 'framework_example' # str | Model instance framework
instance_slug = 'instance_slug_example' # str | Model instance slug
page_size = 20 # int | Number of items per page (default 20) (optional) (default to 20)
page_token = 'page_token_example' # str | Page token for pagination (optional)

try:
    # List model instance files for the current version
    api_response = api_instance.model_instance_files(owner_slug, model_slug, framework, instance_slug, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->model_instance_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 
 **framework** | **str**| Model instance framework | 
 **instance_slug** | **str**| Model instance slug | 
 **page_size** | **int**| Number of items per page (default 20) | [optional] [default to 20]
 **page_token** | **str**| Page token for pagination | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_instance_version_files**
> Result model_instance_version_files(owner_slug, model_slug, framework, instance_slug, version_number, page_size=page_size, page_token=page_token)

List model instance version files

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name
framework = 'framework_example' # str | Model instance framework
instance_slug = 'instance_slug_example' # str | Model instance slug
version_number = 'version_number_example' # str | Model instance version number
page_size = 20 # int | Number of items per page (default 20) (optional) (default to 20)
page_token = 'page_token_example' # str | Page token for pagination (optional)

try:
    # List model instance version files
    api_response = api_instance.model_instance_version_files(owner_slug, model_slug, framework, instance_slug, version_number, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->model_instance_version_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 
 **framework** | **str**| Model instance framework | 
 **instance_slug** | **str**| Model instance slug | 
 **version_number** | **str**| Model instance version number | 
 **page_size** | **int**| Number of items per page (default 20) | [optional] [default to 20]
 **page_token** | **str**| Page token for pagination | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_instance_versions_download**
> Result model_instance_versions_download(owner_slug, model_slug, framework, instance_slug, version_number)

Download model instance version files

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name
framework = 'framework_example' # str | Model instance framework
instance_slug = 'instance_slug_example' # str | Model instance slug
version_number = 'version_number_example' # str | Model instance version number

try:
    # Download model instance version files
    api_response = api_instance.model_instance_versions_download(owner_slug, model_slug, framework, instance_slug, version_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->model_instance_versions_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 
 **framework** | **str**| Model instance framework | 
 **instance_slug** | **str**| Model instance slug | 
 **version_number** | **str**| Model instance version number | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: file

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_create_instance**
> Result models_create_instance(owner_slug, model_slug, model_new_instance_request)

Create a new model instance

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model slug
model_new_instance_request = kaggle.ModelNewInstanceRequest() # ModelNewInstanceRequest | Information for creating a new model instance

try:
    # Create a new model instance
    api_response = api_instance.models_create_instance(owner_slug, model_slug, model_new_instance_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->models_create_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model slug | 
 **model_new_instance_request** | [**ModelNewInstanceRequest**](ModelNewInstanceRequest.md)| Information for creating a new model instance | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_create_instance_version**
> Result models_create_instance_version(owner_slug, model_slug, framework, instance_slug, model_instance_new_version_request)

Create a new model instance version

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model slug
framework = 'framework_example' # str | Model instance framework
instance_slug = 'instance_slug_example' # str | Model instance slug
model_instance_new_version_request = kaggle.ModelInstanceNewVersionRequest() # ModelInstanceNewVersionRequest | Information for creating a new model instance version

try:
    # Create a new model instance version
    api_response = api_instance.models_create_instance_version(owner_slug, model_slug, framework, instance_slug, model_instance_new_version_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->models_create_instance_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model slug | 
 **framework** | **str**| Model instance framework | 
 **instance_slug** | **str**| Model instance slug | 
 **model_instance_new_version_request** | [**ModelInstanceNewVersionRequest**](ModelInstanceNewVersionRequest.md)| Information for creating a new model instance version | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_create_new**
> Result models_create_new(model_new_request)

Create a new model

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
model_new_request = kaggle.ModelNewRequest() # ModelNewRequest | Information for creating a new model

try:
    # Create a new model
    api_response = api_instance.models_create_new(model_new_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->models_create_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_new_request** | [**ModelNewRequest**](ModelNewRequest.md)| Information for creating a new model | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list**
> Result models_list(search=search, sort_by=sort_by, owner=owner, page_size=page_size, page_token=page_token)

Lists models

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
search = '' # str | Search terms (optional) (default to )
sort_by = 'hotness' # str | Sort the results (optional) (default to hotness)
owner = 'owner_example' # str | Display models by a specific user or organization (optional)
page_size = 20 # int | Number of items per page (default 20) (optional) (default to 20)
page_token = 'page_token_example' # str | Page token for pagination (optional)

try:
    # Lists models
    api_response = api_instance.models_list(search=search, sort_by=sort_by, owner=owner, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->models_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search terms | [optional] [default to ]
 **sort_by** | **str**| Sort the results | [optional] [default to hotness]
 **owner** | **str**| Display models by a specific user or organization | [optional] 
 **page_size** | **int**| Number of items per page (default 20) | [optional] [default to 20]
 **page_token** | **str**| Page token for pagination | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> Result update_model(owner_slug, model_slug, model_update_request)

Update a model

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name
model_update_request = kaggle.ModelUpdateRequest() # ModelUpdateRequest | Information for updating a model

try:
    # Update a model
    api_response = api_instance.update_model(owner_slug, model_slug, model_update_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 
 **model_update_request** | [**ModelUpdateRequest**](ModelUpdateRequest.md)| Information for updating a model | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model_instance**
> Result update_model_instance(owner_slug, model_slug, framework, instance_slug, model_instance_update_request)

Update a model

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
owner_slug = 'owner_slug_example' # str | Model owner
model_slug = 'model_slug_example' # str | Model name
framework = 'framework_example' # str | Model instance framework
instance_slug = 'instance_slug_example' # str | Model instance slug
model_instance_update_request = kaggle.ModelInstanceUpdateRequest() # ModelInstanceUpdateRequest | Information for updating a model instance

try:
    # Update a model
    api_response = api_instance.update_model_instance(owner_slug, model_slug, framework, instance_slug, model_instance_update_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->update_model_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_slug** | **str**| Model owner | 
 **model_slug** | **str**| Model name | 
 **framework** | **str**| Model instance framework | 
 **instance_slug** | **str**| Model instance slug | 
 **model_instance_update_request** | [**ModelInstanceUpdateRequest**](ModelInstanceUpdateRequest.md)| Information for updating a model instance | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> StartBlobUploadResponse upload_file(start_blob_upload_request)

Start uploading a file

### Example
```python
from __future__ import print_function
import time
import kaggle
from kaggle.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = kaggle.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kaggle.KaggleApi(kaggle.ApiClient(configuration))
start_blob_upload_request = kaggle.StartBlobUploadRequest() # StartBlobUploadRequest | 

try:
    # Start uploading a file
    api_response = api_instance.upload_file(start_blob_upload_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_blob_upload_request** | [**StartBlobUploadRequest**](StartBlobUploadRequest.md)|  | 

### Return type

[**StartBlobUploadResponse**](StartBlobUploadResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

