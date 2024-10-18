
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_1234'  # Es clave para manejar las sesiones.

# Datos simulados de usuarios (en un entorno real, esto sería una base de datos)
usuarios = {
    "Jose Luis": "huaycho2000",
    "usuario2": "password2"
}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar las credenciales
        if username in usuarios and usuarios[username] == password:
            session['username'] = username  # Almacenar el nombre de usuario en la sesión
            flash(f'Bienvenido {username}!', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    else:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar el usuario de la sesión
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
