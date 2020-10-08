import requests


class Config:
    kd = '数据分析'
    referer = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput='
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': referer,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


class Spider:

    def __init__(self, kd=Config.kd):
        self.kd = kd
        self.url = Config.referer
        self.api = 'https://www.lagou.com/jobs/positionAjax.json'
        
        # 必须先请求referer网址
        self.sess = requests.session()
        self.sess.get(self.url, headers=Config.headers)

    def get_position(self, pn):
        data = {'first': 'true',
                'pn': str(pn),
                'kd': self.kd
                }
        # 向API发起POST请求
        r = self.sess.post(self.api, headers=Config.headers, data=data)
        
        # 直接.json()解析数据
        return r.json()['content']['positionResult']['result']

    def engine(self, total_pn):
        for pn in range(1, total_pn + 1):
            results = self.get_position(pn)
            for pos in results:
                print(pos['positionName'], pos['companyShortName'], pos['workYear'], pos['salary'])


if __name__ == '__main__':
    lagou = Spider()
    lagou.engine(2)
