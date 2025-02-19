from app import app, db
from flask import render_template, redirect, url_for
from app.models import User
from app.controllers.user_controller import add_user


# Strona główna
@app.route("/")
def home():
    # Pobieramy wszystkich użytkowników z bazy danych
    users = User.query.all()
    return render_template("home.html", users=users)


# Strona "O nas"
@app.route("/about")
def about():
    return render_template("about.html")


# Strona dodawania użytkownika
@app.route("/add_user")
def add_user_route():
    # Dodajemy nowego użytkownika za pomocą kontrolera
    add_user("Jan", "jan@example.com")
    # Przekierowujemy na stronę główną po dodaniu użytkownika
    return redirect(url_for('home'))  # Można użyć 'home' bo mamy zdefiniowaną funkcję o tej nazwie


# Przykład trasy do edytowania użytkownika
@app.route("/edit_user/<int:user_id>")
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)


# Przykład trasy do usuwania użytkownika
@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))  # Po usunięciu wracamy do strony głównej
