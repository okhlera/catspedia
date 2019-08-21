from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def index():
    with open("static/data.json","r+", encoding="utf-8") as file:
        cats=json.load(file)
        return render_template('index.html', cats=cats)


@app.route('/add', methods=['GET'])
def add_form():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add():
    fields = ['name', 'photo', 'description']
    for field in fields:
        if request.form.get(field, '') == '':
            return redirect('/add')
    cat = {
        "name": request.form['name'],
        "description": request.form['description'],
        "photo": request.form['photo']
    }
    file=open("static/data.json","r+", encoding="utf-8")
    cats=json.load(file)
    cats["cats"].append(cat)
    file.close()
    file = open("static/data.json", "w", encoding="utf-8")
    json.dump(cats,file)
    file.close()
    return redirect('/cats/{0}'.format(len(cats["cats"])))


@app.route('/cats/<id>', methods=['GET'])
def details(id):
    with open("static/data.json","r+", encoding="utf-8") as file:
        cats=json.load(file)
        cat = cats["cats"][int(id) - 1]
        return render_template('details.html', cat=cat)
@app.route('/like/<id>', methods=['GET'])
def like():
    pass


@app.route('/comment/<id>', methods=['POST'])
def comment():
    pass


app.run(debug=True, port=8080)