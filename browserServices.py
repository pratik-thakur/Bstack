from flask import Flask, Response
import webbrowser
from time import sleep
import os
from pywinauto import Application
from browser_history.browsers import Chrome
from browser_history.browsers import Firefox
f = Chrome()


app = Flask(__name__)
enter_url=input('Enter URL you want to open: ')

@app.route('/start', methods=['GET'])
def home_page():
    print('Hello world - open')
    webbrowser.open(enter_url)


    return Response("browser opened", status=200, mimetype='text/html')


@app.route('/stop', methods=['GET'])
def home1_page():
    print('Hello world - close')
    browserExe = "chrome.exe"
    os. system("taskkill /f /im "+browserExe)



    return Response("browser closed", status=200, mimetype='text/html')

@app.route('/getlatest', methods=['GET'])
def home2_page():
    print('Hello world - getlastest')
    outputs = f.fetch_history()
    # his is a list of (datetime.datetime, url) tuples
    his = outputs.histories
    res=his[-1][1]
    print(res)
    # for i in res:
    #     print(i)
    # print(his[-1])




    return Response("getlatesturl", status=200, mimetype='text/html')


@app.route('/historyDel', methods=['GET'])
def home3_page():

    return Response("histrory cleasring", status=200, mimetype='text/html')

app.run(port=5000)





# # for opening the url
# enter_url=input('Enter URL you want to open: ')
# webbrowser.open(enter_url)




# for closing the specified browser
# sleep(5)
# browserExe = "chrome.exe"
# os. system("taskkill /f /im "+browserExe)



# # for getting the latesturl
# app = Application(backend='uia')
# app.connect(title_re=".*Chrome.*")
# element_name="Address and search bar"
# dlg = app.top_window()
# url = dlg.child_window(title=element_name, control_type="Edit").get_value()
# print(url)




# for getting the latesturl (updated wla) (chrome)
# f = Chrome()
# outputs = f.fetch_history()
# # his is a list of (datetime.datetime, url) tuples
# his = outputs.histories
# res=his[-1][1]
# print(res)
# # for i in res:
# #     print(i)
# print(his[-1])

# for getting the latesturl (updated wla) (firefox)
# f = Firefox()
# outputs = f.fetch_history()
# # his is a list of (datetime.datetime, url) tuples
# his = outputs.histories
# res=his[-1][1]
# print(res)
# # for i in res:
# #     print(i)
# print(his[-1])