# Day 01

## Create User "marvin"

Create a user **marvin** with:
- Home directory: `/home/marvin`
- Description: "Android Paranoid"
- UID: `4242`

```bash
sudo useradd -m -d /home/marvin -c "Android Paranoid" -u 4242 marvin
```

Set password to `toto42sh`:

```bash
sudo passwd marvin
```

### Verify User Information

- User info:
  ```bash
  id marvin
  ```
- Home directory:
  ```bash
  grep marvin /etc/passwd | cut -d: -f6
  ```
- UID:
  ```bash
  id -u marvin
  ```
- Description:
  ```bash
  grep marvin /etc/passwd | cut -d: -f5
  ```
- Full details:
  ```bash
  getent passwd marvin
  ```

---

## Create Group "H2G2"

Create a group **H2G2** with GID `42400`:

```bash
sudo groupadd -g 42400 H2G2
```

Add marvin to the group:

```bash
sudo usermod -aG H2G2 marvin
```

Create user **Zaphod**:

```bash
sudo useradd -m -d /home/zaphod -c "Zaphod Beeblebrox" -u 4200 -g 42400 zaphod
```

Set password for Zaphod:

```bash
sudo passwd zaphod
```

Create directory **HeartOfGold**:

```bash
sudo mkdir /home/HeartOfGold
```

Set ownership to group **H2G2**:

```bash
sudo chown :H2G2 /home/HeartOfGold
```

### Verify Group & File Information

- Check marvin's groups:
  ```bash
  groups marvin
  ```
- Get group details:
  ```bash
  getent group H2G2
  ```
  or
  ```bash
  grep H2G2 /etc/group
  ```
- Check file ownership:
  ```bash
  ls -ld /home/HeartOfGold
  ```

---

## Install SSH

```bash
sudo apt update
sudo apt install openssh-server
```

### Configure SSH

- Disable password authentication:
  ```bash
  sudo nano /etc/ssh/sshd_config
  ```
  Add:
  ```
  PasswordAuthentication no
  ```

- Change SSH port to `4242`:
  ```
  Port 4242
  ```

- Disable root login:
  ```
  PermitRootLogin no
  ```

Restart SSH:

```bash
sudo systemctl restart ssh
```

### Enable SSH Key Authentication

```bash
ssh-keygen -t rsa -b 2048
```

Copy SSH key:

```bash
ssh-copy-id -p 4242 user@server_ip
```

Test connection:

```bash
ssh -p 4242 user@server_ip
```

---

## Restrict SSH Access for Zaphod

```bash
sudo nano /etc/ssh/sshd_config
```

Add at the end:

```
Match User zaphod
    DenyUsers zaphod
```

---

## Install Fail2Ban

```bash
sudo apt update
sudo apt install fail2ban
```

### Configure Fail2Ban

```bash
sudo nano /etc/fail2ban/jail.conf
```

Add:

```
[sshd]
enabled = true
port = 4242
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
findtime = 5m
bantime = 30m
```

### Verify & Restart Fail2Ban

- Check status:
  ```bash
  sudo systemctl status fail2ban
  ```
- Restart service:
  ```bash
  sudo systemctl restart fail2ban
  ```
- List banned IPs:
  ```bash
  sudo fail2ban-client status sshd
  ```
- Check rules:
  ```bash
  sudo iptables -L
  ```

---

## Setup Firewall with IPTables

```bash
sudo nano /etc/iptables/rules.v4
```

Add:

```
*filter

# Allow SSH (input and output)
-A INPUT -p tcp --dport 4242 -j ACCEPT
-A OUTPUT -p tcp --sport 4242 -j ACCEPT

# Allow HTTP (output)
-A INPUT -p tcp --dport 80 -j ACCEPT
-A OUTPUT -p tcp --dport 80 -j ACCEPT

# Allow HTTPS (output)
-A INPUT -p tcp --dport 443 -j ACCEPT
-A OUTPUT -p tcp --dport 443 -j ACCEPT

# Allow DNS (output)
-A INPUT -p udp --dport 53 -j ACCEPT
-A OUTPUT -p udp --dport 53 -j ACCEPT
-A INPUT -p tcp --dport 53 -j ACCEPT
-A OUTPUT -p tcp --dport 53 -j ACCEPT

# Drop all other incoming traffic
-P INPUT DROP
-P FORWARD DROP
-P OUTPUT DROP

COMMIT
```

### Apply IPTables on Startup

```bash
sudo nano /etc/network/if-pre-up.d/iptables
```

Add:

```bash
#!/bin/sh
iptables-restore < /etc/iptables/rules.v4
```

Make script executable:

```bash
sudo chmod +x /etc/network/if-pre-up.d/iptables
```

Apply rules:

```bash
sudo cat /etc/iptables/rules.v4 | sudo iptables-restore
```

### Test Configuration

- Update packages:
  ```bash
  sudo apt update
  ```
- Reboot & verify persistence:
  ```bash
  sudo reboot
  ```
- Check rules:
  ```bash
  sudo iptables -L
  ```
