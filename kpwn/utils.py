# 检查文件类型的函数
def check_file_type(filename):
    import magic  # 确保安装了python-magic库
    mime = magic.Magic(mime=True)
    return mime.from_file(filename)