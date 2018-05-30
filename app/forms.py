# coding:utf-8

<<<<<<< HEAD
from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField,DateField
from wtforms.widgets.core import PasswordInput
from wtforms.validators import DataRequired, Email, NumberRange
=======
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField, DateField
from wtforms.widgets.core import PasswordInput
from wtforms.validators import DataRequired, Email, NumberRange
from models import User
>>>>>>> the lastst version on 2018/05


class PasswordField(PasswordField):
    # 修改PasswordInput参数值显示密码
    widget = PasswordInput(hide_value=False)


<<<<<<< HEAD
class configForm_a(Form):
    taffy_dir = StringField(u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send = BooleanField(u"是否自动发送报告邮件")
    mail_host = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port = IntegerField(u"邮件服务器端口", validators=[DataRequired(), NumberRange(0, 65535)])
    mail_user = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to = StringField(u"收件人地址", description=u'多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")

class configForm_aa(Form):
    taffy_dir_A = StringField(u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name_A = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send_A = BooleanField(u"是否自动发送报告邮件")
    mail_host_A = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port_A = IntegerField(u"邮件服务器端口", validators=[DataRequired(), NumberRange(0, 65535)])
    mail_user_A = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd_A = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject_A = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to_A = StringField(u"收件人地址", description=u'多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")

class configForm_aaa(Form):
    taffy_dir_AA = StringField(u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name_AA = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send_AA = BooleanField(u"是否自动发送报告邮件")
    mail_host_AA = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port_AA = IntegerField(u"邮件服务器端口", validators=[DataRequired(), NumberRange(0, 65535)])
    mail_user_AA = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd_AA = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject_AA = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to_AA = StringField(u"收件人地址", description=u'多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")

class configForm_aaaa(Form):
    taffy_dir_BB = StringField(u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name_BB = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send_BB = BooleanField(u"是否自动发送报告邮件")
    mail_host_BB = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port_BB = IntegerField(u"邮件服务器端口", validators=[DataRequired(), NumberRange(0, 65535)])
    mail_user_BB = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd_BB = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject_BB = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to_BB = StringField(u"收件人地址", description=u'多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")
=======
class configForm_a(FlaskForm):
    # taffy_dir = StringField(
    #     u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send = BooleanField(u"是否自动发送报告邮件")
    mail_host = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port = IntegerField(u"邮件服务器端口", validators=[
                             DataRequired(), NumberRange(0, 65535)])
    mail_user = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to = StringField(u"收件人地址", description=u'多个地址请以;分割',
                          validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")


class configForm_aa(FlaskForm):
    taffy_dir_A = StringField(
        u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name_A = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send_A = BooleanField(u"是否自动发送报告邮件")
    mail_host_A = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port_A = IntegerField(u"邮件服务器端口", validators=[
                               DataRequired(), NumberRange(0, 65535)])
    mail_user_A = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd_A = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject_A = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to_A = StringField(
        u"收件人地址", description=u'多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")


class configForm_aaa(FlaskForm):
    taffy_dir_AA = StringField(
        u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name_AA = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send_AA = BooleanField(u"是否自动发送报告邮件")
    mail_host_AA = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port_AA = IntegerField(u"邮件服务器端口", validators=[
                                DataRequired(), NumberRange(0, 65535)])
    mail_user_AA = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd_AA = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject_AA = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to_AA = StringField(
        u"收件人地址", description=u'多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")


class configForm_aaaa(FlaskForm):
    taffy_dir_BB = StringField(
        u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name_BB = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send_BB = BooleanField(u"是否自动发送报告邮件")
    mail_host_BB = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port_BB = IntegerField(u"邮件服务器端口", validators=[
                                DataRequired(), NumberRange(0, 65535)])
    mail_user_BB = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd_BB = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject_BB = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to_BB = StringField(
        u"收件人地址", description=u'多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")


# class NameForm(Form):
    # username = StringField('User Name', validators=[DataRequired(
    #     message=u"用户名不能为空")], render_kw={'placeholder': u'用户名'})
    # password = PasswordField('Password', validators=[DataRequired(
    #     message=u"密码不能为空")], render_kw={'placeholder': u'输入密码'})
    # remember_me = BooleanField('remember me', default=False)
    # submit = SubmitField('Sign in')


class NameForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(
        message=u"用户名不能为空")], render_kw={'placeholder': u'用户名'})
    ###StringField构造函数中的可选参数validators指定一个有验证函数组成的列表，在接受用户提交的数据之前验证数据。
    ###电子邮件字段用到了WTForms提供的Length（）和Email（）验证函数。
    password = PasswordField('Password', validators=[DataRequired(
        message=u"密码不能为空")], render_kw={'placeholder': u'密码'})
    ###PasswordField类表示属性为type="password"的<input>元素。
    remember_me = BooleanField('remember me', default=False)
    ###BooleanField类表示复选框。
    # submit_button = SubmitField(u"登录")


# class UploadForm(FlaskForm):
#     pyfile = FileField(validators=[FileAllowed(
#         upfiles, u'pyfiles'), FileRequired(u'文件未选择！')])
#     submit = SubmitField(u'Upload')
>>>>>>> the lastst version on 2018/05
