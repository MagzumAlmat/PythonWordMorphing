import re

import bs4
from bs4 import BeautifulSoup
from wsgiref import headers
import requests
import lxml
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome("D:/thesauri parser/chromedriver.exe")
#driver.get(url)
#html=driver.execute_script("var myName='вяжущая минеральная добавка' let doc='SP_RK_3-03-101-2013' ftsTermInSentences(doc, term);")
import time
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import random

agents = [
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)'
]
headers = {"User-Agent":random.choice(agents)}
#driver=webdriver.Chrome("D:/thesauri parser/chromedriver.exe")
browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get('https://thesauri.kazniisa.kz/')


import pymorphy2

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#from pandas.tests.io.test_parquet import fp

output=[]
import random
import json
# agents = [
# 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'
# 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)'
# ]
#headers = {"User-Agent":random.choice(agents)}
headers = {'content-type': 'application/json'}

df = pd.ExcelFile('C:\\9.xlsx').parse('Лист1') #you could add index_col=0 if there's an index

#df = pd.ExcelFile('C:\\2Chapter1100.xlsx').parse('Лист1') #you could add index_col=0 if there's an index

x=[]
x.append(df['term'])

#print(x)
lenx=len(x)

stringOfX=str(x)
#stringOfX=stringOfX.replace(" ","%")
stringOfX=stringOfX.replace("0","")
stringOfX=stringOfX.replace("1","")
stringOfX=stringOfX.replace("2","")
stringOfX=stringOfX.replace("3","")
stringOfX=stringOfX.replace("4","")
stringOfX=stringOfX.replace("5","")
stringOfX=stringOfX.replace("6","")
stringOfX=stringOfX.replace("7","")
stringOfX=stringOfX.replace("8","")
stringOfX=stringOfX.replace("9","")
stringOfX=stringOfX.replace("[","")
#print('stringOfX--------',stringOfX)


s=[]


links=[]
docs=[]
output=''
    #print(df['term'][0])
link=''



i=0
ss=''
query=''



def scrap(line,headers,i,s):
    #print('тут должно лежать продолжение урла',line)

    #print('я внутри скрапера',i)




            # print(len(stringOfX1),'количество данных внутри переменной буфера')


    url="https://thesauri.kazniisa.kz:8081/thesauriBack/term/version/1/"+line
    #print('сформированный урл',url)
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')


    ss=str(soup)
    # strSoup=soup
    # strSoup=strSoup.lstrip('\n')
    bad_chars = ['\r', '\n']
    #print('ЭТО СУП', type(ss),ss)



    #data = json.loads(ss)
    #jtopy = json.dumps(data)  # json.dumps take a dictionary as input and returns a string as output.
    #dict_json = json.loads(jtopy)  # json.loads take a string as input and returns a dictionary as output.
    #print(dict_json)



    #print(len(soup))
    if len(ss) == 2:
        output = line.replace('%20', ' ')
        description = 'Не найдено данных'
        print(output, description)
        # with open('C:\\9.txt', 'a') as the_file:
        #     the_file.write(output+"    "+description+'\n')

    else:
        output = line.replace('%20', ' ')

        morphing(str(output))
        description = 'Есть данные'
        #print(output, description,len(ss))
        # with open('C:\\9.txt', 'a') as the_file:
        #     the_file.write(output + "    " + description + '\n')
        #print(ss)
        data = json.loads(ss)

        for item in data:
            print()
            print(item['doc_code'],output)
            print()
            morphing(output)
            #javascript = "ftsTermInSentences(" +item['doc_code'] +","+ output+")"
            javascript="ftsTermInSentences('"+item['doc_code']+"','"+output+"')"
            browser.execute_script(javascript)
            time.sleep(10)
            elements = browser.find_elements_by_id('sentencesListDiv')
            work=0
            for e in elements:
                # print(e.text)
                for it in range(0,len(check)):
                #print('данные внутри check',check[it])
                # strings = ['the', 'one']

                    regex = re.compile(check[it])
                    match = re.search(regex, e.text)
                    if match:
                        print('НАЙДЕНО в  "{}" в тексте "{}"'.format(check[it], e.text))
                        print()
                        text_pos = match.span()
                        print(e.text[match.start():match.end()])
                        work=work+1                        #Отработать с этими Найдено либо нет   =\
                        # with open('C:\\otvet.txt', 'a') as the_file:
                        #     the_file.write(output + "    " + '1' + '\n')


                    else:
                        workNo='Не найдено'
                        print('Не найдено в "{}"'.format(check[it]))
                        # with open('C:\\otvet.txt', 'a') as the_file:
                        #     the_file.write(output + "    " + '0' + '\n')
                        print()

                print("счетчик", work)
                if work >= 1:
                    break

        with open('C:\\otvet2.txt', 'a') as the_file:
            the_file.write(output + "    " + str(work)+ '\n')

            check.clear()

            time.sleep(1)

