### https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04

1. `sudo apt install python3-certbot-nginx`
1. `sudo nano /etc/nginx/sites-available/example.com`
   nginx.conf:

```
server {
  listen 80;
  server_name our-domain.com www.our-domain.com;

}
```

1. `sudo nginx -t`

-   test nginx config is correct

1. `sudo service nginx restart`
1. `sudo ufw status`
1. `sudo ufw allow 'Nginx Full'`
1. `sudo ufw delete allow 'Nginx HTTP'`
1. `sudo certbot --nginx -d example.com -d www.example.com`
1. `sudo certbot renew --dry-run`

-   test renewal
