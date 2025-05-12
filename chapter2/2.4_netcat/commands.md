# read help
```bash
python netcat.py --help
```
# start and use a shell
start the server
```bash
python netcat.py -t 127.0.0.1 -p 5555 -l -c
```
client
```bash
python netcat.py -t 127.0.0.1 -p 5555
```
press CTRL-D to continue, the script will read until EOF
# execute a single command
start the server
```bash
python netcat.py -t 127.0.0.1 -p 5555 -l -e="cat /etc/passwd"
```
client
```bash
python netcat.py -t 127.0.0.1 -p 5555
```
don't forget CTRL-D
you can also use the original netcat(if you have one)
```bash
nc 127.0.0.1 5555
```
you should get the same response
# HTTP request
use this script to send a HTTP request
```bash
echo -ne "GET / HTTP/1.1\r\nHost: reachtim.com\r\n\r\n" | python ./netcat.py -t reachtim.com -p 80
