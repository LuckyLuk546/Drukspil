from flask import Flask, render_template, url_for, session, redirect
from datetime import date, datetime, timedelta
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template
import dataconnection

app = Flask(__name__)
app.secret_key = 'super secret key'
Mobility(app)

@app.route("/")
@app.route("/index")
@app.route("/forside")
@mobile_template('{mobile/}index.html')
def index(template):

    today = date.today()
    yesterday = today - timedelta(days=1)
    weekday = date.today().weekday()
    info_table = dataconnection.get_info_table().fillna(-1)

    table = dataconnection.get_newest_cars().fillna(-1)
    table[['car_price']] = table[['car_price']].astype(int) # Fjerner .0

    if 'playerlist' not in session:
        session['playerlist'] = []
    playerlist = session['playerlist']

    return render_template("index.html", info_table=info_table, today=today, yesterday=yesterday, weekday=weekday, table=table, playerlist=playerlist, title='Drukspil')

@app.route("/spil")
@mobile_template('{mobile/}spil.html')
def spil(template):

    today = date.today()
    yesterday = today - timedelta(days=1)
    weekday = date.today().weekday()
    info_table = dataconnection.get_info_table().fillna(-1)

    table = dataconnection.get_newest_cars().fillna(-1)
    table[['car_price']] = table[['car_price']].astype(int) # Fjerner .0

    if 'playerlist' not in session:
        return redirect(url_for('index'))
    playerlist = session['playerlist']
    questionlist = ['XXX skal give en lussing til YYY', 'XXX må give to shots ud', 'Fælles skål!', 'XXX skal læse en hel bog imens han/hun står på hovedet :)', 'XXX skal fortælle en hemmelighed MAX 2 personer i selvskabet kender']

    return render_template("spil.html", info_table=info_table, today=today, yesterday=yesterday, weekday=weekday, table=table, playerlist=playerlist, questionlist=questionlist, title='Drukspil')

@app.route("/tospillere/<string:playeret>/<string:playerto>")
@mobile_template('{mobile/}index.html')
def tospillere(template,playeret,playerto):
    
    session['playerlist'] = [playeret, playerto]
    playerlist = session['playerlist']

    return redirect(url_for('spil'))

@app.route("/trespillere/<string:playeret>/<string:playerto>/<string:playertre>")
@mobile_template('{mobile/}index.html')
def trespillere(template,playeret,playerto,playertre):
    
    session['playerlist'] = [playeret, playerto, playertre]
    playerlist = session['playerlist']

    return redirect(url_for('spil'))

@app.route("/qrtest")
@mobile_template('{mobile/}qrtest.html')
def qrtest(template):
    today = date.today()
    yesterday = today - timedelta(days=1)
    weekday = date.today().weekday()
    info_table = dataconnection.get_info_table().fillna(-1)

    return render_template("qrtest.html", info_table=info_table, today=today, yesterday=yesterday, weekday=weekday, title='Qrtest')