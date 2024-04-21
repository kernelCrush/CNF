# CNF
## Containerized Network Functions

### Firewall
1. Build the docker image\
```docker build -t firewall-image .```

2. Run the docker image, with extra networking privilege and using host network namespace\
```docker run --name firewall-image --network host --cap-add NET_ADMIN -d firewall-container```

3. ping google.com

### Load Balancer
1. Build the docker image\
```docker build -t load_balancer .```

2. Run the load_balancer container\
```docker run -d --network host load_balancer```

3. Run 2 servers on 8000 and 8001 using the following commands\
```nc -l localhost 8000```
```nc -l localhost 8001```

4. Connect to the load balancer running on port 8080. This will randomly connect to one of the 2 web servers at the backend\
```curl localhost:8080```