check=[]
def morphing(output):
    morph = pymorphy2.MorphAnalyzer()
    a=output
    # #a="железобетон"
    lst = a.replace('.', '').split()
    #print('количество слов в OUTPUT',len(lst))
    print()
    firstWordsingOrNot = ''
    secondWordsingOrNot = ''
    thirdWordsingOrNot = ''
    if len(lst)==1:
        #print('ветка с 1 словом')
        firstWord = morph.parse(str(lst[0]))[0]
        firstWordsingOrNot = str(firstWord.tag.number)
        if firstWordsingOrNot == 'sing' :
            print('все слова в термине единственного числа,идем по ветке проверки терминов единственного числа')
            #print('все слова в термине единственного числа,идем по ветке проверки терминов единственного числа')
            if len(lst) == 1:
                print('Одно слово в словосочетании')
                word = morph.parse(str(lst[0]))[0]
                #print('Единственное число:')
                v1, v2, v3, v4, v5, v6 = word.inflect({'sing', 'nomn'}),word.inflect({'sing', 'gent'}), word.inflect({'sing', 'datv'}), word.inflect({'sing', 'accs'}), word.inflect({'sing', 'ablt'}), word.inflect({'sing', 'loct'})
                #print(v1.word, v2.word, v3.word, v4.word, v5.word, v6.word)
                check.append(v1.word)
                check.append(v2.word)
                check.append(v3.word)
                check.append(v4.word)
                check.append(v5.word)
                check.append(v6.word)
            elif len(lst) == 2:
                print('два слова в словосочетании')
            elif len(lst) == 3:
                print('три слова в словосочетании')
        else:
            print('один из терминов множественное')


    elif len(lst)==2:
        #print('ветка с 2 словами')
        firstWord = morph.parse(str(lst[0]))[0]
        secondWord=morph.parse(str(lst[1]))[0]

        firstWordsingOrNot = str(firstWord.tag.number)
        secondWordsingOrNot = str(secondWord.tag.number)
        if firstWordsingOrNot == 'sing' and secondWordsingOrNot == 'sing' :

            print('все слова в термине единственного числа,идем по ветке проверки терминов единственного числа')

            if len(lst) == 1:
                print('Одно слово в словосочетании')

            elif len(lst) == 2:

                print('два слова в словосочетании')
                word = morph.parse(str(lst[0]))[0]
                # print('Единственное число:')
                v1, v2, v3, v4, v5, v6 = word.inflect({'sing', 'nomn'}), word.inflect({'sing', 'gent'}), word.inflect(
                    {'sing', 'datv'}), word.inflect({'sing', 'accs'}), word.inflect({'sing', 'ablt'}), word.inflect(
                    {'sing', 'loct'})
                # print(v1.word, v2.word, v3.word, v4.word ,v5.word ,v6.word)
                word = morph.parse(str(lst[1]))[0]
                #print('Единственное число:')
                secondv1, secondv2, secondv3, secondv4, secondv5, secondv6 = word.inflect(
                    {'sing', 'nomn'}), word.inflect({'sing', 'gent'}), word.inflect({'sing', 'datv'}), word.inflect(
                    {'sing', 'accs'}), word.inflect({'sing', 'ablt'}), word.inflect({'sing', 'loct'})
                # print(secondv1.word, secondv2.word, secondv3.word, secondv4.word, secondv5.word, secondv6.word)

                #print('Именительный', 'Кто? Что?', v1.word, secondv1.word)
                ImPadezh=v1.word+' '+secondv1.word

                # print('Родительный', 'Кого? Чего?', v2.word, secondv2.word)
                # print('Дательный', 'Кому? Чему?', v3.word, secondv3.word)
                # print('Винительный', 'Кого? Что?', v4.word, secondv4.word)
                # print('Творительный', 'Кем? Чем?', v5.word, secondv5.word)
                # print('Предложный', 'О ком? О чем?', v6.word, secondv6.word)
                check.append(v1.word+' '+secondv1.word)
                check.append(v2.word+' '+secondv2.word)
                check.append(v3.word+' '+secondv3.word)
                check.append(v4.word+' '+secondv4.word)
                check.append(v5.word+' '+secondv5.word)
                check.append(v6.word+' '+secondv6.word)
            elif len(lst) == 3:

                print('три слова в словосочетании')



        else:
            print('один из двух терминов множественное')


    elif len(lst)==3:
        #print('ветка с 3 словами')
        firstWord = morph.parse(str(lst[0]))[0]
        secondWord = morph.parse(str(lst[1]))[0]
        thirdWord=morph.parse(str(lst[2]))[0]
        #print(word.tag.number)
        firstWordsingOrNot = str(firstWord.tag.number)
        secondWordsingOrNot = str(secondWord.tag.number)
        thirdWordsingOrNot=str(thirdWord.tag.number)


        if firstWordsingOrNot=='sing' and secondWordsingOrNot=='sing' and thirdWordsingOrNot=='sing':


           print('все слова в термине единственного числа,идем по ветке проверки терминов единственного числа')

           if len(lst)==1:
                print('Одно слово в словосочетании')

           elif len(lst)==2:
                print('два слова в словосочетании')
           elif len(lst) == 3:
                    print('три слова в словосочетании')
                    word = morph.parse(str(lst[0]))[0]
                    #print(type(word.tag.number))
                    # print('Единственное число:')
                    v1, v2, v3, v4, v5, v6 = word.inflect({'sing', 'nomn'}), word.inflect({'sing', 'gent'}), word.inflect(
                        {'sing', 'datv'}), word.inflect({'sing', 'accs'}), word.inflect({'sing', 'ablt'}), word.inflect(
                        {'sing', 'loct'})
                    # print(v1.word, v2.word, v3.word, v4.word ,v5.word ,v6.word)
                    word = morph.parse(str(lst[1]))[0]
                    secondv1, secondv2, secondv3, secondv4, secondv5, secondv6 = word.inflect({'sing', 'nomn'}), word.inflect(
                        {'sing', 'gent'}), word.inflect({'sing', 'datv'}), word.inflect({'sing', 'accs'}), word.inflect(
                        {'sing', 'ablt'}), word.inflect({'sing', 'loct'})
                    # print(secondv1.word, secondv2.word, secondv3.word, secondv4.word, secondv5.word, secondv6.word)
                    word = morph.parse(str(lst[2]))[0]
                    #print('Единственное число:')

                    thirdv1, thirdv2, thirdv3, thirdv4, thirdv5, thirdv6 = word.inflect({'sing', 'nomn'}), word.inflect(
                        {'sing', 'gent'}), word.inflect({'sing', 'datv'}), word.inflect({'sing', 'accs'}), word.inflect(
                        {'sing', 'ablt'}), word.inflect({'sing', 'loct'})

                    # print('Именительный', 'Кто? Что?', v1.word, secondv1.word,thirdv1.word)
                    # print('Родительный', 'Кого? Чего?', v2.word, secondv2.word,thirdv2.word)
                    # print('Дательный', 'Кому? Чему?', v3.word, secondv3.word,thirdv3.word)
                    # print('Винительный', 'Кого? Что?', v4.word, secondv4.word,thirdv4.word)
                    # print('Творительный', 'Кем? Чем?', v5.word, secondv5.word,thirdv5.word)
                    # print('Предложный', 'О ком? О чем?', v6.word, secondv6.word,thirdv6.word)
                    check.append(v1.word+' '+secondv1.word+' '+thirdv1.word)
                    check.append(v2.word+' '+secondv2.word+' '+thirdv2.word)
                    check.append(v3.word+' '+secondv3.word+' '+thirdv3.word)
                    check.append(v4.word+' '+secondv4.word+' '+thirdv4.word)
                    check.append(v5.word+' '+secondv5.word+' '+thirdv5.word)
                    check.append(v6.word+' '+secondv6.word+' '+thirdv6.word)

                        #ADJF,Qual masc,sing,ablt
                        #ADJF,Qual masc,sing,loct


        else:
            print('один из трех терминов имеет множественное число')


