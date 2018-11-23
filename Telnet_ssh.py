import telnetlib
import paramiko
import time
'''
封装Telnet和ssh
'''
class Telnet():
    
    def __init__(self,username,password,address,port=23):
        self.username = username
        self.password = password
        self.address = address
        self.port = port
        flag = 0
        while flag < 10:
            try:
                self.tn = telnetlib.Telnet(self.address,self.port)
                self.tn.read_until(b'login: ',timeout=10)  
                self.tn.write(self.username.encode('ascii') + b'\n')
                if self.password:
                    self.tn.read_until(b'Password: ',timeout=10) 
                    self.tn.write(self.password.encode('ascii') + b'\n')
                    time.sleep(2)
                flag = 10
            except Exception as e:
                print("try %d times,%s"%(flag,e))
            flag=flag+1
            
    def cmd(self,command):
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(2)
        command_result = self.tn.read_very_eager().decode('ascii')
        return command_result

    def cloes(self):
        self.tn.write(b"exit\n")

class SSH():

    def __init__(self,username,password,address,port=22):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        flag = 0
        while flag < 10 :
            try:
                self.ssh.connect(address, port, username, password,timeout=5)
                flag = 10
            except Exception as e:
                print("try %d times,%s"%(flag,e))
            flag=flag+1
    
    def cmd(self,command):
        stdin, stdout, stderr = self.ssh.exec_command(command.encode("ascii"))
        time.sleep(2)
        result = stdout.read()
        return result.decode("ascii")
    
    def cloes(self):
        self.ssh.close()


if __name__ =="__main__":
    a = SSH("admin","admin","192.168.1.1")
    t = a.cmd("ifconfig")
    print(t.decode("ascii"))
    a.cloes()
