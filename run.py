from proxypool.api import app
from proxypool.schedule import Schedule

def main():

    s = Schedule()
    s.run()    # 启动后台代理服务
    app.run('127.0.0.1','5555')  # 启动Flask




if __name__ == '__main__':
    main()

