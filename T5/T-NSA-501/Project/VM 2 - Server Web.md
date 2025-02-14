# Create and configure VM 2 - Server Web

## 1. Create VM2 in VirtualBox

1. Open **VirtualBox**.
2. Click on **New** to create a new virtual machine.
    - Name and Operating System: 
      - **Name**: VM2-ServerWeb
      - **Type**: BSD
      - **Version**: FreeBSD (64-bit)
   - **Memory**: 
     - At least **1024 MB** (or more depending on system resources).
   - **Hard Disk**: 
     - Create a new Virtual Hard Disk
     - Create a new **VDI (VirtualBox Disk Image)**, dynamically allocated
     - Allocate sufficient disk space (e.g., **20GB** or more).
3. Click **Create** to finalize.

---

## 2. Install FreeBSD on VM2

1. Start **VM2-ServerWeb** and click **Start**.
2. Follow the FreeBSD installation process (choose **default options**).
3. Choose **DHCP** for network configuration.
4. Complete installation:
   - Set **root password**.
   - Create a **user**.
   - Select **optional system components**.
5. **Reboot** (remove installation ISO).

---

## 3. Post-Installation Setup

> [!TIP]
> **If you need an IP address, run:**
>
>```sh
>dhclient em0  # Request an IP from DHCP
>```

### Update FreeBSD Packages

```sh
sudo pkg update && sudo pkg upgrade
```

### Install NGINX

```sh
sudo pkg install nginx
```

### Install PHP 7.4

#### Install Git

```sh
sudo pkg install git
```

#### Clone FreeBSD Ports

```sh
git clone https://git.FreeBSD.org/ports.git /usr/ports
```

#### Checkout Specific Commit

```sh
cd /usr/ports
git checkout 27ac371f93d36f77f00b8da261e496904184dd33
```

#### Compile & Install PHP 7.4

```sh
cd /usr/ports/lang/php74
make install clean
```

#### Compile & Install PHP 7.4 Extensions

```sh
cd /usr/ports/lang/php74-extensions
make install clean
```

If any problems occur, install missing dependencies:

```sh
sudo pkg install autoconf m4 help2man texinfo
```

Run recursive configuration:

```sh
make config-recursive install clean
```

#### Install PHP-MySQLi

```sh
cd /usr/ports/databases/php74-mysqli
make config  # Enable MySQL options
make install clean
```

### Install MySQL Server

```sh
pkg install mysql80-server
```

---

## 4. Configure NGINX

Edit the NGINX configuration file:

```sh
sudo vi /usr/local/etc/nginx/nginx.conf
```

Modify the `server` block to point to the web directory.

### Start NGINX

```sh
sudo service nginx start
```

### Configure PHP

Edit PHP configuration:

```sh
sudo vi /usr/local/etc/php.ini
```

Modify settings such as `memory_limit`, `timezone`, etc.

### Start PHP-FPM

```sh
sudo service php-fpm start
```

### Start MySQL

```sh
sudo service mysql-server start
```

### Secure MySQL Installation

```sh
sudo mysql_secure_installation
```

---

## 5. Database Setup

### Create Database & User

```sh
mysql -u root -p
```

Inside MySQL:

```sql
CREATE DATABASE nsa501;
USE nsa501;
SOURCE ./nsa501.sql;

CREATE USER 'backend'@'localhost' IDENTIFIED BY 'Bit8Q6a6G';
GRANT ALL PRIVILEGES ON nsa501.* TO 'backend'@'localhost';
FLUSH PRIVILEGES;

ALTER USER 'backend'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Bit8Q6a6G';
```

---

## 6. Start NGINX on Boot

Enable and start NGINX:

```sh
sudo sysrc nginx_enable=YES
sudo service nginx start
```

### Test NGINX

Open a web browser and visit:

```
http://localhost
```

You should see the **default NGINX welcome page**.

---

## 7. Deploy Web Application

### Edit NGINX Configuration

```sh
sudo nano /usr/local/etc/nginx/nginx.conf
```

Modify:

```
server {
    listen 80;
    server_name localhost;

    location / {
        root   /usr/local/www/nginx;
        index  data.php index.html index.htm;
    }
}
```

Ensure PHP is configured:

```
location ~ \.php$ {
    fastcgi_pass   127.0.0.1:9000;
    fastcgi_param  SCRIPT_FILENAME  /usr/local/www/nginx/data.php;
    include        fastcgi_params;
}
```

### Restart NGINX

```sh
sudo service nginx restart
```

---

## 8. Configure Static IP (Optional)

Edit **/etc/rc.conf**:

```sh
sudo vi /etc/rc.conf
```

Add:

```
ifconfig_em0="inet 192.168.42.70 netmask 255.255.255.192" defaultrouter="192.168.42.1"
```

### Restart Network Services

```sh
sudo service netif restart
```

---

After completing these steps, **VM2** will have **NGINX, PHP, and MySQL** installed and configured.  
The web application should be deployed, and MySQL will be set up with the specified database and user. 🚀