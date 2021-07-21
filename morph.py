import re

import bs4
from bs4 import BeautifulSoup
from wsgiref import headers
import requests
import lxml
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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

df = pd.ExcelFile('C:\\abzal.xlsx').parse('Лист1') #you could add index_col=0 if there's an index

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

        with open('C:\\abz.txt', 'a') as the_file:
            the_file.write(output+"    "+description+'\n')

    else:
        output = line.replace('%20', ' ')

        morphing(str(output))
        description = 'Есть данные'
        #print(output, description,len(ss))
        # with open('C:\\9.txt', 'a') as the_file:
        #     the_file.write(output + "    " + description + '\n')
        #print(ss)
        data = json.loads(ss)
        work = 0
        for item in data:
            print()
            print('Новый поиск ',item['doc_code'],output)

            print()
            morphing(output)
            if work == 1:
                break
            #javascript = "ftsTermInSentences(" +item['doc_code'] +","+ output+")"

            windows_before = browser.current_window_handle


            javascript="ftsTermInSentences('"+item['doc_code']+"','"+output+"')"

            browser.execute_script(javascript)
            time.sleep(1)
            elements = browser.find_elements_by_id('sentencesListDiv')
            browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
            browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')




            # WebDriverWait(browser, 5).until(EC.number_of_windows_to_be(2))
            # windows_after = browser.window_handles
            # new_window = [x for x in windows_after if x != windows_before][0]
            # browser.switch_to_window(new_window)
            # WebDriverWait(browser, 5).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "myframe")))

            # for el in elements:
            #     txt1=str(el.text)
            #     print('data',txt1)

            #elements=browser.find_element_by_tag_name('<b>')


            for e in elements:
                print()
                workNo=''
                print('Текст документа:   '+'\n',e.text)
                for it in range(0,len(check)):
                    #print('',check[it])
                    print()
                    regex = re.compile(check[it].replace('ё','е'))
                    print('this is regex ',regex)
                    match = re.search(regex, str(e.text))
                    print('this is match',match)


                    if match:
                        workNo='Найден'
                        print(item['doc_code']+ '  '+workNo+' Термин:   "{}" в тексте "{}"'.format(check[it], '\n'+e.text))
                        print()
                        text_pos = match.span()
                        print(e.text[match.start():match.end()])
                        work=work+1
                        print("счетчик", work)
                        if work == 1:
                            break

                        # with open('C:\\otvet.txt', 'a') as the_file:
                        #     the_file.write(output + "    " + '1' + '\n')
                    else:
                        workNo='Не найдено'
                        #print('Не найдено в "{}"'.format(check[it]))
                        # with open('C:\\otvet.txt', 'a') as the_file:
                        #     the_file.write(output + "    " + '0' + '\n')
                        print()



                    regex = re.compile(output.replace('ё', 'е'))
                    print('this is regex ', regex)
                    match = re.search(regex, str(e.text))
                    print('this is match', match)

                    if match:
                        workNo='Найден'
                        print(item['doc_code']+ '  '+workNo+' Термин:   "{}" в тексте "{}"'.format(check[it], '\n'+e.text))
                        print()
                        text_pos = match.span()
                        print(e.text[match.start():match.end()])
                        work=work+1
                        print("счетчик", work)
                        if work == 1:
                            break

                        # with open('C:\\otvet.txt', 'a') as the_file:
                        #     the_file.write(output + "    " + '1' + '\n')


                    else:
                        workNo='Не найдено'
                        #print('Не найдено в "{}"'.format(check[it]))
                        # with open('C:\\otvet.txt', 'a') as the_file:
                        #     the_file.write(output + "    " + '0' + '\n')
                        print()




        with open('C:\\abz.txt', 'a') as the_file:
            the_file.write(output + "    " + description+ "    " +str(work)+' '+workNo+"  в документе     "+'  '+item['doc_code']+ '\n')
            check.clear()




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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
    if len(lst)==1:  #Если 1 слово в термине
        #print('ветка с 1 словом')
        firstWord = morph.parse(str(lst[0]))[0]
        firstWordsingOrNot = str(firstWord.tag.number)

        print('Одно слово в словосочетании')
        word = morph.parse(str(lst[0]))[0]

        try:        #print('Единственное число:')
            v1, v2, v3, v4, v5, v6 = word.inflect({'sing', 'nomn'}),word.inflect({'sing', 'gent'}), word.inflect({'sing', 'datv'}), word.inflect({'sing', 'accs'}), word.inflect({'sing', 'ablt'}), word.inflect({'sing', 'loct'})
                    #print(v1.word, v2.word, v3.word, v4.word, v5.word, v6.word)

            #check.append(firstWord)
            check.append(v1.word)
            check.append(v2.word)
            check.append(v3.word)
            check.append(v4.word)
            check.append(v5.word)
            check.append(v6.word)
        except:
            pass
        try:
            plurv1, plurv2, plurv3, plurv4, plurv5, plurv6 = word.inflect({'plur', 'nomn'}), word.inflect({'plur', 'gent'}), word.inflect(
                {'plur', 'datv'}), word.inflect({'plur', 'accs'}), word.inflect({'plur', 'ablt'}), word.inflect(
                {'plur', 'loct'})
                    # print(v1.word, v2.word, v3.word, v4.word, v5.word, v6.word)

            check.append(plurv1.word)
            check.append(plurv2.word)
            check.append(plurv3.word)
            check.append(plurv4.word)
            check.append(plurv5.word)
            check.append(plurv6.word)
        except:
            pass
    elif len(lst)==2:
        #print('ветка с 2 словами')
        firstWord = morph.parse(str(lst[0]))[0]
        secondWord=morph.parse(str(lst[1]))[0]
        firstWordsingOrNot = str(firstWord.tag.number)
        secondWordsingOrNot = str(secondWord.tag.number)
        #print('два слова в словосочетании')

        word0 = morph.parse(str(lst[0]))[0]
        #print(word0.word)
        # print('Единственное число:')
        try:
            v1, v2, v3, v4, v5, v6 = word0.inflect({'sing', 'nomn'}), word0.inflect({'sing', 'gent'}), word0.inflect(
                {'sing', 'datv'}), word0.inflect({'sing', 'accs'}), word0.inflect({'sing', 'ablt'}), word0.inflect(
                {'sing', 'loct'})
            # print(v1.word, v2.word, v3.word, v4.word ,v5.word ,v6.word)
            word1 = morph.parse(str(lst[1]))[0]
            #print(word1.word)
            #print('Единственное число:')
            secondv1, secondv2, secondv3, secondv4, secondv5, secondv6 = word1.inflect(
                {'sing', 'nomn'}), word1.inflect({'sing', 'gent'}), word1.inflect({'sing', 'datv'}), word1.inflect(
                {'sing', 'accs'}), word1.inflect({'sing', 'ablt'}), word1.inflect({'sing', 'loct'})
            #check.append(word0+' '+word1)

            check.append(v1.word+' '+secondv1.word)
            check.append(v2.word+' '+secondv2.word)
            check.append(v3.word+' '+secondv3.word)
            check.append(v4.word+' '+secondv4.word)
            check.append(v5.word+' '+secondv5.word)
            check.append(v6.word+' '+secondv6.word)

            word2 = morph.parse(str(lst[0]))[0]

            #print(word2.word)

            plurv1, plurv2, plurv3, plurv4, plurv5, plurv6 = word2.inflect({'plur', 'nomn'}), word2.inflect({'plur', 'gent'}), word2.inflect(
                {'plur', 'datv'}), word2.inflect({'plur', 'accs'}), word2.inflect({'plur', 'ablt'}), word2.inflect(
                {'plur', 'loct'})
            #print(plurv1.word, plurv2.word, plurv3.word, plurv4.word ,plurv5.word ,plurv6.word)
        except:
            pass

        word3 = morph.parse(str(lst[1]))[0]
        #print(word3.word)
        # print('Единственное число:')

        try:
            plursecondv1, plursecondv2, plursecondv3, plursecondv4, plursecondv5, plursecondv6 = word3.inflect({'plur', 'nomn'}), word3.inflect({'plur', 'gent'}), word3.inflect({'plur', 'datv'}), word3.inflect({'plur', 'accs'}), word3.inflect({'plur', 'ablt'}), word3.inflect({'plur', 'loct'})
            print(str(plursecondv1.word))

            check.append(plurv1.word + ' ' + plursecondv1.word)
            check.append(plurv2.word + ' ' + plursecondv2.word)
            check.append(plurv3.word + ' ' + plursecondv3.word)
            check.append(plurv4.word + ' ' + plursecondv4.word)
            check.append(plurv5.word + ' ' + plursecondv5.word)
            check.append(plurv6.word + ' ' + plursecondv6.word)


        except:
            pass

            print("Что-то пошло не так")
            errormessage='Что-то пошло не так в склонении слова '+ str(word3)
        #check.append(word0 + ' ' + word1)
        # print(plurv1.word)
        # print(plurv2.word)
        # print(plurv3.word)
        # print(plurv4.word)
        # print(plurv5.word)
        # print(plurv6.word)



    elif len(lst)==3:
        #print('ветка с 3 словами')
        firstWord = morph.parse(str(lst[0]))[0]
        secondWord = morph.parse(str(lst[1]))[0]
        thirdWord=morph.parse(str(lst[2]))[0]
        #print(word.tag.number)
        firstWordsingOrNot = str(firstWord.tag.number)
        secondWordsingOrNot = str(secondWord.tag.number)
        thirdWordsingOrNot=str(thirdWord.tag.number)

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

        try:
            check.append(v1.word+' '+secondv1.word+' '+thirdv1.word)
            check.append(v2.word+' '+secondv2.word+' '+thirdv2.word)
            check.append(v3.word+' '+secondv3.word+' '+thirdv3.word)
            check.append(v4.word+' '+secondv4.word+' '+thirdv4.word)
            check.append(v5.word+' '+secondv5.word+' '+thirdv5.word)
            check.append(v6.word+' '+secondv6.word+' '+thirdv6.word)
        except:
            pass
        word = morph.parse(str(lst[0]))[0]
        plurv1, plurv2, plurv3, plurv4, plurv5, plurv6 = word.inflect({'plur', 'nomn'}), word.inflect({'plur', 'gent'}), word.inflect(
            {'plur', 'datv'}), word.inflect({'plur', 'accs'}), word.inflect({'plur', 'ablt'}), word.inflect(
            {'plur', 'loct'})
                # print(v1.word, v2.word, v3.word, v4.word ,v5.word ,v6.word)
        word = morph.parse(str(lst[1]))[0]
        plursecondv1, plursecondv2, plursecondv3, plursecondv4, plursecondv5, plursecondv6 = word.inflect(
            {'plur', 'nomn'}), word.inflect({'plur', 'gent'}), word.inflect({'plur', 'datv'}), word.inflect({'plur', 'accs'}), word.inflect(
            {'plur', 'ablt'}), word.inflect({'plur', 'loct'})
                # print(secondv1.word, secondv2.word, secondv3.word, secondv4.word, secondv5.word, secondv6.word)
        word = morph.parse(str(lst[2]))[0]
                # print('Единственное число:')



        try:
            plurthirdv1, plurthirdv2, plurthirdv3, plurthirdv4, plurthirdv5, plurthirdv6 = word.inflect(
                {'plur', 'nomn'}), word.inflect(
                {'plur', 'gent'}), word.inflect({'plur', 'datv'}), word.inflect({'plur', 'accs'}), word.inflect(
                {'plur', 'ablt'}), word.inflect({'plur', 'loct'})

            check.append(plurv1.word + ' ' + plursecondv1.word + ' ' + plurthirdv1.word)
            check.append(plurv2.word + ' ' + plursecondv2.word + ' ' + plurthirdv2.word)
            check.append(plurv3.word + ' ' + plursecondv3.word + ' ' + plurthirdv3.word)
            check.append(plurv4.word + ' ' + plursecondv4.word + ' ' + plurthirdv4.word)
            check.append(plurv5.word + ' ' + plursecondv5.word + ' ' + plurthirdv5.word)
            check.append(plurv6.word + ' ' + plursecondv6.word + ' ' + plurthirdv6.word)


        except:
            pass

            print("Что-то пошло не так")
            errormessage='Что-то пошло не так в склонении слова '+ str(word)


#-----------------------------------------------------------------------------------------------------------


output=''
    #print(df['term'][0])
link=''

#print('this is lenght',len(df))
for line in range(0,len(df)):

    stringOfX1 = df['term'][line].replace(" ", "%20")
    #print(line,stringOfX1)
    if len(stringOfX1)==1:
        stringOfX1 = df['term'][line].replace("%20", " ")


    scrap(str(stringOfX1), headers, i, ss)
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


