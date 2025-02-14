# Day 03

## Install Required Binaries

```bash
sudo apt update
sudo apt install curl
curl -1sLf 'https://dl.cloudsmith.io/public/symfony/stable/setup.deb.sh' | sudo -E bash
sudo apt install symfony-cli
sudo apt install composer
```

If you encounter key issues:

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
```

References:
- [Install PHP 8.2 on Debian 11](https://orcacore.com/install-php-8-2-debian-11/)
- [Install Node.js & npm on Debian 11](https://www.vultr.com/docs/how-to-install-node-js--npm-on-debian-11/)

---

## Install Apache 2

```bash
sudo apt install apache2
sudo systemctl start apache2
sudo systemctl enable apache2
```

### Verify Installation

```bash
sudo systemctl status apache2
```

### Configure Apache to Listen on Port 80

```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```

Modify:

```
<VirtualHost *:80>
    ...
</VirtualHost>
```

Restart Apache:

```bash
sudo systemctl restart apache2
```

---

## Install MySQL 5.7

Reference: [How to Install MySQL on Debian](https://computingforgeeks.com/how-to-install-mysql-on-debian-linux-system/)

Secure installation:

```bash
sudo mysql_secure_installation
```

### Allow External Connections

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

Change:

```
bind-address = 127.0.0.1
```

to

```
bind-address = 0.0.0.0
```

### Restart MySQL

```bash
sudo systemctl restart mysql
sudo systemctl enable mysql
sudo systemctl status mysql
```

---

## Add SQL Database

```bash
wget https://cdn.alexishenry.eu/shared/files/nsapool.sql
```
or use **WinSCP**

### Create Database

```bash
mysql -u root -p -e "CREATE DATABASE nsapool;"
```

### Import Database

```bash
mysql -u root -p nsapool < nsapool.sql
```

### Connect to MySQL

```bash
mysql -u root -p
```

### Verify Import

```sql
SHOW DATABASES;
USE nsapool;
SHOW TABLES;
SELECT * FROM user;
```

### Configure Database User

```sql
CREATE USER 'data-backend'@'%' IDENTIFIED BY 'EwUrk9Q46';
GRANT ALL PRIVILEGES ON *.* TO 'data-backend'@'%';
FLUSH PRIVILEGES;
exit;
```

### Verify Database User

```bash
mysql -u data-backend -p
SHOW GRANTS FOR 'data-backend'@'%';
```

---

## Install phpMyAdmin

```bash
sudo apt install phpmyadmin
```

### Create Symbolic Link

```bash
sudo ln -s /etc/phpmyadmin/apache.conf /etc/apache2/sites-enabled/phpmyadmin.conf
```

Restart Apache:

```bash
sudo systemctl restart apache2
```

### Configure Apache for Port 8000 (If Necessary)

```bash
sudo nano /etc/apache2/ports.conf
```

Modify to:

```
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

Listen 80
Listen 8000

<IfModule ssl_module>
    Listen 443
</IfModule>

<IfModule mod_gnutls.c>
    Listen 443
</IfModule>
```

Restart Apache:

```bash
sudo systemctl restart apache2
```

### Reconfigure phpMyAdmin (If Needed)

```bash
sudo dpkg-reconfigure phpmyadmin
```

### Fix Password Issues

```sql
uninstall plugin validate_password;
```

### Test phpMyAdmin

```bash
curl -I http://localhost:8000/phpmyadmin
```

### Verify Installation

```bash
sudo dpkg -l | grep phpmyadmin
ls -l /etc/apache2/sites-enabled/
```

Ensure alias is correctly set:

```bash
sudo nano /etc/apache2/sites-enabled/phpmyadmin.conf
```

---

## Setup Frontend

```bash
wget https://cdn.alexishenry.eu/shared/files/frontend.zip
```
or use **WinSCP**

### Install Unzip

```bash
sudo apt install unzip
```

### Create Directory

```bash
sudo mkdir -p /var/www
```

### Unzip Archive

```bash
sudo unzip frontend.zip -d /var/www/
```

Rename archive:

```bash
mv T-NSA-500_day03_frontend-main frontend
mv frontend /var/www/
```

### Configure Apache for Frontend

```bash
sudo nano /etc/apache2/sites-available/frontend.conf
```

Add:

```
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/frontend/public

    <Directory /var/www/frontend/public>
        AllowOverride None
        Order Allow,Deny
        Allow from All

        <IfModule mod_rewrite.c>
            Options -MultiViews
            RewriteEngine On
            RewriteCond %{REQUEST_FILENAME} !-f
            RewriteRule ^(.*)$ index.php [QSA,L]
        </IfModule>
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/frontend_error.log
    CustomLog ${APACHE_LOG_DIR}/frontend_access.log combined
</VirtualHost>
```

### Enable Site

```bash
sudo a2ensite frontend.conf
```

### Disable Default Site

```bash
sudo a2dissite 000-default
```

Apply changes:

```bash
sudo systemctl restart apache2
```

### Test Frontend

```bash
curl -I http://10.0.2.15:80/
```

