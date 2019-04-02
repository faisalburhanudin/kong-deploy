# Kong Deploy

Example deployment kong api gateway using docker-compose


## Docker compose stack

In this docker-compose there are 4 services:

1. my-service: for example rest api
2. kong-database: for kong database storage
3. konga: for kong dashboard
4. kong: api gateway

For more detail open docker-compose.yml


## Start services 

Start service one by one, because some service sometime run but not in ready state

```bash
# run kong-database
docker-compose up -d kong-database

# check if kong-database ready for connection
# last output should be something like this
# kong-database_1  | LOG:  database system is ready to accept connections
docker-compose logs kong-database

# run migration
docker-compose up migration

# run kong
docker-compose up -d kong

# check if kong is run successful
curl -i http://localhost:8001/

# rung konga
# after run you can visit http://127.0.0.1:1337 in browser
# WARNING: when create admin user, use long password, if not konga will be error after register
# for complete konga installation open https://github.com/pantsel/konga
# NOTE: when create connection to kong admin use url http://kong:8001/
docker-compose up -d konga

# run my-service
docker-compose up -d my-service

# configure my-service to kong gateway
# if you want step by step, check section below
python deploy.py

```

## Register service to kong step by step

```bash
# add service
python add_service.py

# add a route
python add_route.py


# Check request via gateway
curl -i -X GET --url http://localhost:8000/ --header 'Host: my-service.dev'
```

## Rate limit

```bash
# enable rate limit plugin, in this script 5 request/minute
python enable_ratelimit.py

# check request 6 request
curl -i -X GET --url http://localhost:8000/ --header 'Host: my-service.dev'
curl -i -X GET --url http://localhost:8000/ --header 'Host: my-service.dev'
curl -i -X GET --url http://localhost:8000/ --header 'Host: my-service.dev'
curl -i -X GET --url http://localhost:8000/ --header 'Host: my-service.dev'
curl -i -X GET --url http://localhost:8000/ --header 'Host: my-service.dev'
curl -i -X GET --url http://localhost:8000/ --header 'Host: my-service.dev'

# 00/ --header 'Host: my-service.dev'
# HTTP/1.1 429 Too Many Requests
# Date: Tue, 02 Apr 2019 06:49:07 GMT
# Content-Type: application/json; charset=utf-8
# Connection: keep-alive
# Content-Length: 37
# X-RateLimit-Limit-minute: 5
# X-RateLimit-Remaining-minute: 0
# Server: kong/1.1.1

# {"message":"API rate limit exceeded"}
```