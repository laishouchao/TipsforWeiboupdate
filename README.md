# TipsforWeiboupdate
读取账户关注的人的微博更新，当更新时发送消息到指定微信群  
**2017年以前注册并登陆过网页版微信的微信号该项目依旧可用**
## 运行效果
![结果预览](https://i.jpg.dog/img/1e7c45edcdc928f11c9dca06e4969ecd.png)
## 安装方式
### 直接安装
> 直接在git bash中执行  
> git clone https://github.com/laishouchao/TipsforWeiboupdate.git  
> cd TipsforWeiboupdate  
> python3 Getnews.py
### docker安装
> 暂无

## 参数说明
* `./sinaweibopy3/UserSinaweibopy3.py:line9,line10`请根据自己的weiboAPI信息更改后运行。运行过程打开浏览器，复制url中的code参数返回控制台输入可获得access_token
* 将access_token替换到GetNews.py中的url参数的相应位置
* 查询时间在main函数中，根据情况自行修改
* 各变量名很乱，见谅