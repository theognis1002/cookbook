### General Commands

1. `docker compose up --build`
1. `docker compose down`

    - Stops containers and removes containers, networks, volumes, and images created by `up`.

1. `docker compose start`
1. `docker compose stop`

    - Stops running containers without removing them. They can be started again with `docker-compose start`.

1. `docker compose restart`
1. `docker compose logs <optional: service>`

### Run one-off commands

1. `docker compose run <service_name> <command>`
    - ie; `docker compose run app python manage.py createsuperuser`
