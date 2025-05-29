# SaveManagerServer

提供基础的存档位置信息更新服务和存档下载业务

- `/` 查看所有的路径
- `/config/hash` 获取配置的哈希值
- `/config/latest` 获取最新的配置
- `/game` 获取游戏列表
- `/game/<name>` 获取特定游戏的存档

## 配置文件

所有的配置都应该卸载 `config.json` 文件内

```json
{
    "saves": {
        "domain": "https://bili33.top",
        "path": {
            "赛博朋克2077": "%USERPROFILE%\\Saved Games\\CD Projekt Red\\Cyberpunk 2077",
            "黑神话：悟空": "%SteamApps%\\common\\BlackMythWukong\\b1\\Saved",
            "测试游戏1": "%USERPROFILE%\\Saved Games\\TestGame1",
            "测试游戏2": "%USERPROFILE%\\Saved Games\\TestGame2"
        }
    }
}
```

- `saves.domain` 表示下载存档文件的链接
- `saves.path.<game>` 表示某个游戏的存档位置，`<game>` 必须为游戏名，并且此游戏名应该与下载时的文件名相匹配

## 关于变量

`%USERNAME%` 在 Windows 中指的是当前登录的用户的用户名

`%AppData%` 指的是 `C:\Users\%USERNAME%\AppData\Roaming` 这个文件夹

`%SteamApps` 指的是 Steam 的游戏安装文件夹，需要注意的是游戏库可以分布在多个盘符（Steam 自身的机制）

`%USERPROFILE` 指的是 `C:\Users\%USERNAME` 这个文件夹
