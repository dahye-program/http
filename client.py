#최종 클라이언트
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def crawlingSend() :
    html = urlopen("http://192.168.0.164/PRESENTATION/ADVANCED/INFO_PRTINFO/TOP")
    bsObject = BeautifulSoup(html, "html.parser")

    # 현 프린터 상태 (사용할 수 있습니다. | 사용할 수 없습니다.)
    ready = bsObject.find('div', class_='preserve-white-space')

    #남은 토너량 
    color = bsObject.select('.color')
    i = 0
    array = []
    for link in color:
        array.append(link.get('height')) 
        i += 1
    # 총 사용 종이량 
    html = urlopen("http://192.168.0.164/PRESENTATION/ADVANCED/INFO_MENTINFO/TOP")
    bsObject = BeautifulSoup(html, "html.parser")
    result = bsObject.find('fieldset', class_='group')
    result = result.find('dd', class_='value clearfix')
    totalPaper = result.find('div', class_='preserve-white-space')

    print('black    : '+array[0]+'/50')
    print('cyan     : '+array[1]+'/50')
    print('magenta  : '+array[2]+'/50')
    print('yellow   : '+array[3]+'/50')
    print(ready.text)

    if('사용할 수 있습니다.'==ready.text):
        prtReady='usable'
    elif('사용 중입니다.'==ready.text):
        prtReady='using now'
    elif('오류가 발생했습니다. 제품의 표시등 또는 메시지를 확인하십시오.'==ready.text): 
        prtReady='ERROR'

    print(totalPaper.text)

    r = requests.post('http://192.168.0.180:8080', data='black    : '
            +array[0]+'/50\n'+'cyan     : '+array[1]+'/50\n'+'magenta  : '  
            +array[2]+'/50\n'+'yellow   : '+array[3]+'/50\n'+prtReady+'\n'+totalPaper.text)
    r.url
    return

if __name__=='__main__':
    # 뷰티풀소프 설정
    html = urlopen("http://192.168.0.164/PRESENTATION/ADVANCED/INFO_PRTINFO/TOP")
    bsObject = BeautifulSoup(html, "html.parser")

    # 현 프린터 상태 (사용할 수 있습니다. | 사용할 수 없습니다.)
    ready = bsObject.find('div', class_='preserve-white-space')
    flag = True
    crawlingSend()

