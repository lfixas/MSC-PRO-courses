# Day 10

## Install Samba

### On the Server

```bash
sudo apt update
sudo apt install samba
sudo apt install smbclient
```

### On the Client

```bash
sudo apt update
sudo apt install samba
sudo apt install smbclient
```

### Configure `smbclient` on Windows

Reference: [Microsoft Documentation](https://learn.microsoft.com/fr-fr/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3?tab=client)

```bash
sc.exe qc lanmanworkstation
sc.exe config lanmanworkstation depend= bowser/mrxsmb10/mrxsmb20/nsi
sc.exe config mrxsmb10 start= auto
```

### Connect to the Samba Server

```bash
smbclient //10.0.2.15/nsapoolday10 -U lucas
```

---

## User Creation

```bash
sudo useradd -m -d /home/stuxnet Stuxnet
sudo useradd -m -d /home/mirai Mirai
```

Set passwords:

```bash
sudo passwd Stuxnet
sudo passwd Mirai
```

### Create Private Directories

```bash
sudo mkdir -p /home/stuxnet/private
sudo mkdir -p /home/mirai/private
sudo chown Stuxnet:Stuxnet /home/stuxnet/private
sudo chown Mirai:Mirai /home/mirai/private
sudo chmod 700 /home/stuxnet/private
sudo chmod 700 /home/mirai/private
```

### Create Shared Directory

```bash
sudo mkdir -p /home/lucas/nsapoolday10
sudo chown :users /home/lucas/nsapoolday10
sudo chmod 777 /home/lucas/nsapoolday10
```

### Configure Samba

```bash
sudo nano /etc/samba/smb.conf
```

Add:

```
[Stuxnet]
   path = /home/stuxnet/private
   valid users = Stuxnet
   read only = no

[Mirai]
   path = /home/mirai/private
   valid users = Mirai
   read only = no

[Shared]
   path = /home/lucas/nsapoolday10
   valid users = @Stuxnet @Mirai
   read only = no
   writable = yes
   browseable = yes
   guest of = no
   max size = 500
```

### Add Samba Users

```bash
smbpasswd -a Stuxnet
smbpasswd -a Mirai
```

Restart Samba:

```bash
sudo systemctl restart smbd
```

### Test Connection from Client

```bash
smbclient -L //10.0.2.15 -U lucas
smbclient //10.0.2.15/Shared -U Stuxnet
```

---

## Mount Samba Share

### Install CIFS Utils

```bash
sudo apt update
sudo apt install cifs-utils
```

### Create Mount Script

```bash
sudo nano /usr/local/bin/mountsmb.sh
```

Add:

```bash
#!/bin/bash

if grep -qs /mnt/smb_share /proc/mounts; then
   :
else
   mount -t cifs //10.0.2.15/Shared /mnt/smb_share -o username=Stuxnet,password=B94N3v8Ztk
fi
```

Make script executable:

```bash
sudo chmod +x /usr/local/bin/mountsmb.sh
```

### Add Script to Startup

```bash
sudo crontab -e
```

Add:

```
@reboot /bin/bash /usr/local/bin/mountsmb.sh
```

Reboot VM:

```bash
sudo reboot
```

### Verify

```bash
df -h
```

### Test Mount

```bash
sudo mount -a
ls /mnt/smb_share
sudo mkdir -p /mnt/smb_share
```

### Configure FSTAB

```bash
sudo nano /etc/fstab
```

Add:

```
//10.0.2.15/Shared /mnt/smb_share cifs username=Stuxnet,password=root,iocharset=utf8,sec=ntlm 0 0
```

Apply changes:

```bash
sudo mount -a
```

Verify mount:

```bash
df -h
```

Reboot:

```bash
sudo reboot
```

---

## Install ProFTPd

```bash
sudo apt update
sudo apt install proftpd
```

### Configure FTP

```bash
sudo nano /etc/proftpd/proftpd.conf
```

Add:

```
# Set the server name
ServerName "Debian FTP Server"

# Enable TLS
<IfModule mod_tls.c>
    TLSEngine on
    TLSLog /var/log/proftpd/tls.log
    TLSProtocol TLSv1.2
    TLSRequired on
    TLSRSACertificateFile /etc/proftpd/tls/proftpd.crt
    TLSRSACertificateKeyFile /etc/proftpd/tls/proftpd.key
    TLSOptions AllowClientRenegotiations
</IfModule>

# Enable passive FTP connections
PassivePorts 49152 65534
UseReverseDNS off

# DefaultRoot specifies the directory which will be used as the chroot environment for a user.
DefaultRoot ~

# Disable anonymous access
<Anonymous ~>
    User ftp
    Group nogroup
    UserAlias anonymous ftp
    RequireValidShell off
    DenyAll
</Anonymous>
```

### Generate TLS Certificate

```bash
sudo mkdir /etc/proftpd/tls
sudo openssl req -x509 -nodes -newkey rsa:2048 -keyout /etc/proftpd/tls/proftpd.key -out /etc/proftpd/tls/proftpd.crt -days 365
sudo chmod 600 /etc/proftpd/tls/proftpd.key
```

### Restart FTP Server

```bash
sudo systemctl restart proftpd
```

### Test FTP Connection

```bash
ftp 10.0.2.15
```

```bash
Name (10.0.2.15:lucas): Stuxnet
331 Password required for Stuxnet.
Password: B94N3v8Ztk
```

