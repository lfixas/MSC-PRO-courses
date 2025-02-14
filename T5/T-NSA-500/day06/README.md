# Day 06

## Install OpenSSH Server

```bash
sudo apt install openssh-server
```

### Generate SSH Key

```bash
cd ~/.ssh
ssh-keygen -f vm_debian_{..}
```

### Configure SSH Port Forwarding

```bash
ssh -p 2222 marvin@127.0.0.1
```

---

## Install Docker

References:
- [Install Docker Engine on Debian](https://docs.docker.com/engine/install/debian/)

### Install Required Dependencies

```bash
sudo apt install -y curl
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
```

### Add Docker Repository & Install Docker

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

### Start & Enable Docker

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Verify Installation

```bash
sudo docker --version
sudo curl --version
```

---

## Create User & Add to Docker Group

### Create User "marvin"

```bash
sudo adduser marvin
```

### Add "marvin" to Docker Group

```bash
sudo usermod -aG docker marvin
```

### Verify Group Membership

```bash
groups marvin
```

### Make Docker-Compose Executable for Marvin

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

---

## Docker-Compose Configuration

Create `docker-compose.yml`:

```yaml
version: '3'

services:
  portainer:
    image: portainer/portainer
    container_name: portainer-nsapoold06
    ports:
      - "5555:9000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
#      - portainer_data:/data
    restart: always
    command: -H unix:///var/run/docker.sock

  database:
    image: mariadb:latest
    container_name: db_nsapoold06
    environment:
      MYSQL_DATABASE: nsapoold06
      MYSQL_USER: marvin
      MYSQL_PASSWORD: Marvin53Xb
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3306:3306"
    volumes:
      - ./init-scripts:/docker-entrypoint-initdb.d
    restart: always

  back_nsapoold06:
    build: "./project"
    container_name: back_nsapoold06
    ports:
      - "80:5000"
```

### Ensure `init-scripts` Exists in the Same Directory as `docker-compose.yml`
Make sure to place the initialization scripts inside `init-scripts/` at the same location as `docker-compose.yml`.

