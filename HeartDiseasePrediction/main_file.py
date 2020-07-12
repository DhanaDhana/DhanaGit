from flask import Flask, render_template, url_for, request,redirect, session
from sklearn.externals import joblib
import os
import numpy as np
import pickle
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__, static_folder='static')

picFolder = os.path.join('static')
app.config['UPLOAD_FOLDER']=picFolder
UPLOAD_FOLDER2='static/uploads/'
app.config['UPLOAD_FOLDER2']=UPLOAD_FOLDER2

@app.route("/")
def heart():
    img=os.path.join(app.config['UPLOAD_FOLDER'],'wel.jpg')
    img2= os.path.join(app.config['UPLOAD_FOLDER'], 'saraswati.png')
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'heart5.webp')
    return render_template('heart.html',image=img,image2=img2,image3=img3)

@app.route("/home")
def home():
    if 'loggedin' in session:
        return render_template('home.html')
    return redirect(url_for('login'))

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'Dhana1525'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1525'
app.config['MYSQL_DB'] = 'HeartDiseaseDB'

# Intialize MySQL
mysql = MySQL(app)
# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('profile'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)
@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST':
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phoneNo = request.form['phone']
        address = request.form['addr']
        image = request.files['img']
        sex = request.form['gender']
        DOB = request.form['dob']
        # in database coloum image_path
        # static/uploads/<FileStorage: '_20200126_223932.JPG' ('image/jpeg')>
        pat = str(image).replace("<FileStorage: '", '')  # static/uploads/_20200126_223932.JPG' ('image/jpeg')>
        pat2 = pat.replace("('image/jpeg')>", '')  # static/uploads/_20200126_223932.JPG'
        pat3 = pat2.replace("'", '')  # static/uploads/_20200126_223932.JPG
        path = (os.path.join(app.config['UPLOAD_FOLDER2'], pat3))
        image.save(os.path.join(app.config['UPLOAD_FOLDER2'], image.filename))
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (username, password, email, phoneNo, address, path, sex, DOB))
        mysql.connection.commit()
        msg = 'You have successfully registered!'
        return render_template('register.html', msg=msg, )
    else:
        return redirect(url_for('adminLogin'))

@app.route('/pythonlogin/profile')
def profile():
    # Check if user is loggedin

    if 'loggedin' in session:

        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info

        return render_template('profile.html',account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/result', methods=['POST', 'GET'])
def result():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    trestbps = float(request.form['trestbps'])
    chol = float(request.form['chol'])
    restecg = float(request.form['restecg'])
    thalach = float(request.form['thalach'])
    exang = int(request.form['exang'])
    cp = int(request.form['cp'])
    fbs = float(request.form['fbs'])
    x = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                  thalach, exang]).reshape(1, -1)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO HeartPredictionList VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (age,sex,restecg,chol,restecg,thalach,exang,cp,fbs,))
    mysql.connection.commit()
    scaler_path = os.path.join(os.path.dirname(__file__), 'models/scaler.pkl')
    scaler = None
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)

    x = scaler.transform(x)
    model_path = os.path.join(os.path.dirname(__file__), 'models/rfc.sav')
    clf = joblib.load(model_path)
    y = clf.predict(x)
    print(y)
    # No heart disease
    if y == 0:
        return render_template('nodisease.html')
    # y=1,2,4,4 are stages of heart disease
    else:
        return render_template('heartdisease.htm', stage=int(y))

@app.route('/about')
def about():
    if 'loggedin' in session:
        img4 = os.path.join(app.config['UPLOAD_FOLDER'], 'heart8.webp')
        return render_template('about.html',image4=img4)
    return redirect(url_for('login'))
@app.route("/list")
def list():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from HeartPredictionList")
        data = cursor.fetchall()  # data from database
        return render_template('results.html',data=data)
    return redirect(url_for('login'))

@app.route("/contact")
def contact():
    return render_template('contactUs.html')

@app.route("/pay")
def pay():
    return render_template('payment.html')

@app.route("/adminLogin")
def adminLogin():
    return render_template('adminLogin.html')

@app.route("/adminLoginSuccess",methods=['POST'])
def adminLoginSuccess():

    if  request.method == 'POST':
        admin = request.form['username']
        skey = request.form['password']
    if  admin=="DhanaPolimera" and skey=="dhana@825":
        return render_template("register.html")

    else:
        # Account doesnt exist or username/password incorrect
        msg = 'Incorrect username/secretekey!'
        # Show the login form with message (if any)
        return render_template('adminLogin.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
