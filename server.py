from flask import Flask,render_template,request;
from weather import get_current_weather;

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template(
        'index.html'
    )

@app.route('/weather')
def get_weather():
    #Obtener city del url(what the user types)
    city = request.args.get('city')

    #Verificar que no sea un espacio en blanco
    if not bool(city.strip()):
        city = 'Toronto'

    

    weather_data = get_current_weather(city)

    if weather_data == {'cod': '404', 'message': 'city not found'}:
        weather_data = 'Ciudad no encontrada'
        return render_template(
            'not_found.html',
            title = f'{city}'
        )


    else:
        return render_template(
            'weather.html',
            title = weather_data['name'],
            status = weather_data['weather'][0]['description'].capitalize(),
            temp = f"{weather_data['main']['temp']:.1f}",
            feels_like = f"{weather_data['main']['feels_like']:.1f}",
    )




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)