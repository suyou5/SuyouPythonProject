"""
腾讯云试唇色api
"""
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.fmu.v20191213 import fmu_client, models
try:
    cred = credential.Credential("AKIDUnumQrbAyZx9C1A4HEqENHwNjtukGipi", "shGcmiPq79z0hCScv63D7tUp484rz4ML")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "fmu.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = fmu_client.FmuClient(cred, "ap-guangzhou", clientProfile)

    req = models.TryLipstickPicRequest()
    params = {
        "LipColorInfos": [
            {
                "RGBA": {
                    "R": 255,
                    "G": 117,
                    "B": 0,
                    "A": 0
                },
                "ModelAlpha": 50
            }
        ],
        "Url": 'http://gchat.qpic.cn/gchatpic_new/467162434/3979142650-2854117514-C813E8C8F7B1D83C9F75C276DC7B0672/0?term=2',
        "RspImgType": "url"
    }
    req.from_json_string(json.dumps(params))

    resp = client.TryLipstickPic(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
