import requests
import lxml.etree as et
import time
import random
import json


id='280b6f782c8940c0b24274ada2d492f9'
company='新疆八一钢铁股份有限公司'

dic = [{'id':'280b6f782c8940c0b24274ada2d492f9','company':'新疆八一钢铁股份有限公司'},
       {'id':'cc09f7019ffce0339635ae5ca5bfa958','company':'天地科技股份有限公司'},
       {'id':'d3c1f6a797036894fe5fe92fa04e2c8d','company':'江苏长电科技股份有限公司'}]

data =[]

#链接爬取
for j in range(1):
    urls='https://www.qichacha.com/company_getinfos?unique='+id+'&companyname='+company+'&p='+str(j+1)+'&tab=assets&box=zhuanli&zlpublicationyear=&zlipclist=&zlkindcode=&zllegalstatus='

    header = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=16e05916fa267c-09198321f519d-5146291a-144000-16e05916fa498f; _uab_collina=157205144942970615109614; zg_did=%7B%22did%22%3A%20%2216e059183da1bc-0ac8b643df7923-5146291a-144000-16e059183db3f4%22%7D; acw_tc=3cdfd94815754414615573296eaf32477c1ead47cd6d2e1b68743c5216; QCCSESSID=sj1mea9re63e677ca264pa3d17; hasShow=1; CNZZDATA1254842228=1286981390-1572049319-https%253A%252F%252Fwww.baidu.com%252F%7C1575986015; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1575972710,1575977794,1575987994,1575988123; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1575988253; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201575987993290%2C%22updated%22%3A%201575988253291%2C%22info%22%3A%201575441460061%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22sp0.baidu.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%229714df193538d256ff02faa5acaf6796%22%7D',
        'Host': 'www.qichacha.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.qichacha.com/firm_280b6f782c8940c0b24274ada2d492f9.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    try:
        res = requests.get(url=urls,headers=header).text
        re = et.HTML(res)
        msg = re.xpath('//td/a/@href')
    except AttributeError:
        break
    print('正在爬取第'+str(j+1)+"页链接")
    time.sleep(0.24 + random.random())
    for i in msg:
        data.append(i)
# print(data)
#详细信息
datas = []
for i in data:
    dictdata = {}
    ul = 'https://www.qichacha.com/'+i
    ress = requests.get(url=ul,headers=header).text
    html0bj = et.HTML(ress)
    cn = "".join(html0bj.xpath('//table[@class="ntable"]/tbody/tr[2]/td[2]/text()'))#申请号
    day = "".join(html0bj.xpath('//table[@class="ntable"]/tbody/tr[2]/td[4]/text()'))#申请日
    openday = "".join(html0bj.xpath('//table[@class="ntable"]/tbody/tr[3]/td[4]/text()'))#公开日
    proposer = "".join(html0bj.xpath('//table[@class="ntable"]/tbody/tr[5]/td[4]/a/text()')).replace('\n','').replace(' ','')#申请人
    dictdata['cn'] = cn
    dictdata['day'] = day
    dictdata['openday'] = openday
    dictdata['proposer'] = proposer
    datas.append(dictdata)
    time.sleep(0.24 + random.random())
    print(dictdata)
# print(datas)

with open('company.json', 'w+', encoding="utf-8") as f:
    json.dump(datas, f, ensure_ascii=False)

