import requests
import itchat
import time
import json


class getInfo(object):
    def __init__(self):
        self.url = f"https://api.weibo.com/2/statuses/home_timeline.json?access_token=2.00AICJkHKHfXOC0ca80471b00LcIop&count=1"
        self.headers = {
            "cookie": "Cookie: SINAGLOBAL=4437256218914.105.1579259452117; login_sid_t=1d812c69bc2c6bbd2bf87f05de5330f4; cross_origin_proto=SSL; Ugrow-G0=140ad66ad7317901fc818d7fd7743564; TC-V5-G0=799b73639653e51a6d82fb007f218b2f; _s_tentry=passport.weibo.com; wb_view_log=1920*10801; Apache=150045861391.4657.1581488327664; ULV=1581488328180:2:1:1:150045861391.4657.1581488327664:1579259452857; ALF=1613024337; SSOLoginState=1581488338; SUB=_2A25zR-iCDeRhGeFO4lYW-SrIyjqIHXVQNV1KrDV8PUNbmtANLWzXkW9NQVRWkkB6xC3rYMuF1Khr6nWlgSORPMHZ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWypBWbg6zJc73PgN7FFQAe5JpX5KzhUgL.FoM71KBN1KBXeKq2dJLoIp5LxKqL1-BLBKH0q0-0So.0; SUHB=0la1D27EcGac-S; wvr=6; wb_view_log_7094794416=1920*10801; UOR=xc84.com,widget.weibo.com,www.baidu.com; TC-Page-G0=04dc502e635144031713f186989293c7|1581489979|1581489936; webim_unReadCount=%7B%22time%22%3A1581490107205%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"}

    def Getinfo(self):
        print(self.url)
        response = requests.get(url=self.url, headers=self.headers).text
        # print(response)
        # 将数据保存到json文件中，防止被反扒后没有数据
        with open("./outPut/getinfo.log", "a", encoding="utf-8")as fp:
            fp.write(response)
        return response


class send_massage:
    def __init__(self, qunname, countext):
        itchat.auto_login(enableCmdQR=True, hotReload=True)
        self.gname = qunname
        self.context = countext

    def SendChatRoomsMsg(self):
        # 获取群组所有的相关信息（注意最好群聊保存到通讯录）
        myroom = itchat.get_chatrooms(update=True)
        # 定义全局变量（也可以不定义)
        global username
        #  传入指定群名进行搜索，之所以搜索，是因为群员的名称信息也在里面
        myroom = itchat.search_chatrooms(name=self.gname)
        for room in myroom:
            #  print(room)
            # 遍历所有NickName为键值的信息进行匹配群名
            if room['NickName'] == self.gname:
                username = room['UserName']
                #  得到群名的唯一标识，进行信息发送
                itchat.send_msg(self.context, username)
            else:
                print('No groups found')


if __name__ == '__main__':
    # 循环30分钟查询一次微博更新
    message_old = "null"
    while (1 == 1):
        # 获取动态信息
        getInfoinit = getInfo()
        info = getInfoinit.Getinfo()
        # 调用格式化函数格式化信息
        infoinit = json.loads(info)
        from_name = infoinit["statuses"][0]["user"]["name"]
        from_text = infoinit["statuses"][0]["retweeted_status"]["text"]
        # 查询是否有微博更新
        if from_text == message_old:
            continue
        else:
            message_old = from_text
        send_neirong = from_name + "\n更新微博，内容如下:\n" + from_text
        print(send_neirong)
        # 登录微信
        itchat.auto_login(enableCmdQR=True, hotReload=True)
        # 调用发送微信的函数
        sendsend = send_massage(qunname="B特战小分队", countext=send_neirong)
        sendsend.SendChatRoomsMsg()
        print("发送成功")
        # 保持登录状态
        itchat.run()
        time.sleep(1800)
