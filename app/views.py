# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

<<<<<<< HEAD
from flask import render_template, request, jsonify, redirect, url_for, flash, send_from_directory
from app import app
from forms import configForm_aaaa, configForm_a, configForm_aa, configForm_aaa
import glob
import os
from datetime import datetime as dt
=======
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect
from flask import render_template, request, jsonify, redirect, url_for, flash, send_from_directory, Flask, session
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from app import app, basedir,ALLOWED_EXTENSIONS
from forms import configForm_aaaa, configForm_a, configForm_aa, configForm_aaa, NameForm
from models import User
import glob
import os
import time
from datetime import datetime as dt
import base64
# import paramiko
>>>>>>> the lastst version on 2018/05
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yaml
<<<<<<< HEAD
=======
import platform

>>>>>>> the lastst version on 2018/05

CONFIG_FILE_A = 'config_a.yml'
CONFIG_FILE_AA = 'config_aa.yml'
CONFIG_FILE_AAA = 'config_aaa.yml'
CONFIG_FILE_AAAA = 'config_aaaa.yml'


<<<<<<< HEAD
@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("/index.html")


@app.route("/report1", methods=["GET", "POST"])
=======

# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)


# csrf protection
csrf = CsrfProtect()
csrf.init_app(app)

# 这个callback函数用于reload User object，根据session中存储的user id


@login_manager.user_loader
# 加载用户的回调函数接收以Unicode字符串形式表示的用户标示符
# 如果能找到用户，这个函数必须返回用户对象，否则返回None。
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/index', methods=["GET", "POST"])
@login_required
def index():
    return render_template(
        'index.html', username=current_user.username)
# ...


# ...
# 添加登录视图，如果是GET方法，返回一个简单的表单

@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=['GET', 'POST'])
# 当请求为GET时，直接渲染模板，当请求是POST提交时，验证表格数据，然后尝试登入用户。
def login():
    form = NameForm()
    if form.validate_on_submit():
        print form.username.data  # 表格中填入了数据，执行下面操作
        user = User.query.filter_by(username=form.username.data).first()
        # 视图函数使用表单中填写的email加载用户

        if user is not None and user.verify_password(form.password.data):
            # 如果user不是空的，而且验证表格中的密码正确，执行下面的语句，调用Flask_Login中的login_user（）函数，在用户会话中把用户标记为登录。
            # 否则直接执行flash消息和跳转到新表格中。
            login_user(user, remember=True)
            print 'success'
            # login_user函数的参数是要登录的用户，以及可选的‘记住我’布尔值。
            return redirect(request.args.get('next') or url_for('index'))
            # 用户访问未授权的ＵＲＬ时会显示登录表单，Flask-Login会把原地址保存在查询字符串的next参数中，这个参数可从request.args字典中读取。如果查询字符串中没有next参数，则重定向到首页。
        else:
            # error = {
            #     message:u"用户名密码错误"
            # }
            # return jsonify(error)
            flash('用户名/密码错误!!!', 'error')
            print 'failed'
    return render_template('login.html', form=form)


@app.route('/logout')
# 退出路由
@login_required
# 用户要求已经登录
def logout():
    logout_user()
    # 登出用户，这个视图函数调用logout_user()函数，删除并重设用户会话。
    # 显示flash消息
    return redirect(url_for('login'))
    # 重定向到登录页

