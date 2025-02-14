# Day 09

## Password Policy

Edit password policy:

```bash
sudo nano /etc/login.defs
```

Modify:

```
PASS_MAX_DAYS   180
PASS_MIN_DAYS   90
PASS_WARN_AGE   7
PASS_MIN_LEN    12
```

Explanation:
- **PASS_MAX_DAYS**: Maximum number of days a password may be used.
- **PASS_MIN_DAYS**: Minimum number of days between password changes.
- **PASS_WARN_AGE**: Number of days warning before a password expires.
- **PASS_MIN_LEN**: Minimum password length.

### Verify Password Policy

```bash
chage -l <user>
```

---

## Users & Groups

### Create Users

```bash
sudo adduser david
sudo adduser alexia
sudo adduser john
sudo adduser martine
sudo adduser karim
```

### Create Groups

```bash
sudo addgroup hr_team
sudo addgroup it_team
sudo addgroup admin
```

### Assign Users to Groups

#### HR Team

```bash
sudo usermod -aG hr_team david
sudo usermod -aG hr_team martine
sudo usermod -aG hr_team karim
```

#### IT Team

```bash
sudo usermod -aG it_team alexia
sudo usermod -aG it_team john
sudo usermod -aG it_team karim
```

#### Admin

```bash
sudo usermod -aG admin karim
```

### Verify Groups

```bash
getent group hr_team
getent group it_team
getent group admin
```

---

## Sudoers Configuration

Edit sudoers file:

```bash
sudo visudo
```

Add:

```
# Allow user john to execute any commands with sudo
john ALL=(ALL:ALL) ALL

# Allow IT team to run specific commands
%it_team ALL=(ALL:ALL) /bin/cat, /bin/ls, /bin/grep
```

---

## SSH Configuration

Edit SSH settings:

```bash
sudo nano /etc/ssh/sshd_config
```

Modify:

```
Port 1337
PermitRootLogin prohibit-password
```

### Restart SSH

```bash
sudo systemctl restart ssh
```

### Test SSH Connection

```bash
ssh -p 1337 <username>@127.0.0.1
```

---

## Disable IPv6

Edit sysctl settings:

```bash
sudo nano /etc/sysctl.conf
```

Add:

```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.all.autoconf = 0
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.default.autoconf = 0
```

### Apply Changes

```bash
sudo sysctl -p
```

### Verify IPv6 Status

```bash
ip a
```

---

## Firewall Configuration

### Install iptables

```bash
sudo apt update
sudo apt install iptables-persistent
```

### Edit Firewall Rules

```bash
sudo nano /etc/iptables/rules.v4
```

Add:

```
*filter
:INPUT DROP [0:0]
:FORWARD DROP [0:0]
:OUTPUT DROP [0:0]

# Allow incoming network packets
-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

# Allow incoming and outgoing traffic on port 1337
-A INPUT -p tcp --dport 1337 -j ACCEPT
-A OUTPUT -p tcp --sport 1337 -j ACCEPT

# Allow outgoing HTTP traffic
-A OUTPUT -p tcp --dport 80 -j ACCEPT

# Allow outgoing HTTPS traffic
-A OUTPUT -p tcp --dport 443 -j ACCEPT

# Allow DNS traffic
-A OUTPUT -p udp -m udp --dport 53 -j ACCEPT
-A OUTPUT -p tcp -m tcp --dport 53 -j ACCEPT

# Allow ping traffic
-A OUTPUT -p icmp -j ACCEPT

COMMIT
```

### Restart Firewall

```bash
sudo service netfilter-persistent restart
```

### Verify Firewall Rules

```bash
sudo iptables -L
```

Test with:

```bash
telnet localhost 1337
```

---

## Install Fail2Ban

```bash
sudo apt update
sudo apt install fail2ban
```

### Configure Fail2Ban

```bash
sudo nano /etc/fail2ban/jail.local
```

Add:

```
[ssh]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
findtime = 30m
bantime = 1800
```

### Restart Fail2Ban

```bash
sudo service fail2ban restart
```

### Verify Fail2Ban Status

```bash
sudo fail2ban-client status ssh
```

### Test SSH Connection

```bash
ssh -p 1337 <username>@127.0.0.1
```

### View Logs

```bash
sudo cat /var/log/auth.log
```

---

## Install SE Linux

```bash
sudo apt update
sudo apt install selinux-basics selinux-policy-default
```

### Activate SE Linux

```bash
sudo selinux-activate
```

### Reboot System

```bash
sudo reboot
```

### Verify SE Linux

```bash
sestatus
```

---

## Install ClamAV (AntiVirus)

```bash
sudo apt update
sudo apt install clamav clamav-daemon
sudo service clamav-freshclam restart
```

### Create Scan Script

```bash
nano clamav_scan.sh
```

Add:

```bash
#!/bin/bash

LOG_FILE="/var/log/clamav/clamav_scan.log"
SCAN_DIR="/"

echo -e "\033[1;32mStarting ClamAV scan at \033[0;36m$(date)\033[1;32m.\033[0m"
echo "Starting ClamAV scan at $(date)" >> "$LOG_FILE"

clamscan -r --exclude-dir="^/sys" --exclude-dir="^/proc" --exclude-dir="^/dev" --exclude-dir="^/run" "$SCAN_DIR" 2>&1 | tee -a "$LOG_FILE"

echo "ClamAV scan completed at $(date)" >> "$LOG_FILE"
echo -e "\033[1;32mClamAV scan completed at \033[0;36m$(date)\033[1;32m.\033[0m"
```

### Make Script Executable

```bash
sudo chmod +x clamav_scan.sh
```

### Schedule ClamAV Scan (Daily at 23:42)

```bash
crontab -e
```

Add:

```
42 23 * * * root /root/clamav_scan.sh
```

### Restart Services

```bash
systemctl restart cron && systemctl restart rsyslog
```

### Verify Cron Job

```bash
crontab -l
```

### View Scan Log

```bash
cat /var/log/clamav/clamav_scan.log
```

Execute Scan Manually:

```bash
echo "Starting ClamAV scan." | wall
/root/clamav_scan.sh
```

Restart Firewall:

```bash
nano /etc/iptables/rules.v4
service netfilter-persistent restart
```

