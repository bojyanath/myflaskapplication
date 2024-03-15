##  Push docker image to repository. 

* I have created a docker hub account.
* Then i created a new repository "docker-repo" in docker hub.

* I used tag command to tag my image to the "docker-repo" repository.

```python
Syntax: DOCKER TAG IMAGE_NAME:TAG NAMESPACE/REPOSITORY:TAG
Ex    : docker tag my-flask-app:latest bojyanath/docker-repo:latest

```

* Then in pushed the changes to "docker-repo" directory

```python
Syntax :  DOCKER PUSH NAMESPACE/REPOSITORY:TAG
Ex     :  docker push bojyanath/docker-repo:latest
```
