from flask import Flask, url_for, request, render_template
import temperaturen_umrechnen as t

#export FLASK_ENV=development

app = Flask(__name__)


@app.route("/",)
def index(a = None, b = None, u = None, temp = None):
    if a != None and b != None:
        return render_template('index_temp.html', a=a, b=b, u=u, temp=temp, instruction='Welche Einheit wollen Sie umrechnen?')
    else:
        return render_template('index_temp.html',  instruction='Welche Einheit wollen Sie umrechnen?')

@app.route("/calc", methods=['POST'])
def calc():
    u = int(request.form['unit'])
    temperature = int(request.form['temperature'])
    if u == 0:
        a = round(t.celsius_to_fahrenheit(temperature), 2)
        b = round(t.celsius_to_kelvin(temperature), 2)
        return index(a, b, u, temperature)
    elif u == 1:
        a = round(t.fahrenheit_to_celsius(temperature), 2)
        b = round(t.fahrenheit_to_kelvin(temperature), 2)
        return index(a, b, u, temperature)
    elif u == 2:
        a = round(t.kelvin_to_celsius(temperature), 2)
        b = round(t.kelvin_to_fahrenheit(temperature), 2)
        return index(a, b, u, temperature)
    




if __name__ == "__main__":
    app.run(port=5000, debug=True)
