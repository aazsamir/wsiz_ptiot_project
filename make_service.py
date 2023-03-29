import os

if __name__ == '__main__':
    contents = []
    contents.append("[Unit]")
    contents.append("Description=Local Devices Data Collector Service")
    contents.append("After=network.target")
    contents.append("")

    contents.append("[Service]")
    contents.append("Type=simple")
    localpath = os.path.dirname(os.path.realpath(__file__))
    contents.append("WorkingDirectory=" + localpath)
    contents.append("ExecStart=" + localpath + "/service.py -v")
    contents.append("Restart=always")
    contents.append("RestartSec=3")
    contents.append("Environment=PYTHONUNBUFFERED=1")

    file_content = ""

    for content in contents:
        file_content += content + "\n"

    with open("local_devices_data_collector.service", "w") as f:
        f.write(file_content)

    # move to ~/.config/systemd/user/
    os.system("cp local_devices_data_collector.service ~/.config/systemd/user/")
