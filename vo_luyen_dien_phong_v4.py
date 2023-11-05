import os
import requests

from lxml import html
from tqdm import tqdm

PAGES_TO_SAVE = 10
FROM_CHAPTER  = 5331
TO_CHAPTER    = 6009
ALL_CHAPTER   = 6009
SAVE_DIR      = 'data/vo_luyen_dien_phong_tangthuvien/'

to_save = ""
chapters_in_save = []

# create save dir if not exists
os.makedirs(SAVE_DIR, exist_ok=True)

def process_content(content):
    """
    Filters the given content based on certain conditions.

    Args:
        content (list): The content to be filtered.

    Returns:
        list: The filtered content.

    """
    content = content.split("\n")
    filtered_content = []
    for i, c in enumerate(content):
        if i < 5:
            if "converter" in c.lower():
                continue
            elif 'Chương' in c:
                continue
            elif 'Cập nhật lúc' in c:
                continue
        c = c.strip()
        c = c.replace("\r\n\r\n", "\n")
        c = c.replace("\t", "")
        filtered_content.append(c)
    filtered_content = "\n".join(filtered_content)
    filtered_content = filtered_content.replace("\n\n", "\n")
    return filtered_content


for chapter_number in tqdm(range(FROM_CHAPTER, TO_CHAPTER+1), initial=FROM_CHAPTER, desc="Chapter", total=ALL_CHAPTER):
    chapters_in_save.append(chapter_number)
    page = requests.get(f'https://truyen.tangthuvien.vn/doc-truyen/vu-luyen-dien-phong/chuong-{chapter_number}')
    tree = html.fromstring(page.content)
    try:
        title   = tree.xpath('string(/html/body/div[5]/div[1]/div/h2)').strip()
        normalized_title = title.replace('\xa0', ' ')
    except:
        print(f'chapter {chapter_number} issue')
        title   = "Chương {chapter_number}"

    content = tree.xpath("string(/html/body/div[5]/div[1]/div/div[1]/div[2]/div/div[1])")
    content = process_content(content)
    chapter_content = title + '\n\n' + content + '\n\n\n'
    to_save = chapter_content if to_save == '' else to_save + chapter_content
    if len(to_save) < 2000:
        print(f'oh shit! {chapter_number}')

    if chapter_number % PAGES_TO_SAVE == 0 or chapter_number == TO_CHAPTER:
        with open(f'{SAVE_DIR}/vldp_{min(chapters_in_save)}-{max(chapters_in_save)}.txt','w') as f:
            f.write(to_save)
        to_save = ""
        chapters_in_save = []
