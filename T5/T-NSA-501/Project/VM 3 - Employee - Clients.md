# Create and configure VM 3 - Employee - Clients

## 1. Create VM in VirtualBox

1. Open **VirtualBox**.
2. Click on **New** to create a new virtual machine.
    - Name and Operating System: 
      - **Name**: VM3-Employee-Client
      - **Type**: Linux
      - **Version**: Debian 12 Bookworm (64-bit)
   - **Memory**: 
     - At least **2048 MB** (or more depending on system resources).
   - **Hard Disk**: 
     - Create a new Virtual Hard Disk
     - Create a new **VDI (VirtualBox Disk Image)**, dynamically allocated
     - Allocate sufficient disk space (e.g., **20GB** or more).
3. Click **Create** to finalize.

---

## 2. Install Debian 12 on VM3

1. Download Debian 12 ISO from: [Debian Official Site](https://www.debian.org/)
2. Start the VM and select the Debian 12 ISO.
3. Follow the Debian 12 installation prompts (**Graphical Install**).

### Installation Steps:

- **Select a language**: **English**
- **Select your location**: **United Kingdom**
- **Configure the keyboard**: **French**
- **Configure the network**:
  - **Hostname**: `root`
  - **Domain name**: (leave blank)
  - **Root password**: `root` (enter twice)
- **Create a new user**:
  - **Full name**: `[Your Name]`
  - **Username**: `[Your Name]`
  - **Password**: `root` (enter twice)

### Partition Disks:

- **Partitioning method**: **Guided - use entire disk**
- **Select disk to partition**: **VBOX HARDDISK**
- **Partitioning scheme**: **Separate `/home`, `/var`, and `/tmp` partitions**
- **Finish partitioning and write changes to disk**: **Yes**

### Configure the Package Manager:

- **Scan extra installation media?** **No**
- **Debian archive mirror country**: **France**
- **Debian archive mirror**: **deb.debian.org**
- **HTTP proxy information**: **(leave blank)**

### Popularity Contest:

- **Participate in package usage survey?** **No**

### Software Selection:

- Choose software to install:
  - ✅ Debian desktop environment
  - ✅ GNOME
  - ✅ SSH server
  - ✅ Standard system utilities

### OpenSSH Server Configuration:

- **What to do with modified sshd_config file?**
  - **Keep the local version currently installed**

---

After completing these steps, **VM3** (Employee Client) will be installed and configured with Debian 12, connected to the correct **internal network**, and ready for use. 🚀