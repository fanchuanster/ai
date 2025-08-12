1. sealed-secrets-controller - 
    kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.30.0/controller.yaml

2. create sealed secrets that can be committed to git, using cluster public key
    1) kubectl create secret generic --from-literal=db-pwd=mypwd123 --dry-run=client -o yaml | kubeseal --format=yaml -o yaml
    2) kubectl create secret generic my-dbpwd \
        --from-literal=db-pwd=mypwd123 \
        --dry-run=client -o yaml | \
        kubeseal --cert=pub-cert.pem --format=yaml > sealed-secret.yaml

    jenkins@92d30fc069fe:/tmp$ cat sealed-secret.yaml
---
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  creationTimestamp: null
  name: my-dbpwd
  namespace: default
spec:
  encryptedData:
    db-pwd: AgCHqyTgbJ9L1whnKlMv/yoNvnumWjgGi1YYokKdfs+o6ZtgO6nvaYmKjKhX6N5re3xx6pYZeGYCSfxX0Vfzc51uquK4X60xPiNzaEw7mHtvzxzm3wkUIQLmKaOYTxQmdU+Nr2JSAcezFWxcKNbLNMm6STvyc+JZLntljfrmDRmzxwkO+BGgXLUgFlIbvxvBctdNdQK4IbnhaTzv1L++FcoaNVupjOaUbLVYmF90ULTnVEhU1UPXYC+FI7ZRYg3n4IbG6vVtk87QP87VX6pREU33vmPMqAlCvYPDC9C71WpVqi3O1h3cxhSAOPS3c8YqwpnWb6u649F44uJHe+aJHHPPTJ/F9U4zqJai62L+a5QqIk/wCIBDLSdljlF09E6CcfH8PtklVXnO0P1z3fOl21i8hcSG6a5XCjrU/wmZKNMJW6LJm1aPD/VO9ADfGUaN2I26eD4GLM+SP5cMaeQSJrMxrrY7UOmvAcFHpBVv5ScRpYsa8dqVSYgFtPTH/a0HD1iuavWJIzV81gP4izz9xDUNfe53OgULwxjoJGo6Gc86DAOC6ekEy8+u4GzW61qMLYtAE9Fh0b178ICvvKjwPyrNk5y2yiyFvhDhs8tosUbTW6KyKiHx8RSSwNh+ujKd5k2j9P/uJknOHN11YeGuayi+qkWl7IP0q2393LpFpKKXuIjyR3J3/y6vJ8AZhSGvEJ2DSpKDma3Glw==
  template:
    metadata:
      creationTimestamp: null
      name: my-dbpwd
      namespace: default

3. apply the sealedsecret to create secret in k8s, as k8s cluster can decrypt
4. create volume from secret
5. mount secret volume to pod - as env or file
6. app can access the secret