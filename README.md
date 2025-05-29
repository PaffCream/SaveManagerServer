# SaveManagerServer

提供基础的存档位置信息更新服务和存档下载业务

- `/` 查看所有的路径
- `/config/hash` 获取配置的哈希值
- `/config/latest` 获取最新的配置
- `/game` 获取游戏列表
- `/game/<name>` 获取特定游戏的存档

## 关于变量

`%USERNAME%` 在 Windows 中指的是当前登录的用户的用户名
`%AppData%` 指的是 `C:\Users\%USERNAME%\AppData\Roaming` 这个文件夹
`%SteamApps` 指的是 Steam 的游戏安装文件夹，需要注意的是游戏库可以分布在多个盘符（Steam 自身的机制）