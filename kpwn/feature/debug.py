import subprocess
import time

def run_tmux_commands():
    # 启动 tmux session
    session_name = "my_session"
    subprocess.run(["tmux", "new-session", "-d", "-s", session_name])

    # 在第一个窗口运行 sh 脚本
    subprocess.run(["tmux", "send-keys", "-t", f"{session_name}:0", "./your_script.sh", "C-m"])

    # 新建一个窗口并运行 gdb
    subprocess.run(["tmux", "split-window", "-h", "-t", f"{session_name}:0"])
    subprocess.run(["tmux", "send-keys", "-t", f"{session_name}:0.1", "gdb", "C-m"])

    # 将 tmux 窗口附加到当前终端
    subprocess.run(["tmux", "attach", "-t", session_name])

if __name__ == "__main__":
    print("启动 tmux 窗口并执行 sh 和 gdb...")
    run_tmux_commands() 
