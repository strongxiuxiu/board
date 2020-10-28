"""
    2020.9.27
    show_strong
"""
from self_func import Cso, InquireCode
from flask import render_template, jsonify, request


def index():
    return render_template("index.html")


def hello_worlds():
    return 'test'


def get_board_count():
    try:
        so = Cso().FCSoCursor()  # 初始化获取so库
    except:
        retu_json = InquireCode().inquire_code(201)  #
        return jsonify(retu_json)
    board_num = so.get_board_count()
    if board_num:
        data = {'board_num': board_num}
        retu_json = InquireCode().inquire_code_list(1, data=data)
        return jsonify(retu_json)
    else:
        data = {'board_num': 0}
        retu_json = InquireCode().inquire_code(1, data=data)
        return jsonify(retu_json)


def get_board_status():  # 获取状态
    try:
        num = request.get_json().get('num')  # 板卡数字
        so = Cso().FCSoCursor()  # 初始化获取so库
    except:
        retu_json = InquireCode().inquire_code(201)  #
        return jsonify(retu_json)
    board_status = so.get_board_state(num)
    data = {'board_status_num': board_status}  # 0 空闲状态 1 工作状态 -1 没有该板卡（若只有一块板卡 输入2）
    retu_json = InquireCode().inquire_code_list(1, data=data)
    return jsonify(retu_json)


def start_data_receiving():
    try:
        num = request.get_json().get('num')  # 板卡数字
        so = Cso().FCSoCursor()  # 初始化获取so库
    except:
        retu_json = InquireCode().inquire_code(201)  #
        return jsonify(retu_json)
    so.Load_library()  # 申请资源
    board_status = so.Start_receiving(num)
    data = {'board_num': board_status}  # 0 空闲状态 1 工作状态 -1 没有该板卡（若只有一块板卡 输入2）
    retu_json = InquireCode().inquire_code_list(1, data=data)
    return jsonify(retu_json)


def stop_data_receiving():
    try:
        num = request.get_json().get('num')  # 板卡数字
        so = Cso().FCSoCursor()  # 初始化获取so库
    except:
        retu_json = InquireCode().inquire_code(201)  #
        return jsonify(retu_json)
    # so.Load_library()  # 申请资源
    board_status = so.Stop_receiving(num)
    data = {'board_num': board_status}  # 0 空闲状态 1 工作状态 -1 没有该板卡（若只有一块板卡 输入2）
    retu_json = InquireCode().inquire_code_list(1, data=data)
    return jsonify(retu_json)


def close_Unload_library():
    try:
        so = Cso().FCSoCursor()
    except:
        retu_json = InquireCode().inquire_code(201)  # 201 请求后台服务繁忙
        return jsonify(retu_json)
    Load_library = so.Unload_library()  # 释放资源
    if Load_library:
        retu_json = InquireCode().inquire_code(110)
        return jsonify(retu_json)
    else:
        retu_json = InquireCode().inquire_code(1)
        return jsonify(retu_json)
