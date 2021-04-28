# kubernetes-stroke-prediction

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

Step 2 - Load merge aks credentials between kubectl and your aks cluster
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
