'''
TR069在url获取时会使用dhcp里面的option来发现，这里给出isc-dhcp-server的option生成脚本
'''

def str2hex(s:str)->str:
    ascii_tmp=''
    for char in s :
        ascii_tmp+=str(hex(ord(char)))
    return ascii_tmp.replace("0x",":")

def int2hex(i):
    if i <= 15:
        return "0"+str(hex(i))[2:]
    return str(hex(i))[2:]


def option_43(url,username,passwd):
    option43 = 'option vendor-encapsulated-options '+'01:'+int2hex(len(url))+str2hex(url)+':00:02:'+\
        int2hex(len(username)+len(passwd)+6)+":01:"+int2hex(len(username))+str2hex(username)+":00:02:"+\
            int2hex(len(passwd))+str2hex(passwd)+":00"
    return option43

def option_125(url,username,passwd,idenfiy):
    option125 = 'option vendor-specific-information '+'00:00:0d:e9:'+int2hex(len(url)+len(username)+len(passwd)+len(idenfiy)+14)+ \
        ":0b:"+int2hex(len(url))+str2hex(url)+":0c:1a:01:"+int2hex(len(username))+str2hex(username)+":02:"+int2hex(len(passwd))+\
            ":0D:01:36:0E:04:33:30:30:30:EA:"+int2hex(len(idenfiy))+str2hex(idenfiy)
    return option125

def option_17(url,username,passwd,idenfiy):
    option17 = 'option dhcp6.vendor-opts '+'00:00:0D:E9:00:01:00:'+int2hex(len(url))+str2hex(url)+":00:02:00:"+\
        int2hex(len(username)+len(passwd)+8)+":00:01:00:"+int2hex(len(username))+str2hex(username)+':00:02:00:'+\
            str2hex(passwd)+":00:03:00:01:36:00:04:00:04:33:30:30:30:00:EA:00:"+int2hex(len(idenfiy))+str2hex(idenfiy)
    return option17


if __name__ == "__main__":

    url ="http://www.baidu.com"
    passwd = "dasfafsafasfaf"
    user = "dadasffaf"
    iden ="xxx"
    print(option_125(url,user,passwd,iden))
    print(option_17(url,user,passwd,iden))
    print(option_43(url,user,passwd))
