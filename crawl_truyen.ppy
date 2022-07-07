import requests
from lxml import html
from tqdm import tqdm

PAGES_TO_SAVE = 10
FROM_CHAPTER  = 1
TO_CHAPTER    = 6009
ALL_CHAPTER   = 6009

to_save = ""
chapters_in_save = []

for chapter_number in tqdm(range(FROM_CHAPTER, TO_CHAPTER+1), initial=FROM_CHAPTER, desc="Chapter", total=ALL_CHAPTER):
    chapters_in_save.append(chapter_number)
    page = requests.get(f'https://metruyenchu.com/truyen/vu-luyen-dien-phong/chuong-{chapter_number}')
    tree = html.fromstring(page.content)  
    try:
        title   = tree.xpath('//*[@id="js-read__body"]/div[2]/text()')[0]
    except:
        print(f'chapter {chapter_number} issue')
        title   = "Chương {chapter_number}"
    content = tree.xpath('//*[@id="js-read__content"]/text()')
    content = ''.join(content)
    chapter_content = title + '\n' + content + '\n'
    to_save += chapter_content
    if chapter_number % PAGES_TO_SAVE == 0 or chapter_number == TO_CHAPTER:
        with open(f'vldp_{min(chapters_in_save)}-{max(chapters_in_save)}.txt','w') as f:
            f.write(to_save)
        to_save = ""
        chapters_in_save = []
