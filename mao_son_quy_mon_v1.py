import os
import requests

from lxml import html
from tqdm import tqdm
from time import sleep

PAGES_TO_SAVE = 10
FROM_CHAPTER = 1
TO_CHAPTER = 1601
ALL_CHAPTER = 1601
SAVE_DIR = "data/mao_son_quy_mon_thuat_tangthuvien/"

to_save = ""
chapters_in_save = []

# create save dir if not exists
os.makedirs(SAVE_DIR, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def process_content(content):
    content = content.split("\n")
    filtered_content = []
    for i, c in enumerate(content):
        if i < 5:
            if "converter" in c.lower():
                continue
            elif "Chương" in c:
                continue
            elif "Cập nhật lúc" in c:
                continue
        if "HȯṪȓuyëŋ.cøm" in c:
            continue
        elif "hotruyen" in c:
            continue
        elif c.strip() == "":
            continue
        c = c.strip()
        c = c.replace("\r\n\r\n", "\n")
        c = c.replace("\t", "")
        filtered_content.append(c)
    filtered_content = "\n".join(filtered_content)
    # filtered_content = filtered_content.replace("\n\n", "\n")
    return filtered_content


next_link = "https://hotruyen.com/chuong/mao-son-quy-thuat-su-chuong-1-31303539352D382D312D37313238302D30"
chapter_number = FROM_CHAPTER
while chapter_number <= TO_CHAPTER:
    print(chapter_number)
    chapters_in_save.append(chapter_number)
    page = requests.get(next_link, headers=headers)
    tree = html.fromstring(page.content)
    try:
        title = tree.xpath("string(/html/body/div[5]/div[1]/div/h2)").strip()
        normalized_title = title.replace("\xa0", " ")
    except:
        print(f"chapter {chapter_number} issue")
        title = "Chương {chapter_number}"

    # extract link
    try:
        extracted_link = tree.xpath('//*[@id="chcontent"]/div[4]/a[2]/@href')[0]
    except Exception as e:
        print(chapter_number, e)
        sleep(30)
        continue
    if "javascript" in extracted_link:
        extracted_link = tree.xpath('//*[@id="chcontent"]/div[4]/a[3]/@href')[0]
    next_link = f"https://hotruyen.com{extracted_link}"

    content = tree.xpath('string(//*[@id="borderchapter"])')
    content = process_content(content)
    chapter_content = title + "\n\n" + content + "\n\n\n"
    to_save = to_save + chapter_content
    to_save = to_save.strip()
    if len(to_save) < 2000:
        print(f"oh shit! {chapter_number}")

    if chapter_number % PAGES_TO_SAVE == 0 or chapter_number == TO_CHAPTER:
        with open(
            f"{SAVE_DIR}/msqmt_{min(chapters_in_save)}-{max(chapters_in_save)}.txt", "w"
        ) as f:
            f.write(to_save)
        to_save = ""
        chapters_in_save = []

    # break
    chapter_number += 1
    sleep(5)
