## Files needed

- `cadvisor.daemonset.yaml`
- `poll.deployment.yaml`
- `poll.ingress.yaml`
- `poll.service.yaml`
- `postgres.configmap.yaml`
- `postgres.deployment.yaml`
- `postgres.secret.yaml`
- `postgres.service.yaml`
- `postgres.volume.yaml`
- `redis.configmap.yaml`
- `redis.deployment.yaml`
- `redis.service.yaml`
- `result.deployment.yaml`
- `result.ingress.yaml`
- `result.service.yaml`
- `traefik.deployment.yaml`
- `traefik.rbac.yaml`
- `traefik.service.yaml`
- `worker.deployment.yaml`

## Database - Redis / Postgres

### `postgres.secret.yaml`

`echo -n 'username' | base64`
`echo -n 'password' | base64`

Mettre l'output de chaque dans `POSTGRES_USER` & `POSTGRES_PASSWORD`

`cGllcnJl` : `pierre`
`YWRtaW4=` : `admin`

`POSTGRES_DB` : `mydatabase`

Appliquer les configurations Redis : 
- `kubectl apply -f redis.configmap.yaml`
- `kubectl apply -f redis.deployment.yaml`
- `kubectl apply -f redis.service.yaml`

Appliquer les configurations PostgreSQL :
- `kubectl apply -f postgres.secret.yaml`
- `kubectl apply -f postgres.configmap.yaml`
- `kubectl apply -f postgres.volume.yaml`
- `kubectl apply -f postgres.deployment.yaml`
- `kubectl apply -f postgres.service.yaml`

Vérification du déploiement
- `kubectl get pods -n default`
- `kubectl get services -n default`
- `kubectl logs <postgres-pod-name> -n default`