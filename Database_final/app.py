from database_updation import DemoData
from flask import Flask, render_template,redirect, url_for, request,jsonify
app = Flask(__name__)
labels = []
values = []

def find_query(number):
    if number == "1":
        return ['t1','t2']
    if number == "2":
        return ['t3','t4']
    if number == "3":
        return ['t5']
    if number == "4":
        return ['t6','t7']
    if number == "5":
        return ['t8','t9']
    if number == "6":
        return ['t10']
    if number == "7":
        return ['t11']
    if number == "8":
        return ['t12']
    if number == '10':
        return ['t15','t16','t17','t18','t19','t20','t21']
    if number == '11':
        return ['t22','t23','t24']
    else:
        return "null"

@app.route("/data")
def data():
    label = labels
    script = values
    return jsonify(results = script, labels = label)

@app.route('/queries/<name>/<pwd>',methods = ['POST', 'GET'])
def queries(name,pwd):
     connection_string = "host='localhost' dbname='demo' user={} password= {}"
     executing = DemoData(connection_string.format(name,pwd))
     if request.method == 'POST':
         query_no = request.form['query']
         table_name = find_query(query_no)
         table = []
         for row in table_name:
             table.append(request.form[row])
     else:
         table = request.args.get('table_name')
         query_no = request.args.get('query')
     records = executing.execution(table, query_no)
     return render_template('result.html', result=records)

@app.route('/success/<name>/<pwd>')
def success(name,pwd):
    if ((name == 'demo' and pwd == 'demo') or(name == 'demo_select' and pwd == 'demo_select')):
        return render_template('queries.html',user = name,password = pwd)
    else:
        return render_template('error.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        password = request.form['password']
        return redirect(url_for('success',name = user,pwd = password))
    else:
        user = request.args.get('nm')
        password = request.args.get('password')
        return redirect(url_for('success',name = user,pwd = password))

app.run(debug=True)
