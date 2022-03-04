from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", filas=8, columnas=8 )

@app.route("/<int:numero>")
def colum(numero):
    return render_template("index.html", filas=8, columnas=numero )

@app.route("/<int:numero>/<int:numero2>")
def filas(numero,numero2):
    return render_template("index.html", filas=numero2, columnas=numero )

@app.route("/<int:numero>/<int:numero2>/<color1>")
def filascolor(numero,numero2,color1):
    return render_template("index.html", filas=numero2, columnas=numero, color=color1 )

@app.route("/<int:numero>/<int:numero2>/<color1>/<color2>")
def columnasscolor(numero,numero2,color1,color2):
    return render_template("index.html", filas=numero2, columnas=numero, color=color1, color2=color2 )









if __name__=="__main__":
    app.run(debug=True)