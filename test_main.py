#ver .02

import W_auth_class
import W_parser


try :
        
      UAS = W_auth_class.UserAuth()

except:
        
       pass
    
else:
     html_news = W_parser.get_html(UAS.urlFeed,UAS)
     html_user = W_parser.get_html(UAS.indexUrl,UAS)

     #запишем полученную html новостей в файл
     with open('./feed.html','w',encoding='utf-8') as html_feed:
         html_feed.write(html_news)
         
     #парсим и выводим юзера    
     user = W_parser.parse_user(html_user)
     print(user.name,user.href,user.friends,user.picture,sep = "\n",end = "\n\n\n\n")
     
     #парсим и выводим новости
     news = W_parser.parse_news(html_news)
     for n in news:
         print(n.title,n.title_href,n.info,n.info_href,n.text,n.author,n.author_href,n.time,sep="\n",end = "\n\n\n")

        
