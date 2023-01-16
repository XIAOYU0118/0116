import time
import ISE_info
import check_method
import json


if __name__ == '__main__':
    '''逐个ISE操作'''
    for node in ISE_info.info:
        print(f'{node} information loading\n')
        session = check_method.PortsCheckHandler(node)
        session.clear()  # 清空已存会话
        new_session = check_method.PortsCheckHandler(node)  # 开启新通道
        new_session.shell.send("\n".encode())
        # new_session.shell.send("\n".encode())
        time.sleep(4)
        output = new_session.shell.recv(65535)  # 接收
        new_session.output_list = output.decode().split("\r\n")
        # print(new_session.output_list)
        print("可以重新接收信息（判断是否可以执行port_check）")

        data_file = open(f"output-{node}.json", "a")

        if f"{new_session.node_name}/admin# " in new_session.output_list:
            print("---Checker running---")
            print(new_session.ports)
            dict_data = {}

            # 逐个端口检测
            for port in new_session.ports:
                new_session.output_list = check_method.send_port_check_command(new_session, port)
                dict_data.update({f'tech netstat | include {port}': new_session.output_list})

            # json格式的输出数据写入文件
            json_data = json.dumps(dict_data)
            data_file.write(json_data)

        data_file.close()
        print("\n文件写入完成。\n")
