# kubernetes-stroke-prediction
This repository will walk you throught the steps of deploying a containerized application in the Azure Cloud with Azure Kuebernetes Service, testing the endpoint, load testing the deployment, and automating the deployment and load testing.
[![alt text](https://github.com/malcolmsfraser/kubernetes-stroke-prediction/blob/main/images/721finalthumbnai.jpg)](https://youtu.be/_yqLdCtKRBo) 
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
Step 0 - Create a new resource group from the Azure dashboard 
* Ours is called `ids721final`

Step 1 - Create your aks cluster w/ desires specifications
```
az aks create --resource-group ids721final --name ids721final \
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
az aks get-credentials --resource-group ids721Final --name ids721final
```

Step 3 - Create an acr respository
```
az acr create --resource-group ids721final --name ids721final --sku Basic --admin-enabled true
```

Step 4 - Attach acr repository to your aks cluster
```
az aks update --resource-group ids721final --name ids721final --attach-acr ids721final
```

Step 5 - Build your container image in you acr repository
```
az acr build --registry ids721final --image stroke-predict .
```

Step 5 - Deploy your application on your aks cluster
```
kubectl apply -f k8s/deployment.yaml
```

Step 6 - Add a load balancer in front of your cluster
```
kubectl apply -f k8s/loadbalancer.yaml
```

Step 7 - Find your load balancer IP
```
kubectl get services
```

## Part 2: Query your Kubernetes Application
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

## Part 3: Continuously Deliver you Kubernetes Application
Azure makes this process very simple :)  

1. Navigate to the Azure Kubernetes Service console and select your deployment cluster.  
2. In the panel on the left select "Deployment Center"  
3. Follow the prompts to link the kubernetes deployment to your application's source code repository and set up CD

## Part 4 : Clean-up Resources
The simplest way is to delete the resource group which contains the project
```
az group delete --name ids721final
```

## Tips & Troubleshooting

Be careful with naming resources, Azure has strict requirements. For example, DNS-1035 label must consist of lower case alphanumeric characters or '-', start with an alphabetic character, and end with an alphanumeric character (e.g. 'my-name',  or 'abc-123', regex used for validation is '[a-z]([-a-z0-9]*[a-z0-9])?')

This means that even though you can name a resource '721final', it would be an invalid name. However 'final721' would be acceptable
