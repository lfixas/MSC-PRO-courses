# Day 05

## Install Ansible

```bash
sudo apt install ansible
```

### Set Up Project Structure

```bash
mkdir ansible_project/
cd ansible_project/
nano host.ini
```

Add the following:

```
[nsapoold05]
127.0.0.1 ansible_connection=local
```

Create Playbook:

```bash
nano playbook.yml
```

---

## Change Hostname

```bash
mkdir change_hostname
cd change_hostname
mkdir tasks meta
```

Create `tasks/main.yml`:

```yaml
---
- name: Change hostname to nsapoold05
  hostname:
    name: nsapoold05
```

Create `meta/main.yml`:

```yaml
---
dependencies: []
```

Update Playbook:

```bash
nano /home/lucas/playbook.yml
```

```yaml
---
- hosts: nsapoold05
  become: yes
  roles:
    - change_hostname
```

---

## Create User "Marvin"

```bash
mkdir create_user_marvin
cd create_user_marvin/
mkdir tasks meta
```

Create `tasks/main.yml`:

```yaml
---
- name: Create user Marvin
  user:
    name: "marvin"
    password: "NsaPool42"
    home: /home/marvin
    createhome: yes
```

Create `meta/main.yml`:

```yaml
---
dependencies: []
```

Update Playbook:

```yaml
---
- hosts: nsapoold05
  become: yes
  roles:
    - change_hostname
    - create_user_marvin
```

---

## Set Custom Welcome Message

```bash
mkdir change_welcome_message
cd change_welcome_message/
mkdir tasks meta
```

Create `tasks/main.yml`:

```yaml
---
- name: Set welcome message
  copy:
    content: "Welcome to nsapoold05
"
    dest: /etc/motd
  become: yes
```

Create `meta/main.yml`:

```yaml
---
dependencies: []
```

Update Playbook:

```yaml
---
- hosts: nsapoold05
  become: yes
  roles:
    - change_hostname
    - create_user_marvin
    - change_welcome_message
```

Verify:

```bash
cat /etc/motd
```

---

## Install Required Packages

```bash
mkdir update_packages
cd update_packages/
mkdir tasks meta
```

Create `tasks/main.yml`:

```yaml
---
- name: Update package cache
  apt:
    update_cache: yes
  when: ansible_pkg_mgr == 'apt'

- name: Install necessary packages
  package:
    name:
      - git
      - htop
      - curl
      - sudo
      - unzip
      - python3
      - python3-pip
  become: yes
```

Create `meta/main.yml`:

```yaml
---
dependencies: []
```

Update Playbook:

```yaml
---
- hosts: nsapoold05
  become: yes
  roles:
    - change_hostname
    - create_user_marvin
    - change_welcome_message
    - update_packages
```

---

## Install Nginx and Website

```bash
mkdir install_nginx_website
cd install_nginx_website/
mkdir tasks meta
```

Create `tasks/main.yml`:

```yaml
---
- name: Install Nginx
  package:
    name: nginx
    state: latest
  become: yes

- name: Download and Extract Website Content
  unarchive:
    src: https://gandalf.epitech.eu/pluginfile.php/29515/mod_assign/introattachment/0/app.zip
    dest: /var/www/html/
    remote_src: yes
  become: yes

- name: Set correct permissions for Nginx to serve files
  file:
    path: /var/www/html/
    recurse: yes
    state: directory
    owner: www-data
    group: www-data
    mode: "0755"
  become: yes

- name: Configure Nginx to serve the website
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/sites-available/default
  become: yes
  notify: Restart Nginx

- name: Ensure Nginx is started
  service:
    name: nginx
    state: started
    enabled: yes
  become: yes
```

Create `meta/main.yml`:

```yaml
---
dependencies: []
```

Update Playbook:

```yaml
---
- hosts: nsapoold05
  become: yes
  roles:
    - change_hostname
    - create_user_marvin
    - change_welcome_message
    - update_packages
    - install_nginx_website
```

Create Template File:

```bash
mkdir -p templates
nano templates/nginx.conf.j2
```

```
server {
    listen 80;
    server_name localhost;

    location / {
        root /var/www/html;
        index index.php index.html;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```

---

## Install PHP

```bash
mkdir install_php
cd install_php/
mkdir tasks meta
```

Create `tasks/main.yml`:

```yaml
---
- name: Install PHP and required modules
  package:
    name:
      - php-cli
      - php-fpm
      - php-json
      - php-pdo
      - php-mysql
      - php-zip
      - php-gd
      - php-mbstring
      - php-curl
      - php-xml
      - php-pear
      - php-bcmath
      - php-intl
    state: latest
  become: yes
```

Create `meta/main.yml`:

```yaml
---
dependencies: []
```

Update Playbook:

```yaml
---
- hosts: nsapoold05
  become: yes
  roles:
    - change_hostname
    - create_user_marvin
    - change_welcome_message
    - update_packages
    - install_nginx_website
    - install_php
```

Verify:

```bash
php -v
php -m
cat /etc/php/7.4/cli/php.ini | grep date.timezone
cat /etc/php/7.4/fpm/php.ini | grep date.timezone
systemctl status php7.4-fpm
```

---

## Install MariaDB

```bash
mkdir install_mariadb
cd install_mariadb/
mkdir tasks meta
```

Create `tasks/main.yml`:

```yaml
---
- name: Install MariaDB
  package:
    name: mariadb-server
    state: latest
  become: yes

- name: Install PyMySQL (Python 3)
  pip:
    name: pymysql
  become: yes

- name: Copy the provided database
  copy:
    src: "{{ playbook_dir }}/files/database/nsapool.sql"
    dest: /tmp/nsapool.sql
  become: yes

- name: Create database nsapool
  mysql_db:
    name: nsapool
    state: present
    login_user: root
    login_password: bV3XV
  become: yes

- name: Create MariaDB user
  mysql_user:
    name: nsad04
    host: localhost
    password: "E24h7U5kA9HJhq5VM98pm7p5zmJpf8AK"
    priv: "*.*:ALL"
    state: present
  become: yes
```

Update Playbook:

```yaml
---
- hosts: nsapoold05
  become: yes
  roles:
    - install_mariadb
```

