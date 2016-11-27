#ver .03

import log
import W_user_class
import W_news_class
from bs4 import BeautifulSoup

def parse_user(html):
    soup = BeautifulSoup(html, "html.parser")
    div_user = soup.find("div", {"class" : "dropdown-user"} )

    u = W_user_class.User()
    
    u.href = div_user.a["href"]
    u.name = div_user.find("div",{"class":"full_name"}).a.text
    u.picture = div_user.a.img["src"]
                           
    li_f = soup.find_all('li', class_ = "profile__friends-list-item")
    for i in li_f:
        u.friends.append({
            'Friend': i.a.text,
            'Href': i.a["href"],
            'Picture': i.a.img["src"]
            })
    log.log('D','User was parsed.')
    return u
                           
def parse_news(html):
    soup = BeautifulSoup(html, "html.parser")
    news = []
    articles = soup.find_all("article", class_ = "topic topic-type-topic js-topic" )

    for ar in articles:
        news_i = W_news_class.News()
        news_i.title = ar.header.h1.a.text
        news_i.title_href = ar.header.h1.a["href"]
        news_i.info = ar.header.div.text
        news_i.info_href = ar.header.div.a["href"]
        news_i.text = ar.find("div", {"class" : "cf"}).find("div", {"class" : "topic-content text"}).text
        news_i.author = ar.footer.find("li",{"class":"topic-info-author"}).find("a",{"rel":"author"}).text
        news_i.author_href = ar.footer.find("li",{"class":"topic-info-author"}).find("a",{"rel":"author"})["href"]
        news_i.time = ar.footer.find("li",{"class":"topic-info-date"}).span.text
        news.append(news_i)
    log.log('D','News was parsed.')
    return news




def get_html(url,UAS):
    log.log('I','Request to {}'.format(url))
    response = UAS.s.get(url)
    return response.text

            
     
        
        

   
     
           
