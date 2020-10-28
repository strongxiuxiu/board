import sys
from flask import Flask
import function_method
from flask_cors import *

app = Flask(__name__,
            static_folder='static',
            template_folder="templates")
CORS(app, supports_credentials=True)
app.add_url_rule('/', view_func=function_method.index, methods=["GET"])  # 跳转首页
app.add_url_rule('/api/get_board_count', view_func=function_method.get_board_count, methods=["GET"])  # 获取板卡数量
app.add_url_rule('/api/get_board_status', view_func=function_method.get_board_status, methods=["GET"])  # 获取板卡状态
app.add_url_rule('/api/start_data_receiving', view_func=function_method.start_data_receiving, methods=["GET"])  # 开启接收数据
app.add_url_rule('/api/stop_data_receiving', view_func=function_method.stop_data_receiving, methods=["GET"])  # 停止接收数据
app.add_url_rule('/api/close_Unload_library', view_func=function_method.close_Unload_library, methods=["GET"])  # 释放资源

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 5000

    if sys.argv[1:]:  # 192.168.4.100:8000
        try:
            host, port = sys.argv[1:][0].split(":")
            try:
                functionname, pattern = sys.argv[1:][1].split("=")
                try:
                    import ast

                    pattern = ast.literal_eval(pattern)
                except Exception as e:
                    print('debug参数格式有误错误信息为{},\n'
                          '默认以debug=True启动服务'.format(e))
            except Exception as e:
                print(e)
                pattern = True
                print(2222222222)
        except Exception:
            raise Exception(
                "您输入的参数格式有误,请以x.x.x.x:80启动,\n"
                "如果需要以debug模式运行，请输入参数debug=True\n"
                "启动实例为 python3 runserver.py x.x.x.x:80 debug=True"
            )
        try:
            app.run(host=host, port=port, debug=pattern)
        except Exception as e:
            print("运行错误:{}".format(e))
    else:
        app.run(host=host, port=port, debug=True)
