## creation of pod
* kubectl create -f flask-app.yaml
## check pod status
* kubectl get pods
## delete existing pod
* kubectl delete pod flask-app-pod-yaml
## port-forwarding for pod
* kubectl port-forward flask-app-pod-yaml 8080:5000
* here 8080 is local 
* 5000 is container port (We mentioned container-port as 5000 in pod defined yaml file )