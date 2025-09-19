from netmiko import ConnectHandler, NetmikoTimeoutException
#from getpass import getpass
import time

start_time = time.time()

#devices = [["172.10.50.26", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_10_TEST_SW"]]
devices = [["172.10.50.2", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_10_L3_SW01"],
        ["172.10.50.3", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_10_L3_SW02"],
        ["172.20.120.4", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_20_L3_SW01"],
        ["172.20.120.5", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_20_L3_SW02"],
        ["172.10.50.21", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_10_L2_SW01"],
        ["172.10.50.22", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_10_L2_SW02"]
#        ["172.10.50.23", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_10_L2_SW03"],
#        ["172.10.50.24", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_10_L2_SW04"],
#        ["172.10.50.25", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_10_L2_SW05"],
#        ["172.20.120.23", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_20_L2_SW01"],
#        ["172.20.120.24", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_20_L2_SW02"],
#        ["172.20.120.25", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_20_L2_SW03"],
#        ["172.20.120.26", "2477", "emro_admin", "emro!))$4004", "C9200L-24T-4G", "EMRO_20_L2_SW04"]
        ]

def check(d):

    print("="*80+"\n")
    print("Device Info: 【%s 】 (%s)".center(50)%(d[5], d[0])+"\n")
    print("="*80+"\n")
    cisco = {
            "device_type": "cisco_ios",
            "host": d[0],
            "username": d[2],
            "password": d[3],
            "port": d[1],
            "secret": "emro1004!",
            }
    try:
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        print("\n+"+"-"*78+"+")
        print("|"+"[ config change ]".center(78)+"|")
        print("+"+"-"*78+"+\n")
        print(net_connect.send_config_from_file("showrun.txt"))
        print(net_connect.save_config())
        net_connect.disconnect()
    except NetmikoTimeoutException:
        print("장비 접속 불가(타임아웃)")
    #except NetMikoAuthenticationException:
        #print("장비 접속 불가(인증에러)")

for d in devices:
    check(d)

print("Runtime: %.02f"%(time.time() - start_time))