@app.route("/upload", methods=["GET", "POST"])
@csrf.exempt
@login_required
def upload():
    return render_template('upload.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/uploadSomefiles", methods=["GET", "POST"])
@csrf.exempt
def uploadSomefiles():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file[]")
        result = {}
        # basedir = '/home/svn/Taffy_Web-master/app
        # app.config['UPLOAD_FOLDER'] = '../upload/dingdang_auto/TestCase'
        file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
        print file_dir
        if not os.path.exists(file_dir):
             os.makedirs(file_dir)
        for file in uploaded_files:
            fname = file.filename
            # print fname,uploaded_files
            if file and allowed_file(fname):
                filename = secure_filename(fname)
                save_dir = os.path.join(file_dir, filename)
                print save_dir
                file.save(save_dir)
                # print filename
                result['desc'] = 0
                result['message'] = u'上传成功'
            else:
                result['desc'] = 1001
                result['message'] = u'文件不存在或格式错误，请检查'
            #     return jsonify(result)
    return jsonify(result)




@app.route("/report1", methods=["GET", "POST"])
@login_required
>>>>>>> the lastst version on 2018/05
def report1():
    return render_template("/report1.html")


@app.route("/report2", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def report2():
    return render_template("/report2.html")


@app.route("/report3", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def report3():
    return render_template("/report3.html")


@app.route("/report4", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def report4():
    return render_template("/report4.html")


@app.route("/case4", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def case4():
    if request.method == "GET":
        return render_template("/case4.html")


@app.route("/case3", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def case3():
    if request.method == "GET":
        return render_template("/case3.html")


@app.route("/case2", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def case2():
    if request.method == "GET":
        return render_template("/case2.html")


@app.route("/case1", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def case1():
    if request.method == "GET":
        return render_template("/case1.html")


@app.route("/config", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def config():
    form_a = configForm_a()
    form_aa = configForm_aa()
    form_aaa = configForm_aaa()
    form_aaaa = configForm_aaaa()

    config_a = yaml.load(file(CONFIG_FILE_A, 'r'))
    if form_a.validate_on_submit():
        del form_a.data['csrf_token']
        config_a = form_a.data
        yaml.dump(form_a.data, open(CONFIG_FILE_A, 'w'))
        flash(u'配置保存成功！', 'success')
        return redirect(url_for('config'))
# 读取yml中配置
    for c in config_a:
        getattr(form_a, c).data = config_a[c]

    config_aa = yaml.load(file(CONFIG_FILE_AA, 'r'))
    if form_aa.validate_on_submit():
        del form_aa.data['csrf_token']
        config_aa = form_aa.data
        yaml.dump(form_aa.data, open(CONFIG_FILE_AA, 'w'))
        flash(u'配置保存成功！', 'success')
        return redirect(url_for('config'))
    for a in config_aa:
        getattr(form_aa, a).data = config_aa[a]

    config_aaa = yaml.load(file(CONFIG_FILE_AAA, 'r'))
    if form_aaa.validate_on_submit():
        del form_aaa.data['csrf_token']
        config_aaa = form_aaa.data
        yaml.dump(form_aaa.data, open(CONFIG_FILE_AAA, 'w'))
        flash(u'配置保存成功！', 'success')
        return redirect(url_for('config'))
    for b in config_aaa:
        getattr(form_aaa, b).data = config_aaa[b]

    config_aaaa = yaml.load(file(CONFIG_FILE_AAAA, 'r'))
    if form_aaaa.validate_on_submit():
        del form_aaaa.data['csrf_token']
        config_aaaa = form_aaaa.data
        yaml.dump(form_aaaa.data, open(CONFIG_FILE_AAAA, 'w'))
        flash(u'配置保存成功！', 'success')
        return redirect(url_for('config'))
    for d in config_aaaa:
        getattr(form_aaaa, d).data = config_aaaa[d]

    return render_template("/config.html", form_a=form_a, form_aa=form_aa, form_aaa=form_aaa, form_aaaa=form_aaaa)


<<<<<<< HEAD
# @app.route("/getCaseA_list_page",methods=["GET", "POST"])
# def getCaseA_list_page():
#     page_dict = {
#         'page_content':None,
#         'page_count':None
#     }
#     if request.method == "POST":
#         page_num = request.POST.get('page',None)
#         data_count = request.POST.get('count',None)
#         print page_num,data_count
@app.route("/getCaseA", methods=["GET", "POST"])
def getCaseA():
    if request.method == "GET":
        # 读取配置
        config_aa = yaml.load(file(CONFIG_FILE_A, 'r'))
        # taffy项目路径
        taffy_dir_A = config_aa['taffy_dir']
        result_a = {}
        result_a["case_paths"] = glob.glob(taffy_dir_A + '/**/Test_*.py')
=======
@app.route("/getCaseA", methods=["GET", "POST"])
@login_required
def getCaseA():
    if request.method == "GET":
        # 读取配置
        # config_aa = yaml.load(file(CONFIG_FILE_A, 'r'))
        # taffy项目路径
        # app.config['UPLOAD_FOLDER']='../upload/dingdang_auto/TestCase'
        taffy_dir_A = app.config['UPLOAD_FOLDER'][3:]
        print taffy_dir_A
        result_a = {}
        result_a["case_paths"] = glob.glob(taffy_dir_A + '/Test*.py')
>>>>>>> the lastst version on 2018/05
        # result = glob.glob(taffy_dir + '/**/test_*.py')
        # print jsonify(result)
        return jsonify(result_a)


@app.route("/countPagesA", methods=["GET", "POST"])
<<<<<<< HEAD
def countPagesA():
    if request.method == "GET":
        # 读取配置
        config = yaml.load(file(CONFIG_FILE_A, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir']
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/**/Test_*.py')
=======
@login_required
def countPagesA():
    if request.method == "GET":
        # 读取配置
        # config = yaml.load(file(CONFIG_FILE_A, 'r'))
        # taffy项目路径
        taffy_dir = app.config['UPLOAD_FOLDER'][3:]
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/Test*.py')
>>>>>>> the lastst version on 2018/05
        total_count = len(result["case_paths"])
        total_page = 0
        case_list = []
        a, b = divmod(total_count, 10)
        if b != 0:
            total_page = a + 1
            return jsonify(total_page)
        else:
            total_page = a
            return jsonify(total_page)


@app.route("/getPageA", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@login_required
>>>>>>> the lastst version on 2018/05
def getPageA():
    if request.method == "GET":
        page_index = int(request.args.get('pageNo'))
        # 读取配置
<<<<<<< HEAD
        config = yaml.load(file(CONFIG_FILE_A, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir']
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/**/Test_*.py')
=======
        # config = yaml.load(file(CONFIG_FILE_A, 'r'))
        # taffy项目路径
        taffy_dir = app.config['UPLOAD_FOLDER'][3:]
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/Test*.py')
>>>>>>> the lastst version on 2018/05
        total_count = len(result["case_paths"])
        total_page = 0
        case_list = []
        start_index = 10 * (page_index - 1)
        end_index = 10 * page_index - 1
        a, b = divmod(total_count, 10)
        if b != 0:
            total_page = a + 1
            if page_index <= total_page:
                for case_index in range(start_index, end_index + 1):
                    if case_index < total_count:
                        case_list.append(result["case_paths"][case_index])
                    else:
                        break
<<<<<<< HEAD
                    print jsonify(case_list)
=======
                    # print jsonify(case_list)
>>>>>>> the lastst version on 2018/05
            return jsonify(case_list)
        else:
            total_page = a
            if page_index <= total_page:
                for case_index in range(start_index, end_index + 1):
                    if case_index < total_count:
                        case_list.append(result["case_paths"][case_index])
                    else:
                        break
<<<<<<< HEAD
                    print jsonify(case_list)
=======
                    # print jsonify(case_list)
>>>>>>> the lastst version on 2018/05
            return jsonify(case_list)


@app.route("/getCaseAA", methods=["GET", "POST"])
def getCaseAA():
    if request.method == "GET":
        # 读取配置
        config_a = yaml.load(file(CONFIG_FILE_AA, 'r'))
        # taffy项目路径
        taffy_dir = config_a['taffy_dir_A']
        result_a = {}
        result_a["case_paths"] = glob.glob(taffy_dir + '/**/Test_*.py')
        return jsonify(result_a)


@app.route("/countPagesAA", methods=["GET", "POST"])
def countPagesAA():
    if request.method == "GET":
        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_A']
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/**/Test_*.py')
        total_count = len(result["case_paths"])
        total_page = 0
        case_list = []
        a, b = divmod(total_count, 10)
        if b != 0:
            total_page = a + 1
            return jsonify(total_page)
        else:
            total_page = a
            return jsonify(total_page)


@app.route("/getPageAA", methods=["GET", "POST"])
def getPageAA():
    if request.method == "GET":
        page_index = int(request.args.get('pageNo'))
        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_A']
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/**/Test_*.py')
        total_count = len(result["case_paths"])
        total_page = 0
        case_list = []
        start_index = 10 * (page_index - 1)
        end_index = 10 * page_index - 1
        a, b = divmod(total_count, 10)
        if b != 0:
            total_page = a + 1
            if page_index <= total_page:
                for case_index in range(start_index, end_index + 1):
                    if case_index < total_count:
                        case_list.append(result["case_paths"][case_index])
                    else:
                        break
<<<<<<< HEAD
                    print jsonify(case_list)
=======
                    # print jsonify(case_list)
>>>>>>> the lastst version on 2018/05
            return jsonify(case_list)
        else:
            total_page = a
            if page_index <= total_page:
                for case_index in range(start_index, end_index + 1):
                    if case_index < total_count:
                        case_list.append(result["case_paths"][case_index])
                    else:
                        break
<<<<<<< HEAD
                    print jsonify(case_list)
=======
                    # print jsonify(case_list)
>>>>>>> the lastst version on 2018/05
            return jsonify(case_list)


@app.route("/getCaseAAA", methods=["GET", "POST"])
def getCaseAAA():
    if request.method == "GET":
        # 读取配置
        config_aa = yaml.load(file(CONFIG_FILE_AAA, 'r'))
        # taffy项目路径
        taffy_dir_AAA = config_aa['taffy_dir_AA']
        # a = glob.glob(taffy_dir + '/**/test_*.py')
        # result = {
        #     "case_paths":a
        #     }
        result_aa = {}
<<<<<<< HEAD
        result_aa["case_paths"] = glob.glob(taffy_dir_AAA + '/**/locustfile_*.py')
=======
        result_aa["case_paths"] = glob.glob(
            taffy_dir_AAA + '/**/locustfile_*.py')
>>>>>>> the lastst version on 2018/05
        # result = glob.glob(taffy_dir + '/**/test_*.py')
        # print jsonify(result)
        return jsonify(result_aa)


@app.route("/countPagesAAA", methods=["GET", "POST"])
def countPagesAAA():
    if request.method == "GET":
        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AAA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_AA']
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/**/locustfile_*.py')
        total_count = len(result["case_paths"])
        total_page = 0
        case_list = []
        a, b = divmod(total_count, 10)
        if b != 0:
            total_page = a + 1
            return jsonify(total_page)
        else:
            total_page = a
            return jsonify(total_page)


@app.route("/getPageAAA", methods=["GET", "POST"])
def getPageAAA():
    if request.method == "GET":
        page_index = int(request.args.get('pageNo'))
        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AAA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_AA']
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/**/locustfile_*.py')
        total_count = len(result["case_paths"])
        total_page = 0
        case_list = []
        start_index = 10 * (page_index - 1)
        end_index = 10 * page_index - 1
        a, b = divmod(total_count, 10)
        if b != 0:
            total_page = a + 1
            if page_index <= total_page:
                for case_index in range(start_index, end_index + 1):
                    if case_index < total_count:
                        case_list.append(result["case_paths"][case_index])
                    else:
                        break
<<<<<<< HEAD
                    print jsonify(case_list)
=======
                    # print jsonify(case_list)
>>>>>>> the lastst version on 2018/05
            return jsonify(case_list)
        else:
            total_page = a
            if page_index <= total_page:
                for case_index in range(start_index, end_index + 1):
                    if case_index < total_count:
                        case_list.append(result["case_paths"][case_index])
                    else:
                        break
<<<<<<< HEAD
                    print jsonify(case_list)
=======
                    # print jsonify(case_list)
>>>>>>> the lastst version on 2018/05
            return jsonify(case_list)


@app.route("/getCaseAAAA", methods=["GET", "POST"])
def getCaseAAAA():
    if request.method == "GET":
        # 读取配置
        config_bb = yaml.load(file(CONFIG_FILE_AAAA, 'r'))
        # taffy项目路径
        taffy_dir_BB = config_bb['taffy_dir_BB']
        # a = glob.glob(taffy_dir + '/**/test_*.py')
        # result = {
        #     "case_paths":a
        #     }
        result_bb = {}
        result_bb["case_paths"] = glob.glob(taffy_dir_BB + '/**/Test*.py')
        # result = glob.glob(taffy_dir + '/**/test_*.py')
        # print jsonify(result)
        return jsonify(result_bb)


@app.route("/countPagesAAAA", methods=["GET", "POST"])
def countPagesAAAA():
    if request.method == "GET":
        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AAAA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_BB']
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/**/Test_*.py')
        total_count = len(result["case_paths"])
        total_page = 0
        case_list = []
        a, b = divmod(total_count, 10)
        if b != 0:
            total_page = a + 1
            return jsonify(total_page)
        else:
            total_page = a
            return jsonify(total_page)


@app.route("/getPageAAAA", methods=["GET", "POST"])
def getPageAAAA():
    if request.method == "GET":
        page_index = int(request.args.get('pageNo'))
        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AAAA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_BB']
        result = {}
        result["case_paths"] = glob.glob(taffy_dir + '/**/Test_*.py')
        total_count = len(result["case_paths"])
        total_page = 0
        case_list = []
        start_index = 10 * (page_index - 1)
        end_index = 10 * page_index - 1
        a, b = divmod(total_count, 10)
        if b != 0:
            total_page = a + 1
            if page_index <= total_page:
                for case_index in range(start_index, end_index + 1):
                    if case_index < total_count:
                        case_list.append(result["case_paths"][case_index])
                    else:
                        break
<<<<<<< HEAD
                    print jsonify(case_list)
=======
                    # print jsonify(case_list)
>>>>>>> the lastst version on 2018/05
            return jsonify(case_list)
        else:
            total_page = a
            if page_index <= total_page:
                for case_index in range(start_index, end_index + 1):
                    if case_index < total_count:
                        case_list.append(result["case_paths"][case_index])
                    else:
                        break
<<<<<<< HEAD
                    print jsonify(case_list)
=======
                    # print jsonify(case_list)
>>>>>>> the lastst version on 2018/05
            return jsonify(case_list)


@app.route("/saveCase_A", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@csrf.exempt
>>>>>>> the lastst version on 2018/05
def saveCase_A():
    if request.method == "POST":
        caseName = request.form.get("caseName")
        caseScript = request.form.get("caseScript").encode('utf-8')
        mode = request.form.get("mode")
        result = {}

        # 读取配置
        config = yaml.load(file(CONFIG_FILE_A, 'r'))
        # taffy项目路径
<<<<<<< HEAD
        taffy_dir = config['taffy_dir']

=======
        # taffy_dir = config['taffy_dir']
        taffy_dir = app.config['UPLOAD_FOLDER'][3:]
>>>>>>> the lastst version on 2018/05
        # 判断文件是否含有路径
        if '/' in caseName:
            caseFile = caseName
            caseName = caseName.split('/')[-1]
        elif '\\' in caseName:
            caseFile = caseName
            caseName = caseName.split('\\')[-1]
        else:
            # 先判断文件夹是否存在，不存在则新建
<<<<<<< HEAD
            caseDir = os.path.join(taffy_dir, 'Tests')
=======
            caseDir = taffy_dir
>>>>>>> the lastst version on 2018/05
            if not os.path.exists(caseDir):
                os.makedirs(caseDir)
            caseFile = os.path.join(caseDir, caseName)

        if caseName.startswith('Test_') and caseName.endswith('.py'):
            # 新建文件不可重复
            if u'新建' in mode:
                if os.path.exists(caseFile):
                    result['desc'] = u'文件已存在：{0}'.format(caseFile)
                else:
                    try:
                        with open(caseFile, 'w') as f:
                            f.write(caseScript)
                        result['desc'] = 'pass'
                    except Exception as e:
                        result['desc'] = u'文件保存失败：{0}'.format(e)
            elif u'编辑' in mode:
                try:
                    with open(caseFile, 'w') as f:
                        f.write(caseScript)
                    result['desc'] = 'pass'
                except Exception as e:
                    result['desc'] = u'文件保存失败：{0}'.format(e)
        else:
            result['desc'] = u'文件格式错误：非Test_xxx.py格式'
        return jsonify(result)


@app.route("/saveCase_AA", methods=["GET", "POST"])
def saveCase_AA():
    if request.method == "POST":
        caseName = request.form.get("caseName")
        caseScript = request.form.get("caseScript").encode('utf-8')
        mode = request.form.get("mode")
        result = {}

        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_A']

        # 判断文件是否含有路径
        if '/' in caseName:
            caseFile = caseName
            caseName = caseName.split('/')[-1]
        elif '\\' in caseName:
            caseFile = caseName
            caseName = caseName.split('\\')[-1]
        else:
            # 先判断文件夹是否存在，不存在则新建
            caseDir = os.path.join(taffy_dir, 'Tests')
            if not os.path.exists(caseDir):
                os.makedirs(caseDir)
            caseFile = os.path.join(caseDir, caseName)

        if caseName.startswith('Test_') and caseName.endswith('.py'):
            # 新建文件不可重复
            if u'新建' in mode:
                if os.path.exists(caseFile):
                    result['desc'] = u'文件已存在：{0}'.format(caseFile)
                else:
                    try:
                        with open(caseFile, 'w') as f:
                            f.write(caseScript)
                        result['desc'] = 'pass'
                    except Exception as e:
                        result['desc'] = u'文件保存失败：{0}'.format(e)
            elif u'编辑' in mode:
                try:
                    with open(caseFile, 'w') as f:
                        f.write(caseScript)
                    result['desc'] = 'pass'
                except Exception as e:
                    result['desc'] = u'文件保存失败：{0}'.format(e)
        else:
            result['desc'] = u'文件格式错误：非Test_xxx.py格式'
        return jsonify(result)


@app.route("/saveCase_AAA", methods=["GET", "POST"])
def saveCase_AAA():
    if request.method == "POST":
        caseName = request.form.get("caseName")
        caseScript = request.form.get("caseScript").encode('utf-8')
        mode = request.form.get("mode")
        result = {}

        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AAA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_AA']

        # 判断文件是否含有路径
        if '/' in caseName:
            caseFile = caseName
            caseName = caseName.split('/')[-1]
        elif '\\' in caseName:
            caseFile = caseName
            caseName = caseName.split('\\')[-1]
        else:
            # 先判断文件夹是否存在，不存在则新建
            caseDir = os.path.join(taffy_dir, 'Tests')
            if not os.path.exists(caseDir):
                os.makedirs(caseDir)
            caseFile = os.path.join(caseDir, caseName)

        if caseName.startswith('Test_') and caseName.endswith('.py'):
            # 新建文件不可重复
            if u'新建' in mode:
                if os.path.exists(caseFile):
                    result['desc'] = u'文件已存在：{0}'.format(caseFile)
                else:
                    try:
                        with open(caseFile, 'w') as f:
                            f.write(caseScript)
                        result['desc'] = 'pass'
                    except Exception as e:
                        result['desc'] = u'文件保存失败：{0}'.format(e)
            elif u'编辑' in mode:
                try:
                    with open(caseFile, 'w') as f:
                        f.write(caseScript)
                    result['desc'] = 'pass'
                except Exception as e:
                    result['desc'] = u'文件保存失败：{0}'.format(e)
        else:
            result['desc'] = u'文件格式错误：非Test_xxx.py格式'
        return jsonify(result)


@app.route("/saveCase_AAAA", methods=["GET", "POST"])
def saveCase_AAAA():
    if request.method == "POST":
        caseName = request.form.get("caseName")
        caseScript = request.form.get("caseScript").encode('utf-8')
        mode = request.form.get("mode")
        result = {}

        # 读取配置
        config = yaml.load(file(CONFIG_FILE_AAAA, 'r'))
        # taffy项目路径
        taffy_dir = config['taffy_dir_BB']

        # 判断文件是否含有路径
        if '/' in caseName:
            caseFile = caseName
            caseName = caseName.split('/')[-1]
        elif '\\' in caseName:
            caseFile = caseName
            caseName = caseName.split('\\')[-1]
        else:
            # 先判断文件夹是否存在，不存在则新建
            caseDir = os.path.join(taffy_dir, 'Tests')
            if not os.path.exists(caseDir):
                os.makedirs(caseDir)
            caseFile = os.path.join(caseDir, caseName)

        if caseName.startswith('Test_') and caseName.endswith('.py'):
            # 新建文件不可重复
            if u'新建' in mode:
                if os.path.exists(caseFile):
                    result['desc'] = u'文件已存在：{0}'.format(caseFile)
                else:
                    try:
                        with open(caseFile, 'w') as f:
                            f.write(caseScript)
                        result['desc'] = 'pass'
                    except Exception as e:
                        result['desc'] = u'文件保存失败：{0}'.format(e)
            elif u'编辑' in mode:
                try:
                    with open(caseFile, 'w') as f:
                        f.write(caseScript)
                    result['desc'] = 'pass'
                except Exception as e:
                    result['desc'] = u'文件保存失败：{0}'.format(e)
        else:
            result['desc'] = u'文件格式错误：非Test_xxx.py格式'
        return jsonify(result)


@app.route("/readCase", methods=["GET", "POST"])
def readCase():
    if request.method == "GET":
        caseName = request.args.get("caseName")
        result = {}
        try:
            with open(caseName, 'r') as f:
                result['content'] = f.read()
        except Exception as e:
            result['exception'] = u'文件读取失败：{0}'.format(e)
<<<<<<< HEAD
        return jsonify(result)
=======
    return jsonify(result)
>>>>>>> the lastst version on 2018/05


# @app.route("/downloadCase",methods=["GET","POST"])
# def downloadCase():
#     if request.method == "GET":
#         caseName = request.args.get("caseName")
#         store_path = os.getcwd()
#         return send_from_directory(store_path, caseName, as_attachment=True)


@app.route("/delCase", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@csrf.exempt
>>>>>>> the lastst version on 2018/05
def delCase():
    if request.method == "POST":
        # 获取数组参数
        caseFiles = request.form.getlist("caseFiles[]")
        result = {}
        try:
            for f in caseFiles:
                os.remove(f)
            result['desc'] = 'pass'
        except Exception as e:
            result['desc'] = u'文件删除失败：{0}'.format(e)
        return jsonify(result)


@app.route("/runCase", methods=["GET", "POST"])
<<<<<<< HEAD
=======
@csrf.exempt
>>>>>>> the lastst version on 2018/05
def runCase():
    if request.method == "POST":
        # 获取数组参数
        caseFiles = request.form.getlist("caseFiles[]")
        result = {}
<<<<<<< HEAD
        try:
            caseFiles = ' '.join(
                map(lambda i: '"' + i + '"', caseFiles)).encode('gbk')
            config_a = yaml.load(file(CONFIG_FILE_A, 'r'))
            # Taffy路径
            taffy_dir = config_a['taffy_dir']
            # 测试报告名称
            report_name = config_a['report_name'] + \
                '_{0}.html'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
            # 先判断文件夹是否存在，不存在则新建
            reportDir = os.path.join(taffy_dir, 'Results')
            if not os.path.exists(reportDir):
                os.makedirs(reportDir)
            # 测试报告路径
            report_file = os.path.join(reportDir, report_name)
            command = 'nosetests -v {0}  --with-html --html-report="{1}"'.format(
                caseFiles, report_file.encode('gbk'))
            # 该方法在调用完shell脚本后，返回一个16位的二进制数，0或1
            result['desc'] = os.system(command)
            # 判断是否自动发送结果邮件
            if config_a['auto_send']:
                result = sendReportMail(report_file)
        except Exception as e:
            result['exception'] = u'用例运行失败：{0}'.format(e)
=======
        # try:
        caseFiles = ' '.join(
            map(lambda i: '"' + i + '"', caseFiles)).encode('gbk')
        config_a = yaml.load(file(CONFIG_FILE_A, 'r'))
        # Taffy路径
        # taffy_dir = config_a['taffy_dir']
        taffy_dir = app.config['UPLOAD_FOLDER'][3:]
        # 测试报告名称
        report_name = config_a['report_name'] + \
            '_{0}.html'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
        # 先判断文件夹是否存在，不存在则新建
        reportDir = os.path.join(taffy_dir, 'Results')
        if not os.path.exists(reportDir):
            os.makedirs(reportDir)
            # 测试报告路径
        report_file = os.path.join(reportDir, report_name)
        command = 'nosetests -v {0}  --with-html-output --html-out-file="{1}"'.format(
            caseFiles, report_file.encode('gbk'))
        # 该方法在调用完shell脚本后，返回一个16位的二进制数，0或1
        result['desc'] = os.system(command)
        # 判断是否自动发送结果邮件
        #     if config_a['auto_send']:
        #         result = sendReportMail(CONFIG_FILE_A,report_file)
        # except Exception as e:
        #     result['exception'] = u'用例运行失败：{0}'.format(e)
>>>>>>> the lastst version on 2018/05
        return jsonify(result)


@app.route("/runCaseA", methods=["GET", "POST"])
def runCaseA():
    if request.method == "POST":
        # 获取数组参数
        caseFiles = request.form.getlist("caseFiles[]")
        result = {}
<<<<<<< HEAD
        try:
            caseFiles = ' '.join(
                map(lambda i: '"' + i + '"', caseFiles)).encode('gbk')
            config_a = yaml.load(file(CONFIG_FILE_AA, 'r'))
            # Taffy路径
            taffy_dir = config_a['taffy_dir_A']
            # 测试报告名称
            report_name = config_a['report_name_A'] + \
                '_{0}.html'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
            # 先判断文件夹是否存在，不存在则新建
            reportDir = os.path.join(taffy_dir, 'Results1')
            if not os.path.exists(reportDir):
                os.makedirs(reportDir)
            # 测试报告路径
            report_file = os.path.join(reportDir, report_name)
            command = 'nosetests -v {0}  --with-html --html-report="{1}"'.format(
                caseFiles, report_file.encode('gbk'))
            # 该方法在调用完shell脚本后，返回一个16位的二进制数，0或1
            result['desc'] = os.system(command)

            # 判断是否自动发送结果邮件
            if config_a['auto_send_A']:
                result = sendReportMail(report_file)
        except Exception as e:
            result['exception'] = u'用例运行失败：{0}'.format(e)
=======
        # try:
        caseFiles = ' '.join(
            map(lambda i: '"' + i + '"', caseFiles)).encode('gbk')
        config_a = yaml.load(file(CONFIG_FILE_AA, 'r'))
        # Taffy路径
        taffy_dir = config_a['taffy_dir_A']
        # 测试报告名称
        report_name = config_a['report_name_A'] + \
            '_{0}.html'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
        # 先判断文件夹是否存在，不存在则新建
        reportDir = os.path.join(taffy_dir, 'Results1')
        if not os.path.exists(reportDir):
            os.makedirs(reportDir)
        # 测试报告路径
            report_file = os.path.join(reportDir, report_name)
            command = 'nosetests -v {0}  --with-html --html-report="{1}"'.format(
                caseFiles, report_file.encode('gbk'))
        # 该方法在调用完shell脚本后，返回一个16位的二进制数，0或1
            result['desc'] = os.system(command)

            # 判断是否自动发送结果邮件
        #     if config_a['auto_send_A']:
        #         result = sendReportMail(report_file)
        # except Exception as e:
        #     result['exception'] = u'用例运行失败：{0}'.format(e)
>>>>>>> the lastst version on 2018/05
        return jsonify(result)


@app.route("/runCaseAA", methods=["GET", "POST"])
def runCaseAA():
    if request.method == "POST":
        # 获取数组参数
        caseFiles = request.form.getlist("caseFiles[]")
        vuser = request.form.get("vuser")
        v_perSec = request.form.get("vuserPerSec")
        runtime = request.form.get("runTime")
        result = {}
        try:
            caseFiles = ' '.join(
                map(lambda i: '"' + i + '"', caseFiles)).encode('gbk')
            config_a = yaml.load(file(CONFIG_FILE_AAA, 'r'))
            # Taffy路径
            taffy_dir = config_a['taffy_dir_AA']
            # 测试报告名称
            # report_name = config_a['report_name_AA'] + \
            #     '_{0}.csv'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
            # 先判断文件夹是否存在，不存在则新建
<<<<<<< HEAD
            reportDir = taffy_dir+'\Results\\'+'_{0}'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
=======
            reportDir_base = taffy_dir + 'Results'
            reportDir = reportDir_base + '\\' + \
                '_{0}'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
>>>>>>> the lastst version on 2018/05
            # if not os.path.exists(reportDir):
            #     os.makedirs(reportDir)
            # 测试报告路径
            # report_file = os.path.join(reportDir, '_requests.csv')
<<<<<<< HEAD
=======
            # print reportDir_base
>>>>>>> the lastst version on 2018/05
            command = 'locust -f {0}  --no-web --csv="{1}" -c {2} -r {3} -t{4}s'.format(
                caseFiles, reportDir.encode('gbk'), vuser, v_perSec, runtime)
            # 该方法在调用完shell脚本后，返回一个16位的二进制数，0或1
            result['desc'] = os.system(command)
<<<<<<< HEAD
            report_file = reportDir+"/"+ "_requests.csv"

=======
            report_file = reportDir + "/" + "_requests.csv"

            syst_Name = platform.system()
            if syst_Name == 'Windows':
                winCopy_cmd = 'xcopy ' + reportDir_base + ' app\static\csv\\'
                print winCopy_cmd
                os.system(winCopy_cmd)
            else:
                linuxCopy_cmd = 'cp ' + reportDir_base + ' app\static\csv\\'
                print linuxCopy_cmd
                os.system(winCopy_cmd)
>>>>>>> the lastst version on 2018/05
            # 判断是否自动发送结果邮件
            if config_a['auto_send_AA']:
                result = sendReportMail(report_file)
        except Exception as e:
            result['exception'] = u'用例运行失败：{0}'.format(e)
        return jsonify(result)


@app.route("/runCaseAAA", methods=["GET", "POST"])
def runCaseAAA():
    if request.method == "POST":
        # 获取数组参数
        caseFiles = request.form.getlist("caseFiles[]")
        result = {}
        try:
            caseFiles = ' '.join(
                map(lambda i: '"' + i + '"', caseFiles)).encode('gbk')
            config_a = yaml.load(file(CONFIG_FILE_AAAA, 'r'))
            # Taffy路径
            taffy_dir = config_a['taffy_dir_BB']
            # 测试报告名称
            report_name = config_a['report_name_BB'] + \
                '_{0}.html'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
            # 先判断文件夹是否存在，不存在则新建
            reportDir = os.path.join(taffy_dir, 'Results3')
            if not os.path.exists(reportDir):
                os.makedirs(reportDir)
            # 测试报告路径
            report_file = os.path.join(reportDir, report_name)
            command = 'nosetests -v {0}  --with-html --html-report="{1}"'.format(
                caseFiles, report_file.encode('gbk'))
            # 该方法在调用完shell脚本后，返回一个16位的二进制数，0或1
            result['desc'] = os.system(command)

            # 判断是否自动发送结果邮件
            if config['auto_send_BB']:
                result = sendReportMail(report_file)
        except Exception as e:
            result['exception'] = u'用例运行失败：{0}'.format(e)
        return jsonify(result)


@app.route("/getReport_A", methods=["GET", "POST"])
def getReport_A():
    if request.method == "GET":
        result = {}
        config = yaml.load(file(CONFIG_FILE_A, 'r'))
        # Taffy路径
<<<<<<< HEAD
        taffy_dir = config['taffy_dir']
=======
        # taffy_dir = config['taffy_dir']
        taffy_dir = app.config['UPLOAD_FOLDER'][3:]
>>>>>>> the lastst version on 2018/05
        # 测试报告名称
        report_name = config['report_name']
        result['report_paths'] = glob.glob(
            taffy_dir + '/**/{0}_*.html'.format(report_name))
        # 测试报告按时间排序 降序排列
        result['report_paths'].sort(reverse=True)
        return jsonify(result)


@app.route("/getReport_AA", methods=["GET", "POST"])
def getReport_AA():
    if request.method == "GET":
        result = {}
        config = yaml.load(file(CONFIG_FILE_AA, 'r'))
        # Taffy路径
        taffy_dir_A = config['taffy_dir_A']
        # 测试报告名称
        report_name_A = config['report_name_A']
        result['report_paths'] = glob.glob(
            taffy_dir_A + '/**/{0}_*.html'.format(report_name_A))
        # 测试报告按时间排序 降序排列
        result['report_paths'].sort(reverse=True)
        return jsonify(result)


@app.route("/getReport_AAA", methods=["GET", "POST"])
def getReport_AAA():
    if request.method == "GET":
        result = {}
        config = yaml.load(file(CONFIG_FILE_AAA, 'r'))
        # Taffy路径
        taffy_dir_AA = config['taffy_dir_AA']
        # 测试报告名称
        result['report_paths'] = glob.glob(taffy_dir_AA + '/**/*.csv')
        # 测试报告按时间排序 降序排列
        result['report_paths'].sort(reverse=True)
        return jsonify(result)


@app.route("/getReport_AAAA", methods=["GET", "POST"])
def getReport_AAAA():
    if request.method == "GET":
        result = {}
        config = yaml.load(file(CONFIG_FILE_AAAA, 'r'))
        # Taffy路径
        taffy_dir_BB = config['taffy_dir_BB']
        # 测试报告名称
        report_name_BB = config['report_name_BB']
        result['report_paths'] = glob.glob(
            taffy_dir_BB + '/**/{0}_*.html'.format(report_name_BB))
        # 测试报告按时间排序 降序排列
        result['report_paths'].sort(reverse=True)
        return jsonify(result)


@app.route("/sendMail_A", methods=["GET", "POST"])
<<<<<<< HEAD
def sendMail_A():
    if request.method == "GET":
        report_file = request.args.get("reportName")
        return jsonify(sendReportMail(CONFIG_FILE_A, report_file))
=======
@csrf.exempt
def sendMail_A():
    if request.method == "POST":
        report_file = request.form.getlist("reportName[]")
        print report_file
        return jsonify(sendReportMail(report_file, CONFIG_FILE_A))
>>>>>>> the lastst version on 2018/05


@app.route("/sendMail_AA", methods=["GET", "POST"])
def sendMail_AA():
    if request.method == "GET":
        report_file = request.args.get("reportName")
        return jsonify(sendReportMail(CONFIG_FILE_AA, report_file))


@app.route("/sendMail_AAA", methods=["GET", "POST"])
def sendMail_AAA():
    if request.method == "GET":
        report_file = request.args.get("reportName")
        return jsonify(sendReportMail(CONFIG_FILE_AAA, report_file))


@app.route("/sendMail_AAAA", methods=["GET", "POST"])
def sendMail_AAAA():
    if request.method == "GET":
        report_file = request.args.get("reportName")
        return jsonify(sendReportMail(CONFIG_FILE_AAAA, report_file))


def switchCase_tool(conf_file):
<<<<<<< HEAD
    config = yaml.load(file(conf_file, 'r'))
    return {
        'CONFIG_FILE_A': {
            'mail_host': config['mail_host'],
            'mail_post': config['mail_post'],
            'mail_user': config['mail_user'],
            'mail_pwd': config['mail_pwd'],
            'mail_subject': config['mail_subject'],
            'mail_to': config['mail_to']
        },
        'CONFIG_FILE_AA': {
            'mail_host': config['mail_host_A'],
            'mail_post': config['mail_post_A'],
            'mail_user': config['mail_user_A'],
            'mail_pwd': config['mail_pwd_A'],
            'mail_subject': config['mail_subject_A'],
            'mail_to': config['mail_to_A']
        },
        'CONFIG_FILE_AAA': {
            'mail_host': config['mail_host_AA'],
            'mail_post': config['mail_post_AA'],
            'mail_user': config['mail_user_AA'],
            'mail_pwd': config['mail_pwd_AA'],
            'mail_subject': config['mail_subject_AA'],
            'mail_to': config['mail_to_AA']
        },
        'CONFIG_FILE_AAAA': {
            'mail_host': config['mail_host_BB'],
            'mail_post': config['mail_post_BB'],
            'mail_user': config['mail_user_BB'],
            'mail_pwd': config['mail_pwd_BB'],
            'mail_subject': config['mail_subject_BB'],
            'mail_to': config['mail_to_BB']
        },
    }


def sendReportMail(report_file, conf_file):

    report_name = report_file.split('\\')[-1]
=======
    print conf_file
    config = yaml.load(file(conf_file, 'r'))
    if conf_file == CONFIG_FILE_A:
        return {
            'config_a.yml': {
                'mail_host': config['mail_host'],
                'mail_port': config['mail_port'],
                'mail_user': config['mail_user'],
                'mail_pwd': config['mail_pwd'],
                'mail_subject': config['mail_subject'],
                'mail_to': config['mail_to']
            }
        }
    elif conf_file == CONFIG_FILE_AA:
        return {
            'config_aa.yml': {
                'mail_host': config['mail_host_A'],
                'mail_port': config['mail_port_A'],
                'mail_user': config['mail_user_A'],
                'mail_pwd': config['mail_pwd_A'],
                'mail_subject': config['mail_subject_A'],
                'mail_to': config['mail_to_A']
            }
        }
    elif conf_file == CONFIG_FILE_AAA:
        return {
            'config_aaa.yml': {
                'mail_host': config['mail_host_AA'],
                'mail_port': config['mail_port_AA'],
                'mail_user': config['mail_user_AA'],
                'mail_pwd': config['mail_pwd_AA'],
                'mail_subject': config['mail_subject_AA'],
                'mail_to': config['mail_to_AA']
            }
        }
    else:
        return {
            'config_aaaa.yml': {
                'mail_host': config['mail_host_BB'],
                'mail_port': config['mail_port_BB'],
                'mail_user': config['mail_user_BB'],
                'mail_pwd': config['mail_pwd_BB'],
                'mail_subject': config['mail_subject_BB'],
                'mail_to': config['mail_to_BB']
            }
        }


def sendReportMail(report_files, conf_file):
    print report_files, conf_file
    report_name_list = []
    for i in range(len(report_files)):
        report_name = report_files[i].split('\\')[-1]
        report_name_list.append(report_name)
    print report_name_list
>>>>>>> the lastst version on 2018/05
    result = {}
    return_conf = switchCase_tool(conf_file)
    # 邮件服务器
    mail_host = return_conf[conf_file]['mail_host']
    # 邮件服务器端口
    mail_port = return_conf[conf_file]['mail_port']
    # 发件人地址
    mail_user = return_conf[conf_file]['mail_user']
    # 发件人密码
    mail_pwd = return_conf[conf_file]['mail_pwd']
    # 邮件标题
<<<<<<< HEAD
    mail_subject = return_conf[conf_file]['mail_pwd'] + \
        '_{0}'.format('_'.join(report_name.strip('.html').split('_')[-2:]))
=======
    mail_subject = return_conf[conf_file]['mail_subject'] + \
        '_{0}'.format(
            '_'.join(report_name_list[0].strip('.html').split('_')[-2:]))
>>>>>>> the lastst version on 2018/05
    # 收件人地址list
    mail_to = return_conf[conf_file]['mail_to']

    # 判断报告文件是否存在
<<<<<<< HEAD
    if not os.path.exists(report_file):
        return jsonify(dict(desc=u'测试报告文件不存在：{0}，<strong>先运行一次测试吧！</strong>'.format(report_file)))
    try:
        # 读取测试报告内容
        with open(report_file, 'r') as f:
            content = f.read().decode('utf-8')

        msg = MIMEMultipart('mixed')
        # 添加邮件内容
        msg_html = MIMEText(content, 'html', 'utf-8')
        msg.attach(msg_html)

        # 添加附件
        msg_attachment = MIMEText(content, 'html', 'utf-8')
        msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(
            report_name)
        msg.attach(msg_attachment)

=======
    if len(report_files) == 0:
        # if not os.path.exists(report_file):
        return jsonify(dict(desc=u'测试报告文件不存在：{0}，<strong>先运行一次测试吧！</strong>'.format(report_files)))
    else:
        content_l = []
        for i in range(len(report_files)):
            # 读取测试报告内容
            print str(report_files[i])
            with open(str(report_files[i]), 'r') as f:
                content = f.read().decode('utf-8')
            content_l.append(content)

        content_lists = ''.join(content_l)
        msg = MIMEMultipart('mixed')
        # 添加邮件内容
        msg_html = MIMEText(
            content_lists, _subtype='html', _charset='utf-8')
        msg.attach(msg_html)
>>>>>>> the lastst version on 2018/05
        msg['Subject'] = mail_subject
        msg['From'] = mail_user
        msg['To'] = mail_to

<<<<<<< HEAD
=======
        # # 添加附件
        msg_attachment = MIMEText(content_lists, 'html', 'utf-8')
        msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(
            report_name_list[i])
        msg_attachment["Content-Type"] = 'application/octet-stream'
        msg.attach(msg_attachment)

    try:
>>>>>>> the lastst version on 2018/05
        # 连接邮件服务器
        s = smtplib.SMTP()
        s.connect(mail_host, mail_port)
        # 登陆
        s.login(mail_user, mail_pwd)
        # 发送邮件
        s.sendmail(mail_user, mail_to, msg.as_string())
        # 退出
        s.quit()
        result['desc'] = u'测试报告发送成功'

    except Exception as e:
        result['desc'] = u'测试报告发送失败：{0}'.format(e)

    return result
<<<<<<< HEAD
=======


@app.route("/updateData", methods=["GET", "POST"])
@csrf.exempt
def updateData():
    if request.method == "GET":
        result = {}
        updateCommon = "svn update upload/dingdang_auto/Common/"
        desc_com = os.system(updateCommon)
        updateConfig = "svn update upload/dingdang_auto/Config/"
        desc_conf = os.system(updateConfig)
        updateTools = "svn update upload/dingdang_auto/Tools/"
        desc_tool = os.system(updateTools)
        if desc_com == 0 and desc_conf == 0 and desc_tool == 0:
            result['desc'] = 0
        else:
            result['desc'] = 1
        return jsonify(result)
# def upload(local_dir, remote_dir):
#     try:
#         # 实例化一个transport对象
#         t = paramiko.Transport((REMOTE_HOST, PORT))
#         # 建立连接
#         t.connect(username=USERNAME, password=PASSWORD)
#         # 将sshclient的对象的transport指定为以上的t
#         sftp = paramiko.SFTPClient.from_transport(t)
#         print('upload file start %s ' % dt.now())
#         for root, dirs, files in os.walk(local_dir):
#             print '[%s][%s][%s]' % (root, dirs, files)
#             for filespath in files:
#                 local_file = os.path.join(root, filespath)
#                 print 11, '[%s][%s][%s][%s]' % (root, filespath, local_file, local_dir)
#                 a = local_file.replace(local_dir, '').replace(
#                     '\\', '/').lstrip('/')
#                 print('01', a, '[%s]' % remote_dir)
#                 remote_file = os.path.join(remote_dir, a)
#                 print 22, remote_file
#                 try:
#                     sftp.put(local_file, remote_file)
#                 except Exception as e:
#                     sftp.mkdir(os.path.split(remote_file)[0])
#                     sftp.put(local_file, remote_file)
#                     print "66 upload %s to remote %s" % (local_file, remote_file)
#             for name in dirs:
#                 local_path = os.path.join(root, name)
#                 print 0, local_path, local_dir
#                 a = local_path.replace(local_dir, '').replace('\\', '')
#                 print 1, a
#                 print 1, remote_dir
#                 remote_path = os.path.join(remote_dir, a)
#                 print 33, remote_path
#                 try:
#                     sftp.mkdir(remote_path)
#                     print 44, "mkdir path %s" % remote_path
#                 except Exception as e:
#                     print 55, e
#         print '77,upload file success %s ' % dt.now()
#         t.close()
#     except Exception as e:
#         print 88, e

# @app.route("/upload", methods=["GET", "POST"])
# @csrf.exempt
# def uploadFille():
#     if request.method == "POST":
#         local_dir = request.files['file']
#         print local_dir
#         return jsonify(upload(local_dir, REMOTE_DIR))
>>>>>>> the lastst version on 2018/05
