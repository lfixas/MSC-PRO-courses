# Task01

## Create and Manage Files & Directories

### **Step 1: Create `task01` Directory and Files**

```sh
mkdir task01
cd task01
touch test01
echo -n "If you don't struggle, you don't improve." > test02
chmod 755 test02  # Read & execute for all, write for owner
ln -s test02 test03  # Create symbolic link
```

---

## **Task02**

### **Step 2: Create `task02` Directory and Files**

```sh
mkdir task02
cd task02
echo -e "Z" > z
```

---

## **Task03**

### **Step 3: Create `midLS` Script**

```sh
cd task03
echo '#!/bin/bash' > midLS
echo 'ls -p | grep -v "/$" | grep -v "^\." | sort | tr "\n" "," | sed "s/,$/\n/"' >> midLS
OR
echo 'ls -p | grep -v "/$" | grep -v "^\." | sort | tr "\n" ","' >> midLS
chmod +x midLS  # Make it executable
./midLS  # Execute the script
```

---

## **Task04**

### **Step 4: Create `mr_clean` Script**

```sh
echo '#!/bin/bash' > mr_clean
echo 'find . -type f \( -name "*~" -o -name "#*#" \) -exec rm {} \;' >> mr_clean
chmod +x mr_clean  # Make it executable
```

---

## **Task05**

### **Step 5: Create Git Automation Script**

```sh
echo '#!/bin/bash' > git_commit.sh
echo 'if [ $# -eq 0 ]; then' >> git_commit.sh
echo '    echo "Error: No commit message."' >> git_commit.sh
echo '    exit 1' >> git_commit.sh
echo 'fi' >> git_commit.sh
echo 'git add .' >> git_commit.sh
echo 'git commit -m "$1"' >> git_commit.sh
echo 'git push origin main' >> git_commit.sh
echo 'if [ $? -eq 0 ]; then' >> git_commit.sh
echo '    echo "Push successful."' >> git_commit.sh
echo 'else' >> git_commit.sh
echo '    echo "Error: Push failed."' >> git_commit.sh
echo '    exit 1' >> git_commit.sh
echo 'fi' >> git_commit.sh
echo 'exit 0' >> git_commit.sh

chmod +x git_commit.sh  # Make it executable
```

---

## **Task07**

### **Step 6: Archive Task06 Directory**

```sh
tar czvf task07/task06.tgz task06
```
