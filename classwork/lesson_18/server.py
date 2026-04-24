from flask import Flask, render_template, request, redirect, url_for
from datetime import date

from functions import (
    read_data,
    statistics,
    add_habit
)

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", 
                           habits=read_data(), 
                           stats=statistics(),
                           today = date.today().isoformat()
                        )

@app.post("/add")
def add():
    title = request.form.get("title")
    add_habit(title)
    return redirect(url_for("index"))
    

@app.post("/delete/<int:habit_id>")
def delete(habit_id):
    del_habit(habit_id)
    return redirect(url_for("index"))
    


app.run(port=5003)