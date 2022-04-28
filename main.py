from typing import Optional
from weakref import proxy
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import GetPixDetail

app = FastAPI()


@app.get("/")
def default():
    '默认配置，不输入任何数值就会跳转到文档'
    return RedirectResponse("/docs")


@app.get("/{pid}")
def ImgGet(pid: int = None, p: int = 0):
    '输入图片的id，返回代理站代理后的图片链接，可指定第几张'
    if pid:
        ImgUrl = GetPixDetail.GetPixDetail(pid)["urls"]["original"]
        ProxyUrl = "pximg.knight000.top"
        # 替换pximg为代理站
        ImgUrl = ImgUrl.replace("i.pximg.net", ProxyUrl)
        # 如果输入p0以外的数值则把链接替换为p的数值
        if p != 0:
            ImgUrl = ImgUrl.replace("_p0", f"_p{p}")
        return RedirectResponse(ImgUrl)
    else:
        return RedirectResponse("/docs")


@app.get("/api/{pid}")
def ImgApi(pid: int = None):
    'API方式的请求，返回JSON'
    return GetPixDetail.GetPixDetail(pid)
