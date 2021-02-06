1. `sudo mkdir /etc/nginx/ssl`
1. `cd /etc/nginx/ssl`
1. `sudo openssl genrsa -des3 -out server.key 2048`
1. `sudo openssl req -new -key server.key -out server.csr`
1. `sudo cp server.key server.key.org`
1. `sudo openssl rsa -in server.key.org -out server.key`
1. `sudo openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt`
1. add passphrase to `/etc/keys/global.pass`
1. `sudo chown root:root /etc/keys `
1. `sudo chown root:root /etc/keys/global.pass`
1. add `ssl_password_file /etc/keys/global.pass;` to conf

nginx.conf:

```
server {
  listen 443;
  server_name our-domain.com;

  root /var/www;
  index index.html index.htm;

  ssl on;
  ssl_certificate /etc/nginx/ssl/server.crt;
  ssl_certificate_key /etc/nginx/ssl/server.key;
}
```

1. `sudo service nginx restart1`
