## kubectl Generic Commands

### Cluster Management

- `kubectl cluster-info`: Display endpoint information about the master and services in the cluster.
- `kubectl config view`: Show merged kubeconfig settings or a specific Kubernetes configuration file.
- `kubectl config get-contexts`: List all contexts
- `kubectl config current-context`: Check current context
- `kubectl config use-context <context-name>`: Switch to another context

### Resource Management

- `kubectl apply -f <filename>`: Apply a configuration to a resource by filename or stdin.
- `kubectl create -f <filename>`: Create a resource from a file or from stdin.
- `kubectl delete -f <filename>`: Delete resources by file name or stdin.
- `kubectl get <resource>`: List one or more resources.
- `kubectl describe <resource> <name>`: Show detailed state of a resource including events.
- `kubectl edit <resource> <name>`: Edit a resource on the server.
- `kubectl patch <resource> <name> -p <patch>`: Update fields of a resource using strategic merge patch.
- `kubectl replace -f <filename>`: Replace a resource by filename or stdin.

### Resource Inspection

- `kubectl logs <pod-name>`: Print the logs for a container in a pod.
- `kubectl exec -it <pod-name> -- <command>`: Execute a command in a container.
- `kubectl port-forward <pod-name> <local-port>`:<pod-port>`: Forward one or more local ports to a pod.

### Deployment Management

- `kubectl rollout status deployment/<deployment-name>`: Check the status of a rollout.
- `kubectl rollout undo deployment/<deployment-name>`: Rollback to the previous deployment.
- `kubectl scale deployment <deployment-name> --replicas=<number>`: Scale a deployment.
- `kubectl rollout restart deployment/<deployment-name>`: Restart a deployment.

### Namespace Operations

- `kubectl get namespaces`: List all namespaces in the cluster.
- `kubectl create namespace <name>`: Create a new namespace.
- `kubectl delete namespace <name>`: Delete a namespace.

### Label and Annotation Management

- `kubectl label <resource> <name> <key>=<value>`: Update the labels on a resource.
- `kubectl annotate <resource> <name> <key>=<value>`: Update the annotations on a resource.

### Monitoring and Debugging

- `kubectl get pods`: Display pod info
- `kubectl top node`: Display resource (CPU/Memory/Storage) usage for nodes.
- `kubectl top pod`: Display resource usage for pods.
- `kubectl get events`: List recent events in the cluster or for a specific namespace.

### Service and Ingress

- `kubectl expose deployment/<deployment-name> --type=LoadBalancer --port=80`: Expose a deployment as a new Kubernetes Service.
- `kubectl get services`: List all services in the cluster or specified namespace.
- `kubectl get ingress`: List all Ingress resources.

### Pod Management

- `kubectl run <name> --image=<image>`: Run a particular image on the cluster.
- `kubectl delete pod <pod-name>`: Delete a pod by name.
- `kubectl exec -it -n <NAMESPACE> <POD_ID> -- /bin/bash`: Exec bash into specific pod within a namespace

---

## GCP Specific Commmands

- `gcloud auth login`: Login to GCP
- `gcloud container clusters get-credentials <CLUSTER_NAME> --zone us-east1 --project <PROJECT_ID>`: Access specific cluster + swap context

### Practical CLI Workflows

1. Open bash within a pod

```bash
kubectl config get-contexts
kubectl config use-context <CONTEXT>
kubectl config current-context
kubectl get namespaces
kubectl get pods -n <NAMESPACE>
kubectl exec -it -n <NAMESPACE> <POD_NAME> -- /bin/bash
```
