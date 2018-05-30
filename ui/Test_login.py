# coding:utf-8
import autoit
import time


class test_cloudmusic(object):

    # 定义相关参数
    cloudmusic_path = "C:\Program Files (x86)\woyaowokong\ddgj\Starter.exe"
    cloudmusic_title = "[CLASS:pms_ddgj_main]"
    user = "csjd202"
    passwd = "meituanv5"

    def test_search(self):
        # 运行红叮当客户端
        autoit.run(self.cloudmusic_path)
        time.sleep(5)

        # 等待红叮当窗口激活
        autoit.win_wait_active(self.cloudmusic_title)

        # 按1下TAB切换至输入框
        autoit.send("{TAB 1}")

        # 输入用户名
        autoit.send(self.user)
        time.sleep(2)

        # 按1下TAB切换至输入框
        autoit.send("{TAB 1}")

        # 输入密码
        autoit.send(self.passwd)
        time.sleep(2)

        # 按1下TAB切换至输入框
        autoit.send("{TAB 1}")

        # 点击登录
        autoit.send("{ENTER}")
        time.sleep(2)

        # # 校验当前窗口标题是否含有搜索歌曲名
        # title = autoit.win_get_title(self.cloudmusic_title)
        # assert self.song in title, self.song.encode('utf-8') + ' not in ' + title.encode('utf-8')

        # # 关闭窗口
        # autoit.win_close(self.cloudmusic_title)