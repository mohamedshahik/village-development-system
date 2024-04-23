from flask import Flask, render_template, request, session, flash

import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/OfficerLogin')
def OfficerLogin():
    return render_template('OfficerLogin.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route('/NewUser')
def NewUser():
    return render_template('NewUser.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("you are successfully Login")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/NewOfficer")
def NewOfficer():
    return render_template('NewOfficer.html')


@app.route("/newofficer", methods=['GET', 'POST'])
def newofficer():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        depart = request.form['depart']
        username = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into officertb values('','" + name + "','" + mobile + "','" + email + "','" + address + "','" + depart + "','" + username + "','" + password + "')")
        conn.commit()
        conn.close()
        flash("Record Saved!")

    return render_template('NewOfficer.html')


@app.route("/AOfficerInfo")
def AOfficerInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM officertb ")
    data = cur.fetchall()
    return render_template('AOfficerInfo.html', data=data)


@app.route("/AComplaintInfo")
def AComplaintInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb  ")
    data = cur.fetchall()
    return render_template('AComplaintInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into regtb values('','" + name + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
        conn.commit()
        conn.close()
        flash("Record Saved!")

    return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash('Username or Password is wrong')
            return render_template('UserLogin.html', data=data)

        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and password='" + password + "'")
            data = cur.fetchall()
            flash("you are successfully logged in")
            return render_template('UserHome.html', data=data)


@app.route("/NewComplaint")
def NewComplaint():
    return render_template('NewComplaint.html', uname=session['uname'])


@app.route("/newcomplaint", methods=['GET', 'POST'])
def newcomplaint():
    if request.method == 'POST':
        uname = session['uname']
        depart = request.form['depart']
        info = request.form['info']

        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save("static/upload/" + savename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM regtb where  username='" + uname + "'")
        data = cursor.fetchone()

        if data:
            mobile = data[2]

        else:
            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into complainttb values('','" + uname + "','" + mobile + "','" + depart + "','" + info + "','" + savename + "','','waiting','','')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM complainttb where username='" + uname + "'  ")
        data = cur.fetchall()
        flash('Complaint Post Successfully!')
        return render_template('UComplaintInfo.html', data=data)


@app.route("/UComplaintInfo")
def UComplaintInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb where username='" + session['uname'] + "' and Status='waiting' ")
    data = cur.fetchall()
    return render_template('UComplaintInfo.html', data=data)


@app.route("/UActionInfo")
def UActionInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb where username='" + session['uname'] + "' and Status !='waiting' ")
    data = cur.fetchall()
    return render_template('UActionInfo.html', data=data)


@app.route("/officerlogin", methods=['GET', 'POST'])
def officerlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['oname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from officertb where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash('Username or Password is wrong')
            return render_template('OfficerLogin.html', data=data)

        else:
            session['depart'] = data[5]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM officertb where username='" + username + "' and password='" + password + "'")
            data = cur.fetchall()
            flash("you are successfully logged in")
            return render_template('OfficerHome.html', data=data)


@app.route("/OfficerHome")
def OfficerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM officertb where username='" + session['oname'] + "' ")
    data = cur.fetchall()
    return render_template('OActionInfo.html', data=data)


@app.route("/OActionInfo")
def OActionInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb where Department='" + session['depart'] + "' and Status ='completed' ")
    data = cur.fetchall()
    return render_template('OActionInfo.html', data=data)


@app.route("/OComplaintInfo")
def OComplaintInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb where Department='" + session['depart'] + "' and Status !='completed' ")
    data = cur.fetchall()
    return render_template('OComplaintInfo.html', data=data)


@app.route("/action")
def action():
    id = request.args.get('id')
    session["cid"] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM complainttb where  id='" + id + "'")
    data = cursor.fetchone()

    if data:
        mobile = data[2]

    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complainttb where id='" + id + "' ")
    data = cur.fetchall()
    return render_template('Action.html', data=data)


@app.route("/actioninfo", methods=['GET', 'POST'])
def actioninfo():
    if request.method == 'POST':
        act = request.form['act']
        ainfo = request.form['ainfo']
        oname = session['oname']

        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save("static/upload/" + savename)

        id = session["cid"]

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM complainttb where  id='" + id + "'")
        data = cursor.fetchone()

        if data:
            uuname= data[1]
            mobile = data[2]

        else:
            return 'Incorrect username / password !'
        msg = "Your Complaint Action Info" + ainfo
        sendmsg(mobile, msg)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM regtb where  username='" + uuname + "'")
        data = cursor.fetchone()

        if data:

            email = data[3]

        else:
            return 'Incorrect username / password !'
        sendmail(email,msg)





        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Villagepydb')
        cursor = conn.cursor()
        cursor.execute(
            "update   complainttb set Action='" + ainfo + "',Status='" + act + "' , OfficerName='" + oname + "',Cimage='"+savename+"' where id='" + id + "'")
        conn.commit()
        conn.close()

        flash("Action Info Update successfully")

        return render_template('OActionInfo.html')



def sendmsg(targetno,message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")


def sendmail(Mailid,message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "qmgn xecl bkqv musr")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
