import httpx

# 批量下载图片
base_url = "https://raw.githubusercontent.com/Orz-3/mini/master/Color/"
logo_name_list = [
    "Microsoft",
    "Apple",
    "OpenAI",
    "Telegram",
    "Cylink",
    "Urltest",
    "Static",
    "HK",
    "JP",
    "KR",
    "TW",
    "US",
    "CN",
    "AU",
    "CA",
    "DE",
    "FR",
]

for logo_name in logo_name_list:
    url = f"{base_url}{logo_name}.png"
    response = httpx.get(url)
    if response.status_code == 200:
        with open(f"color/{logo_name}.png", "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download {logo_name}")
