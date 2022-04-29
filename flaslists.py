from socket import socket
from flask import Flask, render_template
app = Flask(__name__)
app.route('/<API end point>', methods = ['POST'])

posts = [
    {
        'list_name1': 'list 1',
        'list_name2': 'list 2',
        'list_name3': 'list 3'
    },
    {
        'id1': '1',
        'id2': '2',
        'id3': '3'
    }
]

data1 = [
    {
        'list_name': 'list 1',
        'Candidat_1': 'walid',
        'Candidat_2': 'Michelle'
    }
]

data2 = [
    {
        'list_name': 'list 2',
        'Candidat_1': 'Nastasia',
        'Candidat_2': 'Nadim'
    }
]

data3 = [
    {
        'list_name': 'list 3',
        'Candidat_1': 'Charbel',
        'Candidat_2': 'Ali'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/list1")
def list1():
    return render_template('list1.html', title='List_1', posts=data1)

@app.route("/list2")
def list2():
    return render_template('list2.html', title='List_2', posts=data2)

@app.route("/list3")
def list3():
    return render_template('list3.html', title='List_3', posts=data3)


@app.route("/voteregistered")
def voteregistered():
    return render_template('voteregistered.html')

@app.route('/encryption')
def encryption():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 3600))
    s.send(bytes("Data on wich encryption should be applied on", "utf-8"))
    complete_info =''
    while True:
        msg=s.recv(1024)
        if len(msg)<=0 :
            break
        complete_info += msg.decode("utf-8")
    return(complete_info)

if __name__ == '__main__':
    app.run(debug=True)