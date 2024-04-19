# CNF
Containerized Network Functions

Firewall
1. Build the docker image
docker build -t firewall-image .

2. Run the docker image, with extra networking privilege and using host network namespace
docker run --name firewall-image --network host --cap-add NET_ADMIN -d firewall-container
