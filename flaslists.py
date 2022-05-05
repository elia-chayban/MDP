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

# @app.route('/', methods=["GET","POST"])
# def home(): 
    #  request = posts
    # if request.method == 'POST':
    #     if request.form['list_name'] == post_id:   
    #         mystring = "http://www.localhost:5000/encryption/" + request[1]
           
        #     c.execute(sql, (post_id,))
        #     return redirect("/")

        # else  
        #     mystring = "http://www.localhost:5000/encryption/" + requestcandidta[1]
        #     c.execute(sql, (post_id,))
        #     return redirect("/")

@app.route('/encryption/<value>')
def encryption(value):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("10.252.296.141", 3600))
    s.send(bytes(value, "utf-8"))
    complete_info = ''
    while True:
        msg=s.recv(1024)
        if len(msg)<=0 :
            break
        complete_info += msg.decode("utf-8")
        return(complete_info)

if __name__ == '__main__':
    app.run(debug=True)