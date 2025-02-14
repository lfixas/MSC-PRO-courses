# Create and configure VM 1 - Gateway

## 1. Create VM in VirtualBox

1. Open **VirtualBox**.
2. Click on **New** to create a new virtual machine.
    - Name and Operating System: 
      - **Name**: VM1-Gateway
      - **Type**: BSD
      - **Version**: OpenBSD (64-bit)
   - **Memory**: 
     - At least **512 MB** (or more depending on system resources).
   - **Hard Disk**: 
     - Create a new Virtual Hard Disk
     - Create a new **VDI (VirtualBox Disk Image)**, dynamically allocated
     - Allocate sufficient disk space (e.g., **10GB** or more).
3. Click **Create** to finalize.

---

## 2. LAN and NAT Configuration in VirtualBox

### Create LANs:

1. Open **VirtualBox** and select **VM1-Gateway**.
2. Click **Settings** → **Network**.
3. For each **Adapter 1 to Adapter 4**:
   - Set **"Attached to"** to **Internal Network**.
   - Create unique names for each internal network:
     - LAN-1 (Administration)
     - LAN-2 (Server)
     - LAN-3 (Employee)

### Configure NAT:

1. In **VM1-Gateway** settings → **Network**.
2. For **Adapter 1**:
   - Set **"Attached to"** to **NAT**.
   - This adapter will handle internet access.
3. Click **OK** to save.

### Assign Internal Networks to VMs:

- **VM2 (Web Server)** → Connect to **"server"** network.
- **VM3 (Employee Client)** → Connect to **"employee"** network.
- **VM4 (Admin Client)** → Connect to **"administration"** network.

### Configure NAT Rules:

1. Go to **File** → **Preferences** → **Network**.
2. Add a new **NAT network**:
   - Click the green **"+"** icon.
   - Set **CIDR** to `10.0.2.0/24`.

---

## 3. Install OpenBSD on VM

1. Download OpenBSD 7.4: [OpenBSD Official Site](https://www.openbsd.org/)
2. Start the VM and select the [OpenBSD 7.4 ISO](https://cdn.openbsd.org/pub/OpenBSD/7.4/amd64/install74.iso).
3. Follow the installation prompts:
   - Choose **Install** at the boot prompt.
   - Set **keyboard layout** to **fr**.
   - Configure **network interfaces** (use DHCP for now).

---

## 4. Configure LANs on OpenBSD

### Install Nano

```sh
pkg_add -u      # Update packages
pkg_add nano    # Install Nano editor
```

### Edit Network Interfaces

```sh
nano /etc/hostname.em1  # LAN-1 (Administration)
```

Add:

```
inet 192.168.42.1 255.255.255.192
```

Repeat for other interfaces:

```sh
nano /etc/hostname.em2  # LAN-2 (Server)
```

```
inet 192.168.42.65 255.255.255.192
```

```sh
nano /etc/hostname.em3  # LAN-3 (Employee)
```

```
inet 192.168.42.129 255.255.255.192
```

### Start Network Interfaces

```sh
sh /etc/netstart
```

### Configure DHCP

```sh
nano /etc/dhcpd.conf
```

Add:

```
option domain-name-servers 8.8.8.8, 8.8.4.4;

# LAN-1 (Administration)
subnet 192.168.42.0 netmask 255.255.255.192 {
    range 192.168.42.40 192.168.42.60;
    option routers 192.168.42.1;
    option broadcast-address 192.168.42.63;
}

# LAN-2 (Server)
subnet 192.168.42.64 netmask 255.255.255.192 {
    range 192.168.42.70 192.168.42.110;
    option routers 192.168.42.65;
    option broadcast-address 192.168.42.127;

    host server {
        hardware ethernet 08:00:27:03:1d:9d;
        fixed-address 192.168.42.70;
    }
}

# LAN-3 (Employee)
subnet 192.168.42.128 netmask 255.255.255.192 {
    range 192.168.42.140 192.168.42.180;
    option routers 192.168.42.129;
    option broadcast-address 192.168.42.191;
}
```

### Restart DHCP Server

```sh
sudo rcctl restart dhcpd
tail /var/log/daemon  # Check logs
```

### Enable & Start DHCP

```sh
rcctl enable dhcpd
rcctl start dhcpd
```

### Restart Network Interfaces

```sh
sh /etc/netstart em1 em2 em3
```

### Enable IP Forwarding

```sh
sysctl -w net.inet.ip.forwarding=1
```

### Reboot System

```sh
reboot
```

---

## 5. Apply Network Segregation & Security

### Configure PF (Packet Filter) Rules

```sh
nano /etc/pf.conf
```

Add:

```
# Network Interfaces
ext_if="em0"
admin_if="em1"
server_if="em2"
employee_if="em3"

# Skip processing on loopback interface
set skip on lo

# Scrub packets
match in all scrub (no-df)

# Admin LAN → Can access all servers
pass in on $admin_if

# NAT for Admin & Server Networks
pass out on $admin_if inet keep state
pass out on $ext_if inet from $admin_if:network to any nat-to ($ext_if)
pass out on $server_if inet keep state
pass out on $ext_if inet from $server_if:network to any nat-to ($ext_if)

# Block inbound TCP to ports 6000
block return in on ! lo0 proto tcp to port 6000:6000

# Allow Employee LAN to access Server LAN on HTTP/HTTPS
pass proto tcp from 192.168.42.128/26 to 192.168.42.64/26 port { 80, 443 }

# Allow All LANs to Access the Internet & Retrieve DHCP/DNS
pass from { 192.168.42.0/26 192.168.42.64/26 192.168.42.128/26 } to any out
```

### Apply PF Rules

```sh
pfctl -f /etc/pf.conf
pfctl -e
```

---

After completing these steps, your OpenBSD system should be configured with the specified **network interfaces, LANs, and DHCP** for each LAN. **Test the network connectivity** thoroughly to ensure everything is functioning correctly.