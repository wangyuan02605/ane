# TODO （1）导入所需python工具库,并将代码截图存放至“赛位号_答题文档1-2.docx”中。

import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tts.v20190823 import tts_client, models
import base64
import uuid
# TODO （2）通过账户密钥SecretId 和 SecretKey实例化一个认证对象，并把代码截图存放至“赛位号_答题文档1-2.docx”中。

cred = credential.Credential("AKID6GNVcbP2QZTEQWTBm9at464zmSzNbgkd", "JUSAhquqeP8pLl9SceSCnMvS4jFZtBOP")

# TODO （3）实例化语音合成所用接口的http选项及一个客户端对象,并把代码截图存放至“赛位号_答题文档1-2.docx”中。
httpProfile = HttpProfile()
httpProfile.endpoint = "tts.tencentcloudapi.com"

# 实例化一个client选项，可选的，没有特殊需求可以跳过
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
# 实例化要请求产品的client对象,clientProfile是可选的
client = tts_client.TtsClient(cred, "ap-beijing", clientProfile)
# TODO （4）生成标识用户唯一身份的会话号sessionId，并把代码截图存放至“赛位号_答题文档1-2.docx”中。
sessionId =str(uuid.uuid1())
# TODO （5）根据提供的接口文档和会话号，配置语音合成的请求参数’params’，要求将文本“欢迎使用智能医院服务”合成为中文“智云”音色其中合成音频的音量为5，并把代码截图存放至“赛位号_答题文档1-2.docx”中。
params = {
    "Text":"欢迎使用智能医院服务",
    "SessionId":sessionId,
    "Volume":5,
    "ModelType":1,
    "VoiceType":1004,
    "Codec":"mp3"

}
# TODO （6）将请求参数转换为json格式向客户端发送请求，打印响应的字符串包，把代码截图存放至“赛位号_答题文档1-2.docx”中。
req = models.TextToVoiceRequest()
req.from_json_string(json.dumps(params))
resp = client.TextToVoice(req)
base64_data=resp
# TODO （7）将字符串包解析成音频文件，命名为“赛位号_语音合成结果.mp3”，并把代码截图存放至“赛位号_答题文档1-2.docx”中。
def ToFile(base64_data, file):
    with open(file,"wb") as f:
        f.write(base64.b64decode(base64_data.Audio))
#要背 对于base64转mp3 是decode
ToFile(base64_data=base64_data,file="2.mp3")