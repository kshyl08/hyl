from s24day95 import creat_app
from flask_script import Manager


app = creat_app()
manager = Manager(app)

#第一种
@manager.command
def custom(arg):
    """
    自定义命令
    python manager.py custom 123

    :param arg:
    :return:
    """
    print(arg)
#第二种
@manager.option('-n','--name',dest='name')
@manager.option('-u','--url',dest='url')
def cmd(name,url):
    """
    自定义命令：
    执行：python manager.py cmd -n wupeiqi -u http://www.oldboyedu.com
    :param name:
    :param url:
    :return:
    """


if __name__ == '__main__':
    manager.run()