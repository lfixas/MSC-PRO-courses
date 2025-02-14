# Day 08

## Preliminary

### Create User

```bash
sudo useradd -m -d /home/nsapoolday08 nsapoolday08
sudo passwd nsapoolday08
```

Password: `T0dayIt3Scripting`

### Grant Sudo Privileges

```bash
sudo usermod -aG sudo nsapoolday08
```

---

## Script 1 - Calculator

```bash
cd /home/nsapoolday08/
nano script1.sh
```

Add the following:

```bash
#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <operand1> <operator> <operand2>"
    exit 1
fi

# Assign the provided arguments to variables
operand1=$1
operator=$2
operand2=$3

# Perform the operation based on the operator
case $operator in
    +)
        result=$(($operand1 + $operand2))
        ;;
    -)
        result=$(($operand1 - $operand2))
        ;;
    x)
        result=$(($operand1 * $operand2))
        ;;
    /)
        result=$(($operand1 / $operand2))
        ;;
    %)
        result=$(($operand1 % $operand2))
        ;;
    *)
        echo "Invalid operator. Please use +, -, x, /, or %."
        exit 1
        ;;
esac

# Print the result
echo "Result: $result"
```

Make script executable:

```bash
chmod +x script1.sh
```

---

## Script 2 - Menu

```bash
nano script2.sh
```

Add the following:

```bash
#!/bin/bash

while true; do
    echo "MENU:"
    echo "1. Verify user exists"
    echo "2. Check UID"
    echo "q. Exit"

    read -p "Enter your choice: " option

    case $option in
        1)
            read -p "Enter username to verify: " username
            if id "$username" &>/dev/null; then
                echo "User $username exists."
            else
                echo "User $username does not exist."
            fi
            ;;
        2)
            read -p "Enter username to check UID: " username
            uid=$(id -u "$username" 2>/dev/null)
            if [ $? -eq 0 ]; then
                echo "UID of $username: $uid"
            else
                echo "User $username not found."
            fi
            ;;
        q)
            echo "Exiting the program."
            exit 0
            ;;
        *)
            echo "Invalid option. Please choose 1, 2, or q."
            ;;
    esac
done
```

Make script executable:

```bash
chmod +x script2.sh
```

---

## Script 3 - File Processing

```bash
nano script3.sh
```

Add:

```bash
#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_epitech.txt>"
    exit 1
fi

file_path=$1

if [ ! -f "$file_path" ]; then
    echo "Error: File not found."
    exit 1
fi

line_count=$(wc -l < "$file_path")
word_count=$(grep -o -i "epitech" "$file_path" | wc -l)

echo "There are $line_count lines in the file."
echo "The word 'epitech' appears $word_count times."

grep -i "epitech" "$file_path" | tee /tmp/epitech2.txt

echo "Lines with 'epitech' have been written to /tmp/epitech2.txt."
```

Make script executable:

```bash
chmod +x script3.sh
```

---

## Script 4 - System Information

```bash
nano script4.sh
```

Add:

```bash
#!/bin/bash

echo "SYSTEM"
echo "Hostname: $(hostname)"
echo "Manufacturer: $(dmidecode -s system-manufacturer)"
echo "Product name: $(dmidecode -s system-product-name)"
echo "Version: $(dmidecode -s system-version)"
echo "Serial number: $(dmidecode -s system-serial-number)"
echo "Operating system: $(lsb_release -ds)"
echo "Kernel: $(uname -r)"
echo "Architecture: $(arch)"

echo "PRIVATE NETWORK INFORMATION"
ip addr show | awk '/inet / {print $2, $7}'

echo "PUBLIC IP ADDR"
curl -s https://ipinfo.io/ip

echo "DNS"
cat /etc/resolv.conf

echo "CPU USAGE"
echo "Model name: $(lscpu | grep "Model name" | cut -d: -f2 | awk '{$1=$1};1')"
echo "CPU frequency: $(lscpu | grep "CPU MHz" | cut -d: -f2 | awk '{$1=$1};1')"
echo "CPU cores: $(lscpu | grep "^CPU(s):" | cut -d: -f2 | awk '{$1=$1};1')"

echo "DISK SPACE INFO"
df -h | awk '$NF=="/home" || $NF=="/tmp" {print "Free space", $NF ":", $4}'
```

Make script executable:

```bash
chmod +x script4.sh
```

---

## Script 5 - SSH Login Tracking

```bash
nano script5.sh
```

Add:

```bash
#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <ACCEPTED|FAILED>"
    exit 0
fi

status="$1"

if [ "$status" != "ACCEPTED" ] && [ "$status" != "FAILED" ]; then
    echo "Invalid parameter. Please use ACCEPTED or FAILED."
    exit 1
fi

log_file="/var/log/auth.log"

if [ "$status" == "ACCEPTED" ]; then
    grep "Accepted password\|Accepted publickey" "$log_file" | awk '{print "ACCEPTED;" $11 ";" $9}' FS=" "
elif [ "$status" == "FAILED" ]; then
    grep "Failed password\|Failed publickey" "$log_file" | awk '{if($9 == "invalid") print "FAILED;" $13 ";" $11; else print "FAILED;" $11 ";" $9}' FS=" "
fi
```

Make script executable:

```bash
chmod +x script5.sh
```

---

## Bonus - Managing `/tmp/`

```bash
nano copy_epitech_txt.sh
```

Add:

```bash
#!/bin/bash

source_path="./epitech.txt"
destination_path="/tmp/"

if [ -e "$source_path" ]; then
    cp "$source_path" "$destination_path"
    echo "File copied successfully to /tmp/"
else
    echo "Error: Source file '$source_path' not found."
fi
```

Make script executable:

```bash
chmod +x copy_epitech_txt.sh
```