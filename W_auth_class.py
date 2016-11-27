#ver .03

import log
import requests
import pickle

class UserAuth():

    def __init__(self, login=None, password=None):
        self.login=login
        self.password=password
        self.s = requests.Session()
        self.indexUrl = 'https://park.mail.ru/pages/index/'
        self.urlLogin = 'https://park.mail.ru/login/'
        self.urlFeed = 'https://park.mail.ru/feed/subscribed/'
        try:
            log.log('I','Request to {}'.format(self.indexUrl))
            resp = self.s.get(self.indexUrl)
        except:
            log.log('E','Authentification is failed!')
            print("Error whith auth")
            return 0
        else:
            self.csrf_token = resp.cookies["csrftoken"]
            self.headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch, br',
                'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
                'Connection': 'keep-alive',
                'Host': 'park.mail.ru', 'Upgrade-Insecure-Requests': "1",
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
                'Referer': 'https://park.mail.ru/pages/index/'
                }
            while self.authorization() != True:
                pass


    def save_cookies(self, requests_cookiejar, filename):
        with open(filename, 'wb') as f:
            pickle.dump(requests_cookiejar, f)
        log.log('I','Cookies are saved.')    


    def load_cookies(self, filename):
        try:
            with open(filename, 'rb') as f:
                s= pickle.load(f)
                log.log('I','Cookies are loaded from file.')
                return s
        except: return self.s.cookies		

    def exit():
        pass

    def authorization (self):
        self.s.cookies=self.load_cookies('./cookie.txt')
        if(self.s.get(self.urlFeed)).url==self.urlFeed:
            log.log('I','Authentification is done.')
            return True
        self.s.headers = self.headers
        if self.login == None:
            self.login = ''
            while self.login.strip() == '':
                self.login = input('Enter an email to log in: ')

        if self.password == None:
            self.password = ''
            while self.password.strip() == '':
                self.password = input('Enter the password: ')

        r = self.s.post(self.urlLogin, {'login': self.login, 'password': self.password, 'csrfmiddlewaretoken': self.csrf_token})
        log.log('I','Post to {}'.format(self.urlLogin))
        if r.status_code==200:
            self.save_cookies(r.cookies, './cookie.txt')
            log.log('I','Authentification is done')
            return True
        else: 
            self.password=None
            self.login=None
            log.log('E','Authentification is failed!')
            return False		    
	
		

