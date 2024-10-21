from setuptools import setup, find_packages

setup(
    name='kpwn',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kpwn = kpwn.cli:main',  # 定义命令和对应的函数
        ],
    },
)
