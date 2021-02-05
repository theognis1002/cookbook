### Django deployment configuration

When deploying a Django project, debug mode must be turned off. When that happens, Django and its development server no longer serve the static or media files anymore - the production server (ie; Nginx) will have to handle that now. Django first has to be configured so that it will copy all of the media/static files in specific locations for the production server to find.

In <project_folder>/settings.py:

1. Set DEBUG=False

1. Ensure both MEDIA_ROOT and STATIC_ROOT are defined using BASE_DIR. For example:

```
MEDIA_ROOT = os.path.join(BASE_DIR, "public/media")
```

```
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
```

1. `python manage.py collectstatic`
    - all static/media files across all of the apps and third-party libraries will be copied into MEDIA_ROOT and STATIC_ROOT

### Setting up uWSGI

1. `source venv/bin/activate`
1. `pip install uwsgi`
1. `cd /var/log`
1. `sudo mkdir uwsgi`
1. `sudo chown <root_username>:<root_password> /var/log/uwsgi`

Create uwsgi_params file in the project’s root folder with the following:

```
uwsgi_param QUERY_STRING $query_string;
uwsgi_param REQUEST_METHOD $request_method;
uwsgi_param CONTENT_TYPE $content_type;
uwsgi_param CONTENT_LENGTH $content_length;
uwsgi_param REQUEST_URI $request_uri;
uwsgi_param PATH_INFO $document_uri;
uwsgi_param DOCUMENT_ROOT $document_root;
uwsgi_param SERVER_PROTOCOL $server_protocol;
uwsgi_param REQUEST_SCHEME $scheme;
uwsgi_param HTTPS $https if_not_empty;
uwsgi_param REMOTE_ADDR $remote_addr;
uwsgi_param REMOTE_PORT $remote_port;
uwsgi_param SERVER_PORT $server_port;
uwsgi_param SERVER_NAME $server_name;
```

Create uwsgi.ini file in the project’s root folder. See reference config below:

```
[uwsgi]
module=<site_name>.wsgi:application
socket=/tmp/<site_name>.sock
chmod-socket = 666
master=True
pidfile=/tmp/project-master.pid
vacuum=True
max-requests=5000
daemonize=/var/log/uwsgi/<site_name>.log
```

### Setting up Nginx

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

### Deploying the app

1. `source venv/bin/activate`
1. `sudo service nginx restart`
1. `uwsgi --ini uwsgi.ini`

### Enabling Nginx and uWSGI to start on reboot

1. `cd /etc/systemd/system/`
1. `sudo touch uwsgi-bootup.service`
1. `sudo nano uwsgi-bootup.service`

See reference config below:

```
[Unit]
Description=uwsgi for denali site
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/home/ubuntu/<project_name>
Environment="PATH=/home/ubuntu/<project_name>/venv/bin"
ExecStart=/home/ubuntu/<project_name>/venv/bin/uwsgi --ini uwsgi.ini

[Install]
WantedBy=multi-user.target
```

1. `sudo systemctl start uwsgi-bootup`
1. `sudo systemctl enable uwsgi-bootup`
1. `sudo systemctl start nginx`
1. `sudo systemctl enable nginx`
