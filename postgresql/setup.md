1. `sudo apt update`
1. `sudo apt install postgresql postgresql-contrib`
1. `sudo -u postgres psql`
1. `CREATE DATABASE <db_name>;`
1. `CREATE USER <username> with PASSWORD '<password>';`
1. `ALTER ROLE <username> SET client_encoding to 'utf8';`
1. `ALTER ROLE <username> SET default_transaction_isolation to 'read committed';`
1. `ALTER ROLE <username> SET timezone to 'UTC';`
1. `GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <username>;`
1. `\q`
1. `exit`
