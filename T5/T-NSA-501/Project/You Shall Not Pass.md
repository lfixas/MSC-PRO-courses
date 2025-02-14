# You Shall Not Pass - Virtual Network Security Project

> [!IMPORTANT]
> This guide uses **VirtualBox** for virtualization. If you're using another platform (e.g., VMware), configurations may vary.

## Project Overview

This project involves setting up a secure virtual network with **three virtual machines (VMs)**:

- **VM 1**: **Gateway** (OpenBSD 7.4) – Manages network traffic & security.
- **VM 2**: **Web Server** (FreeBSD 13) – Hosts a web application & database.
- **VM 3 & VM 4**: **Clients** (Linux) – Connect to the network via DHCP.

---

## VM 1 - Gateway (OpenBSD 7.4)

### **Network Configuration**
- **Configure 4 network interfaces with static IPs.**
- **Setup bridge or NAT for internet access.**
- **Create 3 private networks (LANs) with these IP ranges:**

| LAN | Name | Network | Broadcast | DHCP Range |
|---|---|---|---|---|
| 1 | Administration | `192.168.42.0` | `192.168.42.63` | `192.168.42.40 - 192.168.42.60` |
| 2 | Server | `192.168.42.64` | `192.168.42.127` | `192.168.42.70 - 192.168.42.110` |
| 3 | Employee | `192.168.42.128` | `192.168.42.191` | `192.168.42.140 - 192.168.42.180` |

- **Set correct subnet masks for each network.**

### **Packet Filtering & Security (PF Configuration)**
- **Admin LAN**: Full access to servers on all ports.
- **Employee LAN**: Can access **only** HTTP/HTTPS on the server.
- **All LANs**: Can access the internet, ping other subnets, and use DHCP/DNS.

[📜 Detailed VM 1 Gateway Configuration](VM%201%20-%20Gateway.md)

---

## VM 2 - Web Server (FreeBSD 13)

### **Web Server Configuration**
- **Install NGINX, PHP 7.4, and required modules.**
- **Deploy the provided webpage.**
- **Ensure DHCP assigns it a fixed IP (`192.168.42.70`).**

### **Database Configuration**
- **Install MySQL Server (`mysql80-server`).**
- **Install the `nsa501` database.**
- **Create a MySQL user with:**

| User | Rights | Database | Password |
|---|---|---|---|
| backend | All privileges | nsa501 | `Bit8Q6a6G` |

[📜 Detailed VM 2 Web Server Configuration](VM%202%20-%20Server%20Web.md)

---

## VM 3 & VM 4 - Clients

### **Operating System Installation**
- Install **Debian 12**, Ubuntu, or any other OS with a **GUI**.

### **Network Configuration**
- Set network adapters to **automatically retrieve IPs from DHCP.**

[📜 Detailed VM 3 Employee Client Configuration](VM%203%20-%20Employee%20-%20Clients.md)

---

### **Additional Configuration** 
- Ensure firewall rules are correctly applied for client access. 
- Test the connectivity between clients and servers to verify configurations.

This setup ensures **proper network segmentation, security, and controlled access** between different network segments. 🚀
