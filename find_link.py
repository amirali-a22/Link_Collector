import re

import requests

## at the moment this app collect link of originals erial from "mobomovie" site

## you should give your serial site url
r = requests.get('https://mobomovie.space/series/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%D8%B3%D8%B1%DB%8C%D8%A7%D9%84-'
                 'the-originals-%D8%A8%D8%A7-%D8%B2%DB%8C%D8%B1%D9%86%D9%88%DB%8C%D8%B3-%DA%86%D8%B3%D8%A8%DB%8C%D8%AF%'
                 'D9%87-%D9%81%D8%A7%D8%B1%D8%B3/')

## make sure that site has this "div" option
seasons_div = re.findall("<div class=\"heading_links.*</div>", r.text)

link_file = open("links.txt", "w", encoding="UTF-8")


for div in seasons_div:
    quality = re.findall("کیفیت : .{3}", div)
    season = re.findall("فصل : .{2}", div)
    a_tag = re.findall("<a href=\".*?</a>", div)
    link_file.writelines("\n")

    link_file.writelines(season)
    link_file.writelines(quality)
    link_file.writelines("\n")
    link_file.writelines("\n")
    for a in a_tag:
        link_file.writelines(f"{a}\n")

link_file.close()
