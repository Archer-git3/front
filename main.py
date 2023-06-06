import uuid

import psycopg2
from flask import Flask,redirect, session,  jsonify, render_template, request
import datetime
import requests

app = Flask(__name__, template_folder='html')


app.secret_key = 'your-secret-key'

def save_comment(comment, name):
    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO comments (id, name,comments) VALUES ('{uuid.uuid4()}','{name}','{comment}')")
    conn.commit()
    conn.close()


def load_comments_all():
    comments = []
    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()
    cur.execute(f"select name,comments from comments")
    results = cur.fetchall()
    for row in results:
        name = row[0]
        comment = row[1]
        comments.append({'name': name, 'comment': comment})
    conn.close()
    return comments

def load_comments_by_name(name_filter):
    comments = []
    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()
    cur.execute(f"select name,comments from comments")
    results = cur.fetchall()

    for row in results:
        name = row[0]
        if name == name_filter:
            comment = row[1]
            comments.append({'name': name, 'comment': comment})
    conn.close()
    return comments

def chek(email,number):
    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()

    cur.execute(f"""SELECT "like" FROM data WHERE email = '{email}'""")

    results = cur.fetchone()[0]
    is_favorite = number in results
    conn.commit()
    conn.close()

    return is_favorite

def choose_favorite(email):
    alls={1:"adsharski", 2:"imperetunsky",3:"kudbari",4:"harcho",5:"chihrtma",6:"gruzinskii_salat",7:"megrelskii_salat",8:"atsetsil",9:"hink_sir",10:"hink_bar",11:"pear_in_vine",12:"matsoni", 13:"tukva",14:"chashushuli",15:"chacha",16:"tarhun"}
    alls_for_views = {1: "хачапурі по аджарськи",2:"Імеритинський хачапурі",3:"Кубдарі",4:"Харчо",5:"Чихіртма",6:"Грузинський салат",7:"Мегрельський салат",8:"Ацецилі",9:"Хінкалії з сиром",10:"Хінкалії з бараниною",11:"Груші в червоному вині",12:"Матсоні",13:"Грузинський десерт з тиквою",14:"Чашушули",15:"Чача",16:"Тархун"}

    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute(f"""SELECT "like" FROM data WHERE email = '{email}'""")
    results = cur.fetchone()[0]
    values_list = [alls[key] for key in results if key in alls]
    values_list_for_views = [alls_for_views[key] for key in results if key in alls_for_views]

    conn.commit()
    conn.close()

    result= {
        "values_list": values_list,
        "values_list_for_views": values_list_for_views
    }
    conn.close()
    return  result

@app.route('/')
def site():
    logged_in = session.get('logged_in', False)
    return render_template('site.html', logged_in=logged_in)


@app.route('/history')
def history():
    logged_in = session.get('logged_in', False)
    return render_template('history.html', logged_in=logged_in)

@app.route('/adsharski')
def adsharski():
    nuber= 1
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/adsharski.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/imperetunsky')
def imperetunsky():
    nuber= 2
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/imperetunsky.html', logged_in=logged_in,is_favorite=is_favorite)


@app.route('/kudbari')
def kudbari():
    nuber= 3
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/kudbari.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/chihrtma')
def chihrtma():
    nuber = 5
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/chihrtma.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/harcho')
def harcho():
    nuber = 4
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/harcho.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/gruzinskii_salat')
def gruzinskii_salat():
    nuber= 6
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/gruzinskii_salat.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/megrelskii_salat')
def megrelskii_salat():
    nuber= 7
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/megrelskii_salat.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/atsetsil')
def atsetsil():
    nuber= 8
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/atsetsil.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/hink_sir')
def hink_sir():
    nuber= 9
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/hink_sir.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/hink_bar')
def hink_bar():
    nuber= 10
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/hink_bar.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/pear_in_vine')
def pear_in_vine():
    nuber= 11
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/pear_in_vine.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/matsoni')
def matsoni():
    nuber= 12
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/matsoni.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/tukva')
def tukva():
    nuber= 13
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/tukva.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/chashushuli')
def chashushuli():
    nuber= 14
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/chashushuli.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/chacha')
def chacha():
    nuber= 15
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/chacha.html', logged_in=logged_in,is_favorite=is_favorite)

@app.route('/tarhun')
def tarhun():
    nuber= 16
    logged_in = session.get('logged_in', False)
    email = session.get('email', False)
    if email !=False:
        is_favorite=chek(email,nuber)
    else:
        is_favorite=False
    return render_template('stravu/tarhun.html', logged_in=logged_in,is_favorite=is_favorite)


@app.route('/menu')
def menu():
    name = session.get('name')
    logged_in = session.get('logged_in', False)
    comments = load_comments_all()
    return render_template('menu.html', logged_in=logged_in,name=name,comments=comments)


@app.route('/deserts')
def deserts():
    name = session.get('name')
    logged_in = session.get('logged_in', False)
    comments = load_comments_all()
    return render_template('deserts.html', logged_in=logged_in,name=name,comments=comments)


