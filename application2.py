from flask import Flask, render_template,request
import csv

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/register",methods=["POST"])
def register():
    name=request.form.get("name")
    email=request.form.get("email")
    city=request.form.get("city")
    if not name or not city or not email:
        return render_template('status.html',status='fail')
    file= open(r"filename.csv",'a',newline='')
    file_read=open(r"filename.csv")
    s=file_read.read()
    file_read.close()
    if email not in s:
        writer=csv.writer(file)
        writer.writerow((name,email,city))
        file.close()
        return render_template('status.html',status='success')
    else:
        return render_template('status.html',repeated=1,status='fail')

@app.route('/registered')
def registered():
    with open(r"filename.csv",'r') as file:
        reader= csv.reader(file)
        studentslist=list(reader)
    return render_template('registered.html',students=studentslist)
    
if __name__=='__main__':
    app.run()
