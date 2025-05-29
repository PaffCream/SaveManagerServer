# api/index.py
import hashlib
import json
import os
from fastapi import FastAPI, Response, HTTPException, status
from fastapi.responses import RedirectResponse, JSONResponse

app = FastAPI()

# 文件路径配置
config_file_path = "config.json"

# 初始化 GAME_LIST
GAME_LIST = {}  # 初始化为空字典，以防文件读取失败
data = {}  # 存储 JSON 文件内容，用于后续使用

with open(config_file_path, "r", encoding="utf8") as f:
    data = json.load(f)
    DOMAIN = data.get("saves", {}).get("domain", "https://bili33.top")
    GAME_LIST = data.get("saves", {}).get("path").keys()

@app.get("/")
async def index():
    response_data = {
        "code": 200,
        "path": [
            {
                "route": "/config/hash",
                "description": "Get the latest hash of the config file",
            },
            {"route": "/config/latest", "description": "Get the latest config file"},
            {
                "route": "/game/{game_name}",
                "description": "Get the save file of a game",
            },
            {"route": "/game", "description": "Get the list of games"},
        ],
        "repo": "https://github.com/PaffCream/SaveManagerServer",
        "copyright": "Copyright (c) 2025 GamerNoTitle",
    }
    return response_data

@app.get("/config/hash")
async def latest_hash():
    try:
        if not data:
            raise FileNotFoundError("path.json content not loaded")
        file_hash = hashlib.sha256(json.dumps(data.get("saves", {}).get("path", {})).encode()).hexdigest()
        return {"hash": file_hash}
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="path.json not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/config/latest")
async def latest_config():
    try:
        if not data:
            raise FileNotFoundError("path.json content not loaded")
        return data.get("saves", {}).get("path", {})
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="path.json not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/game/{game}")
async def get_save(game: str):
    # 检查 GAME_LIST 是否已成功加载
    if not GAME_LIST or game not in GAME_LIST:
        raise HTTPException(status_code=404, detail="Game not found or game list not loaded")
    try:
        redirect_url = f"{DOMAIN}/saves/{game}.zip"
        return RedirectResponse(url=redirect_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/game")
async def game_list():
    try:
        # 检查 GAME_LIST 是否已成功加载
        if not GAME_LIST:
            raise HTTPException(status_code=500, detail="Game list not loaded")
        games = [game for game in GAME_LIST]
        return {"games": games}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @app.get("/debug")
# async def debug():
#     # 获取当前路径和目录所有文件的信息然后返回，用于调试
#     try:
#         current_path = os.getcwd()
#         files = os.listdir(current_path)
#         return {
#             "current_path": current_path,
#             "files": files,
#             "game_list": list(GAME_LIST),
#             "data": data
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))