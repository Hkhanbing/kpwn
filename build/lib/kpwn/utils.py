# 检查文件类型的函数
def check_file_type(filename):
    import magic  # 确保安装了python-magic库
    mime = magic.Magic(mime=True)
    return mime.from_file(filename)

def cleanup_tmux(session_name):
    """关闭 tmux 会话"""
    print(f"[+] 关闭 tmux 会话: {session_name}")
    subprocess.run(["tmux", "kill-session", "-t", session_name])

def signal_handler(sig, frame, session_name):
    """捕捉 Ctrl+C 并清理会话"""
    cleanup_tmux(session_name)
    sys.exit(0)