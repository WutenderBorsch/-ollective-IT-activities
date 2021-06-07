from bs4 import BeautifulSoup \
    as bs
import codecs

doc = bs(codecs.open('C:/Users/anast/Downloads/Чёрный клевер смотреть онлайн — Аниме.html', encoding='utf-8', mode='r').read(),
         'html.parser')

title = doc.select('.anime-title')[0].find('h1').get_text()
rating = doc.select('.rating-value')[0].decode_contents().strip()
ratingСount = doc.select('.rating-count')[0].decode_contents().strip()

print('Название:', title, '\nРейтинг: ', rating, '\nКоличество отзывов:', ratingСount)

print('\n\nСвязанные сериалы:\n')

for i in doc.select('.seasons-item'):
    title = i.select('.seasons-item-name')[0].get_text().strip()
    info = i.select('.seasons-item-info')[0].get_text().strip()
    print("\tназвание:", title, ", доп. информация:", info)

print('\n\nкомментарии:\n')

com = []
for i in doc.select('.comment'):
    a = i.select('.comment-actions')[0].find('span', attrs={"class": "d-inline-flex"}).find('span', attrs={"class": "text-success"});

    if a is None:
        rating = 0;
    else:
        rating = int(a.get_text());

    title = i.select('.text-truncate')[0].find('a').get_text().strip()
    comment = i.select('.comment-text')[0].find('div').get_text().strip()
    
    print("\tИмя:", title,"\n\tCообщение:", comment,'\n')
    com.append({'title': title, 'comment': comment, 'rating': rating})

msg = sorted(com, key=lambda x: x['rating'])[len(com)-1]
print('Самый популярный комментарий:', msg['comment'], '\nКоличество лайков:', msg['rating'])
