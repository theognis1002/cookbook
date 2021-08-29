### Add Bash to Alpine

1. `RUN apk update && apk add bash`

### Docker logs

1. `docker logs <container_name>`
1. `docker logs -f` <container_name> <--- continuous logs

### Docker prune

1. `docker system prune -f`
1. `docker volume prune -f`

### Docker run one-off commands

1. `docker compose run <service_name> <command>`
    - ie; `docker compose run app python manage.py createsuperuser`

### Non-sudo docker

1. `sudo usermod -aG docker <current_user>`
