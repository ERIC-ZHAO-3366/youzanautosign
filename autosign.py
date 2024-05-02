import http.client
import requests
import json

webhook_url = 'https://connector.dingtalk.com/webhook/flow/1029cb9359610b523850000j'
conn = http.client.HTTPSConnection('shop40557752.youzan.com')
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'KDTSESSIONID=YZ1228395045475844096YZcqrAJh3y; nobody_sign=YZ1228395045475844096YZcqrAJh3y; yz_log_ftime=1712913801337; yz_log_uuid=2ec11377-0aa0-6f2d-7612-ef8029df1ae6; ec=NxmPwCW1-1712913808124-88217012146ad1508222767; _kdt_id_=40365584; rdfp=249b5546289942c1445c6dd8d418927d; yz_fp_hash=35b7143f13e6deeeb48884314cce7c68; _efmdata=FHo3SUGP%2BOXhB4O6AxVjtBGvrqNlg50AlLKF%2F5k6pgsU%2B892ptNBOF4RKVbGYmcWnzAGAAXd2Lev0RQX0BPxqe1nbtWcFs4OUvXa6LZK4HI%3D; _exid=J47nfj%2F5gtHVuWb9MCU5SYDggAUikQu%2FNvEJVO4KFs3VWdE4Dw6Y4IXCTA0Zhr9aLB4oCK3mDqun4%2BHPdHFZjQ%3D%3D; trace_sdk_context_slg=tagGoodList-default,OpBottom,8486567078,abTraceId; dfp=249b5546289942c1445c6dd8d418927d; loc_dfp=87c725b602192f0d6d161b6985cf0f88; trace_sdk_context_banner_id=f.89403162~cube.8~9~hvkw0lKD; yz_log_seqb=1713628476333; acw_tc=b68f6bbd381c78d1704c0bbb801f38ab675ba0cc1c56c840d2738049d110052f; yz_log_seqn=30',
    'referer': 'https://shop40557752.youzan.com/wscump/checkin/result?kdt_id=40365584',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/123.0.0.0',
    'x-yz-action-id': 'wsc-h5-ump-0a37de1a-1711987203939-714513',
}
conn.request(
    'GET',
    'https://h5.youzan.com/wscump/checkin/checkinV2.json?checkinId=20761&app_id=wx83e2dea9331b402b&kdt_id=40365584&access_token=380c14dfc4008bf8e15c65b317b17d',
    headers=headers
)
response = conn.getresponse()
print(f"Response status: {response.status}")  # 打印响应状态码

response_content = response.read().decode('utf-8')  # decode the response content
print(f"Response content: {response_content}")  # 打印响应内容

# 发送POST请求到Webhook URL
response = requests.post(webhook_url, json=response)

# 打印响应状态码和内容
print(f"Webhook Response Status: {response.status_code}")
print(f"Webhook Response Content: {response.content}")