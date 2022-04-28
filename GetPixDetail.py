import requests
import json
from lxml import etree


def GetPixDetail(pid):

    # 爬取meta内容，Xpath提取
    data = etree.HTML(requests.get(
        url=f'https://www.pixiv.net/artworks/{pid}').text)
    # 解析json并选取本作品内容
    data = json.loads(data.xpath(
        '//meta[@id="meta-preload-data"]/@content')[0])["illust"][str(pid)]
    # 输出有用数据
    res = {
        "id": data["id"],
        "urls": data["urls"],
        "tags": data["tags"]["tags"],
        "user": {
            "userId": data["userId"],
            "userName": data["userName"],
            "alt": data["alt"]
        }
    }

    return(res)
