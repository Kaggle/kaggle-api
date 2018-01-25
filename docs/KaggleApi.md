# kaggle.KaggleApi

All URIs are relative to *https://www.kaggle.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**competitions_data_download_file**](KaggleApi.md#competitions_data_download_file) | **GET** /competitions/data/download/{id}/{fileName} | Download competition data file
[**competitions_data_list_files**](KaggleApi.md#competitions_data_list_files) | **GET** /competitions/data/list/{id} | List competition data files
[**competitions_list**](KaggleApi.md#competitions_list) | **GET** /competitions/list | List competitions
[**competitions_submissions_list**](KaggleApi.md#competitions_submissions_list) | **GET** /competitions/submissions/list/{id} | List competition submissions
[**competitions_submissions_submit**](KaggleApi.md#competitions_submissions_submit) | **POST** /competitions/submissions/submit/{id} | Submit to competition
[**competitions_submissions_upload**](KaggleApi.md#competitions_submissions_upload) | **POST** /competitions/submissions/upload/{guid}/{contentLength}/{lastModifiedDateUtc} | Upload competition submission file
[**competitions_submissions_url**](KaggleApi.md#competitions_submissions_url) | **POST** /competitions/submissions/url/{contentLength}/{lastModifiedDateUtc} | Generate competition submission URL
[**datasets_download_file**](KaggleApi.md#datasets_download_file) | **GET** /datasets/download/{ownerSlug}/{datasetSlug}/{fileName} | Download dataset file
[**datasets_list**](KaggleApi.md#datasets_list) | **GET** /datasets/list | List datasets
[**datasets_list_files**](KaggleApi.md#datasets_list_files) | **GET** /datasets/list/{ownerSlug}/{datasetSlug} | List dataset files


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

# **competitions_data_list_files**
> Result competitions_data_list_files(id)

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

try:
    # List competition data files
    api_response = api_instance.competitions_data_list_files(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_data_list_files: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_list**
> Result competitions_list(page=page, search=search)

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
page = 1 # int | Page number (optional) (default to 1)
search = '' # str | Search terms (optional) (default to )

try:
    # List competitions
    api_response = api_instance.competitions_list(page=page, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
last_modified_date_utc = 56 # int | Last modified date of file in milliseconds since epoch in UTC

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
 **last_modified_date_utc** | **int**| Last modified date of file in milliseconds since epoch in UTC | 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **competitions_submissions_url**
> Result competitions_submissions_url(content_length, last_modified_date_utc, file_name=file_name)

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
content_length = 56 # int | Content length of file in bytes
last_modified_date_utc = 56 # int | Last modified date of file in milliseconds since epoch in UTC
file_name = 'file_name_example' # str | Competition submission file name (optional)

try:
    # Generate competition submission URL
    api_response = api_instance.competitions_submissions_url(content_length, last_modified_date_utc, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->competitions_submissions_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_length** | **int**| Content length of file in bytes | 
 **last_modified_date_utc** | **int**| Last modified date of file in milliseconds since epoch in UTC | 
 **file_name** | **str**| Competition submission file name | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

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
> Result datasets_list(page=page, search=search)

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
page = 1 # int | Page number (optional) (default to 1)
search = '' # str | Search terms (optional) (default to )

try:
    # List datasets
    api_response = api_instance.datasets_list(page=page, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **datasets_list_files**
> Result datasets_list_files(owner_slug, dataset_slug)

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

try:
    # List dataset files
    api_response = api_instance.datasets_list_files(owner_slug, dataset_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KaggleApi->datasets_list_files: %s\n" % e)
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

