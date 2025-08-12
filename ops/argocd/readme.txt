https://argo-cd.readthedocs.io/en/stable/getting_started/


kubectl port-forward svc/argocd-server -n argocd 8080:443
kubectl port-forward svc/kustomize-guestbook-ui -n ns1 8080:80
argocd login localhost:8080 --username admin --password 6l9y5oJRF06C5cTa --insecure
