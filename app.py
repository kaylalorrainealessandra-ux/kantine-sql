from flask import Flask, render_template, request, redirect
from meny import FASTE_RETT, UKESMENY, DRIKKE, DESSERT
import mysql.connector


app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

def get_conn():
    return mysql.connector.connect(
        host = "localhost",
        user = "kayla",
        password = "Passordtilsql123!", 
        database = "login"
    )

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        navn = request.form["navn"]
        brukernavn = request.form["brukernavn"]
        passord = request.form["navn"]
        
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO kunder (navn, brukernavn, passord) VALUES (%s, %s, %s)"
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/login')
    return render_template('register.html')



@app.route('/hovedmeny')
def hovedmeny():
    return render_template('hovedmeny.html', hovedmeny=FASTE_RETT)

@app.route('/ukesmeny')
def ukesmeny():
    return render_template('ukesmeny.html', ukesmeny=UKESMENY)

@app.route('/drikke')
def drikke():
    return render_template('drikke.html', drikke=DRIKKE)

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)