import re

import requests

radio_geek_links = open("radio-geek-link.txt", "w", encoding="UTF-8")

radio_geek_links.writelines("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>radio-geek-links</title>
</head>
<body>

    """)
i = 0
while i <= 15:
    r = requests.get(f"https://jadi.net/tag/podcast/page/{i}/")
    links = re.findall("<a href=\"https://jadi.net/audio/jadi-net_radio-geek.*.mp3\">.*</a>", r.text)
    i += 1

    for j in links:
        radio_geek_links.writelines(re.findall("radio.*?.mp3", j))
        radio_geek_links.writelines("\n")
        radio_geek_links.writelines(f"{j}\n")
        radio_geek_links.writelines("</br>")


radio_geek_links.writelines("""
</body>
</html>
""")
# <a href="https://jadi.net/audio/jadi-net_radio-geek_102_wind-of-change.mp3">دانلود نسخه ام پی تری</a>
