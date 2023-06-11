# Test Service 

Api for test servise

### Structure 
```
TestService 
│   
└───api                                 # main package
|   |
|   └─── api                            # main application
|   |    |   __init__.py                # package file
|   |    |   asgi.py                    # asgi server conf
|   |    |   settings.py                # settings for development 
|   |    |   urls.py                    # urls this application
|   |    |   wsgi.py                    # wsgi server conf 
|   |
|   └───core                            # app with test functional
|   |
|   |   __init__.py                     # package file
|   |   admin.py                        # admin's file
|   |   apps.py                         # config
|   |   managers.py                     # Custom user manager        
|   |   models.py                       # models this app
|   |   permissions.py                  # custom permissions
|   |   routers.py                      # routes this application
|   |   serializers.py                  # serializers
|   |   urls.py                         # routes this application
|   |   views.py                        # all wiews
|   |   viewsets.py                     # This viewset automatically provides actions for custom user
|   └───tests                           # test endpoints
|   |   |
|   |   |   __init__.py
|   |   |   test_endpoints.py
|   |
|   |   manage.py                       # main file
|
|   .gitignore                          # this file consist ignored files
|   poetry.lock                         # poetry lock file
|   poetry.toml                         # config poetry packges
|   README.md                           # description file
```

### load test data

load test themes
```bash
$ cd api
$ python manage.py loaddata core_test.csv
```
load test questions
```bash
$ cd api
$ python manage.py loaddata core_question.csv
```
### Api description

`/` - Home page

`admin/` - administration page

`api/questions/`

**Methods**: GET, HEAD, OPTIONS

**Return type**: json object

`api/questions/<int:pk>/`   

**Methods**: GET, HEAD, OPTIONS

**Return type**: json object

`api/themes/` 

**Methods**: GET, HEAD, OPTIONS

**Return type**: json object

`api/themes/<int:pk>/`

**Methods**: GET, HEAD, OPTIONS

**Return type**: json object

`api/answer/<int:pk>/`

**Methods**: GET, HEAD, OPTIONS

**Return type**: json object

`api/statistic/<int:id>/`

**Methods**: GET, HEAD, OPTIONS

**Return type**: json object

## Run test

```bash
pytest .
```

## LICENSE
MIT