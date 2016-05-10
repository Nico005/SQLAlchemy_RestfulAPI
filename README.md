
## Integration SQLAlchemy ORM with Restframework

integrate the awesome frameworks Django REST Framework and SQLAlchemy


``` 
install packages of requirements.txt
```


### SETTINGS (DATABASE CONFIG)
Configuration connection to database MySQL or etc 

[ Configuration Code](https://github.com/RaminFP/SQLAlchemy_RestfulAPI/blob/master/config/database/dbconfig.py) 

```python

class MySQLInfo:

    IPADDRESSDATABASE = '127.0.0.1'  # Remote DB Address
    USERNAME   = 'root'              # Username DB
    PASSWORD   = ''                  # Password 
    DBNAME     = 'restful'           # DB Name (Here example restful)   
    PORT       = '3306'              # Defualt post MySQL    
```
 
if you need mapping tables with SQLAlchemy you should set `CONNECTOR=True` if mapping is done with SQLAlchemy set `False` 
 
 
### APP (Controllers,APIs,MODELS)

##### Controllers (Render Files(HTML,JS,IMAGE , ...)) :

[ Actions Controller ](https://github.com/RaminFP/SQLAlchemy_RestfulAPI/tree/master/app/controllers) 

##### APIs (JsonRender , Methods , Authenticate) : 


[ Actions API Service ](https://github.com/RaminFP/SQLAlchemy_RestfulAPI/tree/master/app/apis) 

###### GET 

```shell
curl -X GET http://127.0.0.1:8000/
```

###### POST

```shell
curl -X POST http://127.0.0.1:8000/api/insert  -v -H "Accept: application/json" -d "Username=test&Name=test&Email=test@email.com&Date=null&Password=1234"
```

###### PUT

```shell
curl -X PUT http://127.0.0.1:8000/api/update/2 -d "Username=test&Name=test1&Email=rarrrrn@bgg.gmail.com&Date=4321&Password=1234"
```

###### DELETE 

```shell
curl -X DELETE http://127.0.0.1:8000/api/delete/1
```

###### SEARCH 

```shell
curl -X GET http://127.0.0.1:8000/api/search/1
```

###### SEARCH WITH LIKE :

```shell
curl -X GET http://127.0.0.1:8000/api/username/test
```


###### Authenticate (Django Auth Users )

[ Authenticate API Service ](https://github.com/RaminFP/SQLAlchemy_RestfulAPI/blob/master/app/apis/HomeAPI.py) 


##### MODELS (SQLAlchemy Models )

[ Model API Service ](https://github.com/RaminFP/SQLAlchemy_RestfulAPI/tree/master/app/models) 



### SERIALIZER (Serializer Models SQLAlchemy )

[ Serializer Model API Service ](https://github.com/RaminFP/SQLAlchemy_RestfulAPI/tree/master/serialization) 


### TODO



