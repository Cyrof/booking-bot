import requests

cookies = {
    '_ga': 'GA1.3.690329940.1657379803',
    '_gid': 'GA1.3.1097692139.1657379803',
    'ASP.NET_SessionId': 'orzjbp3dyy3smr3rmiv0qsfo',
    'cf_clearance': 'LuuQMJpqUUIhCoWxgYgtWoUc6n2itaKG6j4LGvIThng-1657472188-0-250',
    '_gat_gtag_UA_138358328_1': '1',
}

headers = {
    'authority': 'bookingportal.cdc.com.sg:8443',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.3.690329940.1657379803; _gid=GA1.3.1097692139.1657379803; ASP.NET_SessionId=orzjbp3dyy3smr3rmiv0qsfo; cf_clearance=LuuQMJpqUUIhCoWxgYgtWoUc6n2itaKG6j4LGvIThng-1657472188-0-250; _gat_gtag_UA_138358328_1=1',
    'pragma': 'no-cache',
    'referer': 'https://bookingportal.cdc.com.sg:8443/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'd': 'x0GsKVdHWjEGCtrDczovS75GaKq1IfD3X0xBMTVSaYQDlT3PUoDBoIuZBIn7DeSK82wY6FPqfkXsM79f_LCbobYPzPVtQpK7-wBXobXmDr9mCTVW0',
    't': '637812244157966200',
}

response = requests.get('https://bookingportal.cdc.com.sg:8443/NewPortal/WebResource.axd', params=params, cookies=cookies, headers=headers)
print(response.url)