import requests
from lxml import html
from tqdm import tqdm

PAGES_TO_SAVE = 10
FROM_CHAPTER  = 61
TO_CHAPTER    = 6010
ALL_CHAPTER   = 6010

to_save = ""
chapters_in_save = []

for chapter_number in tqdm(range(FROM_CHAPTER, TO_CHAPTER+1), initial=FROM_CHAPTER, desc="Chapter", total=ALL_CHAPTER):
    chapters_in_save.append(chapter_number)
    page = requests.get(f'https://truyenchu24h.com/truyen/vo-luyen-dinh-phong/chuong-{chapter_number}/')
    tree = html.fromstring(page.content)
    try:
        title = tree.xpath('//*[@id="manga-reading-nav-head"]/div/div[1]/div/div[1]/ol/li[3]/text()')[0].strip()
    except:
        print(f'chapter {chapter_number} issue')
        title   = "Chương {chapter_number}"
    content = str(tree.xpath('string(//*[@class="entry-content_wrap"])')).strip()
    chapter_content = title + '\n\n' + content + '\n\n\n'
    to_save += chapter_content
    if chapter_number % PAGES_TO_SAVE == 0 or chapter_number == TO_CHAPTER:
        to_save = to_save.strip()
        with open(f'data/vo_luyen_dien_phong/vldp_{min(chapters_in_save)}-{max(chapters_in_save)}.txt','w') as f:
            f.write(to_save)
        to_save = ""
        chapters_in_save = []
