# DESCRIPTION
mock-api-server has 2 flask apps running simultaneously but separately.  
It means when you change something (like variables) via http request you won't see changes via https request and vice versa.  
But file sharing on the system works for both
# USAGE
To run all tests from all categories(api, web ui) execute:
```
./run_all_tests.sh
```
This command will build and run all docker containers. After that it executes all tests and shut down containers.

Another option is to do all these commands one by one.

You can find detailed steps below.
### BUILD
```
docker-compose build
```
If you made any changes to api-mock service - rebuild it with the same above cmd

### RUN EVERYTHING
```
docker-compose up -d
```

### RUN TESTS
```
docker-compose run tests
```

### RUN INFINITE FOR DEBUG/PLAY
Replace entrypoint on tests service to infinite loop
```
docker-compose up -d
```

### CONNECT TO RUNNING DB
```
docker exec -it mock-db-server psql -U user -d mockdb
```

### SHUTDOWN
```
docker-compose down
```

### CHECK LOGS
```
docker logs YOUR_CONTAINER_NAME
or
docker logs YOUR_CONTAINER_ID
```

