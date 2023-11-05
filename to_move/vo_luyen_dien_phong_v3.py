import os
import requests

from lxml import html
from tqdm import tqdm

PAGES_TO_SAVE = 10
FROM_CHAPTER  = 5961
TO_CHAPTER    = 5962
ALL_CHAPTER   = 6009
SAVE_DIR      = 'data/vo_luyen_dien_phong'
to_save = ""
chapters_in_save = []

def process_content(content):
    """
    Filters the given content based on certain conditions.

    Args:
        content (list): The content to be filtered.

    Returns:
        list: The filtered content.

    """
    filtered_content = []
    for i, c in enumerate(content):
        if i < 5:
            if "converter" in c.lower():
                continue
            elif 'Chương' in c:
                continue
            elif 'Cập nhật lúc' in c:
                continue

        filtered_content.append(c)
    return filtered_content

# create save dir if not exists
os.makedirs(SAVE_DIR, exist_ok=True)


# add cookie to requests
jar = requests.cookies.RequestsCookieJar()
jar.set('isAdult', '1', domain='metruyencv.com', path='/')
session = requests.Session()
session.cookies = jar

# get chapters


for chapter_number in tqdm(range(FROM_CHAPTER, TO_CHAPTER+1), initial=FROM_CHAPTER, desc="Chapter", total=ALL_CHAPTER):
    chapters_in_save.append(chapter_number)
    page = requests.get(f'https://metruyencv.com/truyen/vu-luyen-dien-phong/chuong-{chapter_number}')
    tree = html.fromstring(page.content)
    try:
        title   = tree.xpath('string(//*[@id="js-read__body"]/div[2])').strip()
    except:
        print(f'chapter {chapter_number} issue')
        title   = "Chương {chapter_number}"

    content = tree.xpath('//*[@id="article"]/text()')
    content = process_content(content)
    content = '\n'.join(content)
    content = content.strip()
    chapter_content = title + '\n\n' + content + '\n\n\n'
    to_save = chapter_content if to_save == '' else to_save + chapter_content
    if len(to_save) < 2000:
        print(f'oh shit! {chapter_number}')

    if chapter_number % PAGES_TO_SAVE == 0 or chapter_number == TO_CHAPTER:
        with open(f'{SAVE_DIR}/vldp_{min(chapters_in_save)}-{max(chapters_in_save)}.txt','w') as f:
            f.write(to_save)
        to_save = ""
        chapters_in_save = []
