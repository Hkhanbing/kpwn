import argparse
import os
import sys

template_path = "~/.kpwn.d"

# 创建框架 create的时候可以软链接
def init():
    print("[+] start init framework")
    if os.path.exists(template_path):
        print("[*] kpwn framework already exists")
        exit(1)
    os.makedirs(template_path)
    os.makedirs(os.path.join(template_path, "templates"))
    os.makedirs(os.path.join(template_path, "tools"))
    os.makedirs(os.path.join(template_path, "src"))
    print("[+] init framework success")

# 创建kpwn工作目录
def create(filename):
    pwd = os.getcwd()
    if os.path.exists(os.path.join(pwd, filename)):
        print("[*] file already exists")
        exit(1)
    os.makedirs(os.path.join(pwd, filename))
    os.makedirs(os.path.join(pwd, filename, "exploit")) # exp目录
    os.makedirs(os.path.join(pwd, filename, "challenge")) # 题目目录
    os.symlink(os.path.join(pwd, filename, "tools"), os.path.join(template_path, "tools")) # 软链接
    os.symlink(os.path.join(pwd, filename, "templates"), os.path.join(template_path, "templates")) # 软链接
    os.symlink(os.path.join(pwd, filename, "src"), os.path.join(template_path, "src")) # 软链接
    print("[+] create kpwn environ successs")

def main():
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description='Generate a kernel pwn struct.')

    # 子parser
    subparsers = parser.add_subparsers(dest='command', help='Subcommands')

    # kpwn init
    subparsers.add_parser('init', help='kpwn init')

    # kpwn create
    create_parser = subparsers.add_parser('create', help='kpwn create <filename>')
    create_parser.add_argument('filename', help='The name of the file to create')

    # 如果没有提供参数，则打印帮助信息
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    # 解析命令行参数

    # 解析命令行参数
    args = parser.parse_args()

    if args.command == 'init':
        init()
    if args.command == 'create':
        create(args.filename)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
