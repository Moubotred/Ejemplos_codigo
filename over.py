import paramiko
import sys
import os

# NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
# rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
# aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
# 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
# lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
# P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU 
# z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
# TESKZC0XvTetK0S9xNwm25STk5iWrBvP
# EN632PlfYiZbn3PhVK3XOGSlNInNE00t
# G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
# 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM 
# JVNBBFS mZwKKOP0Xb FXOoW8 chDz5yVRv

try:
	nivel = sys.argv[1]
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname="bandit.labs.overthewire.org", username=f"bandit{nivel}", password=" JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv",port=2220)
	# stdin, stdout, stderr = ssh.exec_command(f"{sys.argv[2] ,sys.argv[3]}")
	# stdin, stdout, stderr = ssh.exec_command("find . -type f")
	# stdin, stdout, stderr = ssh.exec_command("cat data.txt | tr 'A-Z a-z' 'N-ZA-M n-za-m' ")
	while True:
		cmd = input('cmd > ')

		if cmd == 'close':
			ssh.close()

		if cmd == 'clear':
			os.system('cls')

		stdin, stdout, stderr = ssh.exec_command(f"{cmd}")
		
		print(stdout.read().decode())
		print(stderr.read().decode())
		

except Exception:
	print('[x] Susedio un error')





