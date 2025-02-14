# Day 04

## Backend Setup

```bash
wget https://cdn.alexishenry.eu/shared/files/api-master.zip
```
or use **WinSCP**

### Install Unzip (If Needed)

```bash
sudo apt install unzip
```

### Create Directory (If Needed)

```bash
sudo mkdir -p /var/www
```

### Unzip Backend

```bash
sudo unzip api-master.zip
```

Rename and move:

```bash
mv api backend
mv backend /var/www/
```

### Configure Apache for Backend

```bash
sudo nano /etc/apache2/sites-available/backend.conf
```

Add:

```
<VirtualHost *:8080>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/backend/public

    <Directory /var/www/backend/public>
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

    ErrorLog ${APACHE_LOG_DIR}/backend_error.log
    CustomLog ${APACHE_LOG_DIR}/backend_access.log combined
</VirtualHost>
```

### Configure Port 8080

```bash
sudo nano /etc/apache2/ports.conf
```

### Enable Site Configuration

```bash
sudo a2ensite backend.conf
```

### Install PHP 7.4

```bash
sudo apt install php7.4
sudo update-alternatives --config php
```

### Install Required PHP Modules

```bash
sudo apt install php7.4-xml
```

### Navigate to Backend Directory

```bash
cd /var/www/backend
```

### Install Dependencies

```bash
symfony composer install
```

### Restart Apache

```bash
sudo systemctl restart apache2
```

---

## Admin Security

```bash
wget https://cdn.alexishenry.eu/shared/files/scriptadmin.zip
```
or use **WinSCP**

### Unzip Script

```bash
sudo unzip scriptadmin.zip
```

Move script:

```bash
mv scriptadmin.php /var/www/backend/
```

### Set Up Authentication

```bash
sudo htpasswd -c /etc/apache2/.htpasswd admin
```

(If required: `sudo apt install apache2-utils`)

### Update Backend Configuration

```bash
sudo nano /etc/apache2/sites-available/backend.conf
```

Modify:

```
<VirtualHost *:8080>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/backend/public

    <Directory /var/www/backend/public>
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

    <Location "/admin">
        AuthType Basic
        AuthName "Restricted Access"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user
    </Location>

    ErrorLog ${APACHE_LOG_DIR}/backend_error.log
    CustomLog ${APACHE_LOG_DIR}/backend_access.log combined
</VirtualHost>
```

### Restart Apache

```bash
sudo systemctl restart apache2
```

### Test Security

```bash
curl -I http://localhost:8080/admin
```

> Expected response: `HTTP/1.1 401 Unauthorized`

---

## Set Up Firewall with IPTables

```bash
sudo apt-get update
sudo apt-get install iptables-persistent
```

### Modify IPTables Rules

```bash
sudo nano /etc/iptables/rules.v4.3
```

Add:

```
*filter
:INPUT DROP [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]

# Allow SSH (input and output)
-A INPUT -p tcp --dport 22 -j ACCEPT
-A OUTPUT -p tcp --sport 22 -j ACCEPT

# Allow HTTP protocol (output)
-A OUTPUT -p tcp --dport 80 -j ACCEPT

# Other authorizations necessary for frontend and backend

# Example: Allow MySQL for backend
# -A INPUT -p tcp --dport 3306 -j ACCEPT
# -A OUTPUT -p tcp --sport 3306 -j ACCEPT

# Example: Allow other ports for frontend/backend

COMMIT
```

### Apply Rules

```bash
sudo cat /etc/iptables/rules.v4.3 | sudo iptables-restore
```

### Verify Rules

```bash
sudo iptables -L
```

---

## Create Local Backups

```bash
mkdir /backup
```

### Create Backup Script

```bash
nano /backup/backup.sh
```

Add:

```
#!/bin/bash

# Database credentials
DB_USER="root"
DB_PASSWORD="Nm3ZaMg64"
DB_NAME="nsapool"

# Backup directory
BACKUP_DIR="/backup"

# Timestamp for backup file
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

# Backup file name
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.sql"

# Compressed backup file name
COMPRESSED_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

# MySQL dump command
mysqldump -u$DB_USER -p$DB_PASSWORD $DB_NAME > $BACKUP_FILE

# Check if the MySQL dump was successful
if [ $? -eq 0 ]; then
    echo "MySQL backup completed successfully."

    # Compress the backup file
    tar -czf $COMPRESSED_FILE -C $BACKUP_DIR backup_$TIMESTAMP.sql

    # Remove the original SQL backup file
    rm $BACKUP_FILE

    echo "Backup compressed successfully: $COMPRESSED_FILE"
else
    echo "Error: MySQL backup failed."
fi
```

### Make Script Executable

```bash
chmod +x /backup/backup.sh
```

### Run Backup Script (If Needed)

```bash
/backup/backup.sh
```

---

## Schedule Backup Script

```bash
sudo crontab -e
```

Add:

```
0 * * * * /backup/backup.sh
```

---
