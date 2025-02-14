# Day 07

## Virtual Machine Setup

### Configure NAT Network

1. **On VirtualBox**:
   - Go to **Tools > NAT Networks** and create a network.

2. **On the Virtual Machines**:
   - Go to **Network > Network NAT** and select the created network.

### Verify Connectivity

```bash
ip -c a
ping [IP of the other machine]
```

---

## Install PostgreSQL

Follow the guide:  
[How to Install PostgreSQL 16 on Debian](https://computingforgeeks.com/how-to-install-postgresql-16-on-debian/)

---

## PostgreSQL - Basic Setup

### Change PostgreSQL Password

```bash
sudo -u postgres psql
```

Inside PostgreSQL:

```sql
\password postgres
```

### Create User `nsapool`

```sql
CREATE USER nsapool WITH PASSWORD 'marvin4242';
```

_(Optional: Grant superuser privileges)_

```sql
ALTER USER nsapool WITH SUPERUSER;
```

### Verify Users

```sql
\du
```

Exit PostgreSQL:

```sql
\q
```

### Verify User Connection

```bash
psql -U postgres -h localhost -d postgres
psql -U nsapool -h localhost -d postgres
```

---

## Create Database & User Table

```bash
psql -U postgres -h localhost -d postgres
```

Inside PostgreSQL:

```sql
CREATE DATABASE nsapoold07;
\c nsapoold07

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    nickname VARCHAR(50) NOT NULL
);

INSERT INTO "user" (email, nickname) VALUES ('marvin@epitech.eu', 'marvin42');

SELECT * FROM "user";
```

---

## PostgreSQL - Advanced Replication

Refer to:
- [How to Set Up PostgreSQL Database Replication](https://www.cherryservers.com/blog/how-to-set-up-postgresql-database-replication#step-2-configure-primary-node)
- [YouTube Tutorial](https://youtu.be/1fv2t1a4G2o?si=w-hw0BcfAKFoViNn)

### Modify PostgreSQL Configuration

```bash
sudo nano /etc/postgresql/16/main/postgresql.conf
```

### Debugging Errors

```bash
sudo journalctl -xe | grep postgresql
```

---

## Replication Test

### On the Master VM

```bash
sudo -u postgres psql
```

Inside PostgreSQL:

```sql
CREATE DATABASE test_replication;
\c test_replication;
CREATE TABLE test_table (id serial PRIMARY KEY, data text);
\q
```

Insert Test Data:

```bash
sudo -u postgres psql -d test_replication -c "INSERT INTO test_table (data) VALUES ('test replication');"
```

### On the Slave VM

```bash
sudo -u postgres psql
```

Inside PostgreSQL:

```sql
\c test_replication;
SELECT * FROM test_table;
\q
```

---

## Backup Script

### Create Backup Directory

```bash
su postgres
mkdir backup
```

### Create Backup Script

```bash
nano backup_script.sh
```

Add:

```bash
#!/bin/bash

# Get current date and time
CURRENT_DAY=$(date +%d)
CURRENT_MONTH=$(date +%m)
CURRENT_YEAR=$(date +%Y)
TIMESTAMP=$(date +%s)

# Database connection parameters
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="user"
DB_USER="postgres"
DB_PASSWORD="marvin4242"

# Backup file name
BACKUP_FILE="backup_${CURRENT_DAY}_${CURRENT_MONTH}_${CURRENT_YEAR}_${TIMESTAMP}.sql"

# Export user table to SQL backup file
pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -t user -Fc > $BACKUP_FILE

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Backup successful. File: $BACKUP_FILE"
else
    echo "Backup failed."
fi
```

### Make Script Executable

```bash
chmod +x backup_script.sh
```

### Run PostgreSQL

```bash
sudo -u postgres psql
```
