# KUBERNETES :

          * Kubernetes assembles one or more computers, either virtual machines or bare metal, into a cluster which can run workloads in
            containers.
          * It works with various container runtimes
          * Its suitability for running and managing workloads of all sizes and styles has led to its widespread adoption in clouds and data
            centers.

* k8s cluster is a set of machines called nodes, that are used to containerized applications

### In cluster we have two core pieces:
  - control plane
  - worker nodes

## 1). CONTROL PLANE :  
                   The Kubernetes control plane manages clusters and resources such as worker nodes and pods. The control plane 
                   receives information such as cluster activity, internal and external requests, and more. Based on these factors,
                   the control plane moves the cluster resources from their current state to the desired state,managing the state of 
                   clusters. 
  
* control plane consists of : 
  - API servers
  - etcd
  - scheduler
  - controller manager

### APL server : 
- API server is the primary interface between the control plane and rest of the clusters.
- It exposes a restful API that allows clients to interact with the control plane and submit requests to manage the     
clusters. 

### etcd : 
- etcd  is distributed key value store.
- It stores clusters persistence state.
- It is used by all components in the control plane to store and retrieve info about the cluster.

### scheduler :  
- It is responsible for scheduling pods onto the worker nodes in the cluster.
- It is used to know about the resources required by the pods and the available resources on the worker nodes to make 
  placement decision.

### controller manager :
- Is responsible for running controllers that manage the state of the cluster.


## 2). WORKER NODES :
                  A worker node is a node that runs the application in a cluster and reports to a control plane. The main  
                  responsibilities of a worker node is to process data stored in the cluster and handle networking to ensure traffic 
                  between the application across the cluster and outside  the cluster are properly facilitated.

* Worker nodes consists of :
   - worker nodes
   - Pods
   - Kubelet
   - Container runtime
   - Kube proxy
### Worker nodes : 
- These nodes run's the containerized application workloads.
- The containerized applications runs in a pod.
- Pods are smallest deployable units in kubernetes.

### Pods : 
- Pod hosts one or more containers and provide shared storage and networking for those containers.
- Pods are created and managed by the kubernetes control plane.
- They are basic building blocks of kubernetes applications.

### Kubelet : 
- Kubelet is a daemon that runs on each worker node it's responsible for the communication with the control plane.
- It receives information from control plane about which pods to run on the node and thr pods is maintained.

### Container runtime : 
- It runs the container on the worker nodes.
- It's responsible for pulling the container images from registry.
- starting,stopping and maintaining the containers is done here.

### Kube-proxy : 
- Kube-proxy is a network proxy that runs in each worker node 
                 
- It's responsible for routing the traffic to the correct pods.
                
- It also provides load balancing for the pods & ensure that traffic is distributed evenly across the pods.
   
              
 
