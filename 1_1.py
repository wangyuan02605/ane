# TODO （1）导入所需python工具库,并将代码截图存放至“赛位号_答题文档1-1.docx”中。
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models
import base64
#要背
# TODO （2）通过账户密钥SecretId 和 SecretKey实例化一个认证对象，并把代码截图存放至“赛位号_答题文档1-1.docx”中。
cred = credential.Credential("AKID6GNVcbP2QZTEQWTBm9at464zmSzNbgkd", "JUSAhquqeP8pLl9SceSCnMvS4jFZtBOP")

# TODO （3）实例化语音识别所用接口的http选项及一个客户端对象，并把代码截图存放至“赛位号_答题文档1-1.docx”中。
httpProfile = HttpProfile()
httpProfile.endpoint = "asr.tencentcloudapi.com"

# 实例化一个client选项，可选的，没有特殊需求可以跳过
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
# 实例化要请求产品的client对象,clientProfile是可选的
client = asr_client.AsrClient(cred, "ap-beijing", clientProfile)
file_path="/home/tione/notebook/任务一/语音识别/音频文件/音频6.mp3"
# TODO （4）将所提供的音频素材转换为base64编码规范输出，并把代码截图存放至“赛位号_答题文档1-1.docx”中。
def ToBase64(file):
    with open(file_path,"rb") as f:
        byte_=f.read()
    return base64.b64encode(byte_).decode('utf-8')
voice = ToBase64(file_path)
#要背
# TODO （5）根据提供的接口文档设置语音识别接口的请求参数’params’，要求以语音数据base64形式对中文mp3类型且不过滤语气词和标点符号的音频文件进行配置，并把代码截图存放至“赛位号_答题文档1-1.docx”中。
params = {
    "EngSerViceType":"16k_zh",
    "SourceType":1,
    "VoiceFormat":"mp3",
    "Data":voice,
    "FilterDirty":0,
    "FilterModal":0,
    "FilterPunc":0

}
# TODO （6）将请求参数转换为json格式向客户端发送请求，在控制台输出语音识别结果，并把代码截图存放至“赛位号_答题文档1-1.docx”中。
req = models.SentenceRecognitionRequest()
req.from_json_string(json.dumps(params))
resp = client.SentenceRecognition(req)
resp.to_json_string()
#背一下