#-----------------------------------------------------------------------------------------------------------



        # ss = ss.split("doc_code", maxsplit=2)[1]
        # ss.partition(',')[-2]
        # print(ss)
        # ss = ss[3:38]
        #
        # ss = ss.replace('"', '')
        # ss = ss.replace('doc_name', '')
        # ss = ss.replace('doc_nam', '')
        # ss = ss.replace('doc_na', '')
        # ss = ss.replace('doc_n', '')
        # ss = ss.replace('doc_', '')
        # ss = ss.replace('doc', '')
        # ss= ss.replace('do', '')
        # ss = ss.replace(',', '')
        # ss = ss.replace(':', '')
        # stringOfX12=stringOfX1.replace('%20', ' ')
        # print(ss,stringOfX12)









    # print(data[1]['doc_code'])
    # print(data[3]['doc_code'])
    # print(data[4]['doc_code'])
    # print(data[5]['doc_code'])
    # print(data[6]['doc_code'])


            # req = requests.get(url, headers)
            # soup = BeautifulSoup(url,"html.parser",from_encoding=req.encoding)

            #html_content = requests.get(url).text

            #soup = BeautifulSoup(html_content, "lxml").get_text("doc_code")

            # print(len(soup),soup)
            # if len(soup) == 2:
            #     output = line.replace('%20', ' ')
            #     description = 'Не найдено данных'
            #     print(output, description, soup)
            #
            # else:
            #     output = line.replace('%20', ' ')
            #     description = 'Есть данные'
            #     print(output, description, soup)
            #
            #
            #     soup = soup.split("doc_code", 1)[1]
            #     soup.partition(',')[-2]
            #     soup = soup[3:27]
            #     soup = soup.replace('"', '')
            #     soup = soup.replace('doc_name', '')
            #     soup = soup.replace('doc_nam', '')
            #     soup = soup.replace('doc_na', '')
            #     soup = soup.replace('doc_n', '')
            #     soup = soup.replace('doc_', '')
            #     soup = soup.replace('doc', '')
            #     soup = soup.replace('do', '')
            #     soup = soup.replace(',', '')
            #     print('this is soup',soup)




#s=[]
output=''
    #print(df['term'][0])
link=''

print('this is lenght',len(df))
for line in range(0,len(df)):

    stringOfX1 = df['term'][line].replace(" ", "%20")
    #print(line,stringOfX1)
    if len(stringOfX1)==1:
        stringOfX1 = df['term'][line].replace("%20", " ")


    scrap(stringOfX1, headers, i, ss)
    #print('термин добавится к урлу',stringOfX1)

    #
    i = i + 1

# with open("textbooks.json", "w") as writeJSON:
    #     json.dump(soup, writeJSON, ensure_ascii=False)








        #y = json.loads(soup)

        # the result is a Python dictionary:

    #print(y["doc_code"])

        #s.append(y,stringOfX1)
        #print('������ ��� ����� � JS',s)


        #resp=re.findall(r'(.*?)\(.*?\)', resp)
        #resp=re.findall(r"doc_code: \n\"\n([^\"]*)",resp)
        #print(resp)


        #print(resp['initial_term'])
        #print(resp['doc_code'])
        #print(output,description,soup)  # print the parsed data of html


