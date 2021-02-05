### Nginx Setup (Linux)

1. `sudo apt-get update`
1. `sudo apt-get install nginx`
1. `cd /etc/nginx/sites-enabled`
1. `sudo rm default`
1. `cd /etc/nginx/sites-available`
1. `sudo nano <site_name>`
1. Enter in Nginx configuration

```
server {
    listen 80;
    location / {
        uwsgi_pass unix:/tmp/<site_name>.sock;
        include /home/ubuntu/<project>/<site_name>/uwsgi_params;
    }
    location /media  {
        alias /home/ubuntu/<project>/public/media;
    }
    location /static {
        alias /home/ubuntu/<project>/public/static;
    }
}
```

1. `sudo ln -s /etc/nginx/sites-available/<site_name> /etc/nginx/sites-enabled/`
    - creates soft link from the config file to the sites-enabled directory, which Nginx reads from during startup
1. `sudo service nginx restart`
