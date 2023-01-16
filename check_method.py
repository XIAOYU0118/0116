import ise_ssh_connect
import time
import json


class PortsCheckHandler(ise_ssh_connect.ISESSHConnect):
    def clear(self):
        """已经存在interactive shell, 需要关闭已存在的session"""
        time.sleep(3)
        self.shell.send("1\n".encode())
        time.sleep(2)
        self.shell.send("\x03\n".encode())
        self.shell.send("\n".encode())

        time.sleep(3)
        output = self.shell.recv(65535)  # 接收
        self.output_list = output.decode().split("\n")
        print(self.output_list)

        self.shell.send("exit\n".encode())
        time.sleep(3)
        # self.shell.close()
        print("Existing session has been cleared.")

    def checker(self):
        """开始新的ssh session"""
        if f"{self.node_name}/admin# " in self.output_list:
            print("---Checker running---")
            for port in self.ports:
                self.shell.send(f"tech netstat | include {port}\n".encode())
                time.sleep(3)
                self.shell.send("\x03\n".encode())
                time.sleep(2)
                output = self.shell.recv(65535)
                # self.output_list.clear()
                self.output_list = self.output_list.extend(output.decode().split("\n"))
            print(self.output_list)


# 发送测试命令
def send_port_check_command(session, port):
    session.shell.send(f"tech netstat | include {port}\n".encode())
    time.sleep(2)
    session.shell.send("\x03\n".encode())
    time.sleep(1)
    output = session.shell.recv(65535)
    output_list = output.decode().split("\r\n")
    print(port)
    # print(session.output_list)
    return output_list


# # 修改output数据类型为json
# def data_format(data, port):
#     # data = [['tech netstat | include 8905', '^C', 'auto-ise-02/admin# ', 'auto-ise-02/admin# '],
#     #         ['tech netstat | include 8443', '^C', 'auto-ise-02/admin# ', 'auto-ise-02/admin# ']]
#     # dict_data = {f'tech netstat | include {port}': data[0]}
#     dict_data = {}
#     for i in range(len(data)):
#         dict_data[data[i][0]] = data[i]
#     json_data = json.dumps(dict_data)
#     return json_data

# data_format()
# print(data_format())


# a = PortsCheckHandler("auto-ise-01")
# a.output_list = ['tech netstat | include 9090',
#                  'tcp6       0      0 :::9090                 :::*                    LISTEN      142684/jsvc.exe',
#                  '^C',
#                  'auto-ise-01/admin# ',
#                  'auto-ise-01/admin# ']
# b = a.wr_by_lines()
# print(b
