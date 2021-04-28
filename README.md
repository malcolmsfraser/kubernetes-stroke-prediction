# kubernetes-stroke-prediction
This repository will walk you throught the steps of deploying a containerized application in the Azure Cloud with Azure Kuebernetes Service, testing the endpoint, load testing the deployment, and automating the deployment and load testing.

## Part 0: Test the Application Locally
Step 1 - Create a virtual environment and install the requirements
```
python3 -m venv ~/.venv
source ~/.venv/bin/activate
pip install -r requirements.txt
```

Step 2 - Run the application locally
```
python app.py
```

Step 3 - From a separate terminal, query the local host endpoint
```
python utilscli.py payload-predict
```
*default host for utilscli.py is http://localhost:8080/predict - use `python utilscli.py --help` for more info*

## Part 1: AKS/ACR Setup and Application Deployment 
Step 1 - Create your aks cluster w/ desires specifications
```
az aks create --resource-group 721Final --name 721Final \
--generate-ssh-keys \
--node-count 3 \
--vm-set-type VirtualMachineScaleSets \
--load-balancer-sku standard \
--enable-cluster-autoscaler \
--min-count 1 \
--max-count 5
```

Step 2 - Merge aks credentials between kubectl and your aks cluster
```
az aks get-credentials --resource-group 721Final --name 721Final
```

Step 3 - Create an acr respository
```
az acr create --resource-group 721Final --name 721Final --sku Basic --admin-enabled true
```

Step 4 - Attach acr repository to yuor aks cluster
```
az aks update --resource-group 721Final --name 721Final --attach-acr 721Final
```

Step 5 - Build your container image in you acr repository
```
az acr build --registry 721Final --image stroke-predict .
```

Step 5 - Deploy your application on your aks cluster
```
kubectl apply -f aksdeploy/deployment.yaml
```

Step 6 - Add a load balancer in front of your cluster
```
kubectl apply -f aksdeploy/loadbalancer.yaml
```

Step 7 - Find your load balancer IP
```
kubectl get services
```

## Part 2: Query your kubernetes application
Step 1 - (if you haven't already) Create a virtual environment and install the cli requirements
```
python3 -m venv ~/.venv
source ~/.venv/bin/activate
pip install -r requirements.txt
```

Step 2 - Use the utility cli to query the load balancer endpoint:
```
python  utilscli.py payload-predict -host http://<Load-Balacer-External-IP>/predict
```

