import paramiko
import ISE_info
import port_list


class ISESSHConnect:
    def __init__(self, node_name):
        self.node_name = node_name
        self.ip = ISE_info.info[node_name]["host"]
        self.username = ISE_info.info[node_name]["username"]
        self.password = ISE_info.info[node_name]["password"]
        self.ca_key = ISE_info.info[node_name]["ca_key"]
        self.persona = ISE_info.info[node_name]["persona"]
        self.ports = port_list.need_to_check[self.persona]
        # self.ssh_session = self.cli_connect()
        self.shell = self.cli_connect()
        self.output_list = []
        self.data_json = {}

    '''创建ssh通道'''
    def cli_connect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
        client.connect(self.ip, port=22, username=self.username, password=self.password)
        shell = client.invoke_shell()
        print("隧道创建成功")
        # shell.keep_this = client
        return shell


# ise = ISESSHConnect("ise01")
# output = ise.remote_terminal.recv(65535)  # 接收
# ise.output_list = output.decode().split("\n")
# print(ise.output_list, end=" ")
# print(ise.persona, ise.ports)
