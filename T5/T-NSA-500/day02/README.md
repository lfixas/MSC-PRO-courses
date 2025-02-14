# Day 02

## Create Two Network Interfaces

### Install Required Package

```bash
sudo apt install bridge-utils
```

### Configure Bridge Interface

```bash
sudo brctl addif br0 enp0s3
```

### Edit Network Interfaces Configuration

```bash
sudo nano /etc/network/interfaces
```

Add the following:

```
source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug enp0s3
iface enp0s3 inet dhcp

# Private Network
auto enp0s8
allow-hotplug enp0s8
iface enp0s8 inet static
    address 192.168.42.254
    netmask 255.255.255.0
    gateway 192.168.42.255
```

### Restart Network Service

```bash
sudo /etc/init.d/networking restart
```

or

```bash
sudo systemctl restart networking
```

Check status:

```bash
systemctl status networking
```

### Verify Configuration

```bash
ip link
```

> `br0` should be in `state UP`.

---

## Change Hostname to `vm-gateway`

```bash
sudo hostnamectl set-hostname vm-gateway
```

### Verify Hostname

```bash
hostname
```

---

## Install Required Packages

```bash
sudo apt install tcpdump
sudo apt install isc-dhcp-server
sudo apt install bind9
sudo apt install nmap
sudo apt install net-tools
```

---

## Configure DHCP Server

### Edit DHCP Configuration

```bash
sudo nano /etc/dhcp/dhcpd.conf
```

Add:

```
# Sample /etc/dhcp/dhcpd.conf
authoritative;

# Define the private network
subnet 192.168.42.0 netmask 255.255.255.0 {
  range 192.168.42.100 192.168.42.150;
  option routers 192.168.42.254;
}
#    option subnet-mask 255.255.255.0;
#    option broadcast-address 192.168.42.255;
#    default-lease-time 600;
#    max-lease-time 7200;
```

### Configure DHCP Server to Listen on `enp0s8`

```bash
sudo nano /etc/default/isc-dhcp-server
```

Modify:

```
DHCPDv4_CONF=/etc/dhcp/dhcp.conf
INTERFACESv4="enp0s8"
```

### Restart Services

```bash
sudo systemctl restart isc-dhcp-server
sudo systemctl restart networking
```

### Verify DHCP Server Status

```bash
sudo systemctl status isc-dhcp-server
```

### Check Assigned IPs

```bash
sudo ip a
```

> Clients should receive addresses from `192.168.42.100` to `192.168.42.150`.

### Obtain an IP Address Manually

```bash
dhclient enp0s3
ip a
```

---

## Enable IP Forwarding

Edit system configuration:

```bash
sudo nano /etc/sysctl.conf
```

Uncomment or add:

```
net.ipv4.ip_forward=1
```

Apply changes:

```bash
sudo sysctl -p
```