@app.route('/prof')
def prof():
    name = session.get('name')
    email = session.get('email')
    logged_in = session.get('logged_in', False)
    comments = load_comments_by_name(name)
    like = choose_favorite(email)
    combined_list = zip(like["values_list"], like["values_list_for_views"])
    return render_template('profile.html', logged_in=logged_in,name=name, comments=comments,combined_list=combined_list)



@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()

    cur.execute(f"SELECT EXISTS(SELECT 1 FROM data WHERE email = '{email}')")
    result = cur.fetchone()[0]

    if result:
        return 'Електронна пошта вже зареєстрована. поверніться назад та спробуйте іншу пошту або увійти в свій акаунт'

    cur.execute(f"SELECT EXISTS(SELECT 1 FROM data WHERE name = '{name}')")
    result = cur.fetchone()[0]

    if result:
        return 'Така назва акаунта вже зареєстрована. поверніться назад та спробуйте вигадати нову назву акаунту або увійти в свій акаунт'
    cur.execute(f"""INSERT INTO data (name,email,password,"like") VALUES ('{name}','{email}','{password}',ARRAY[0])""")
    conn.commit()
    conn.close()
    session['logged_in'] = True
    session['name'] = name
    session['email'] = email
    return redirect('/prof')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()

    cur.execute(f"SELECT EXISTS(SELECT 1 FROM data WHERE email = '{email}')")
    result = cur.fetchone()[0]
    if result != True:
        return "Користувача з такою електронною поштою не існує"

    cur.execute(f"SELECT EXISTS(SELECT 1 FROM data WHERE password = '{password}')")
    result = cur.fetchone()[0]
    if result!= True:
        return "Невірний пароль"

    cur.execute(f"SELECT name FROM data WHERE email = '{email}'")
    name =cur.fetchone()[0]
    session['logged_in'] = True
    session['name'] = name
    session['email'] = email
    return redirect('/prof')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/submit_comment', methods=['POST'])
def add_comment():
    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()
    comments= request.form.get('comment')
    name = session.get('name')
    cur.execute(f"INSERT INTO comments (id,name,comments) VALUES({uuid.uuid4().int & (2**63-1)},'{name}','{comments}') ")
    conn.commit()
    conn.close()
    name = session.get('name')
    logged_in = session.get('logged_in', False)
    comments = load_comments_all()
    return render_template('menu.html', logged_in=logged_in, name=name, comments=comments)


@app.route('/submit_comment_for_deserts', methods=['POST'])
def add_comment_for_deserts():
    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()
    comments= request.form.get('comment')
    name = session.get('name')
    cur.execute(f"INSERT INTO comments (id,name,comments) VALUES({uuid.uuid4().int & (2**63-1)},'{name}','{comments}') ")
    conn.commit()
    conn.close()
    name = session.get('name')
    logged_in = session.get('logged_in', False)
    comments = load_comments_all()
    return render_template('deserts.html', logged_in=logged_in, name=name, comments=comments)

def insert_list(email, new_list,cur):


    cur.execute(f"""UPDATE data SET "like" = ARRAY{new_list} WHERE email = '{email}'""")

   # if row_exists:
        # Оновлюємо існуючий рядок
   #     cur.execute(f"UPDATE {table_name} SET {column_name} = {row_values} WHERE id = {row_id}")
   # else:
        # Вставляємо новий рядок
   #     cur.execute(f"INSERT INTO {table_name} (id, {column_name}) VALUES ({row_id}, {row_values})")



@app.route('/process_number', methods=['POST'])
def process_number():
    number = request.json['number']
    email = session.get('email')


    conn = psycopg2.connect(database="html_DB", user="postgres", password="111", host="localhost",
                            port="5432")
    cur = conn.cursor()
    cur.execute(f"""SELECT "like" FROM data WHERE email = '{email}'""")

    results = cur.fetchone()[0]
    if number in results:
        results.remove(number)  # Видалення числа зі списку улюблених
    else:
        results.append(number)  # Додавання числа до списку улюблених
    insert_list(email, results,cur)
    is_favorite = number in results

    conn.commit()
    conn.close()

    response = {'is_favorite': is_favorite}
    return jsonify(response),200


def get_weather(city):
    api_key = 'cd6bc136b82fbb646822050f97974856'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        temperature_in_celsius = temperature - 273.15
        description = data['weather'][0]['description']
        return temperature_in_celsius, description, city
    except requests.exceptions.RequestException:
        return None, 'Помилка при отриманні даних про погоду'

@app.route('/weather')
def weather_route():
    city = request.args.get('city')
    today = datetime.date.today().isoformat()
    temperature, description, city = get_weather(city)
    if temperature is not None:
        weather_data = [
            {
                'date': today,
                'temperature': round(temperature,1),
                'description': description
            }
        ]
        return jsonify(weather_data)
    else:
        return jsonify([])



if __name__ == '__main__':
    app.run(debug=True)
