from flask import Flask, request, render_template, redirect, url_for, session, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Example Flask Web App')


@app.get('/profile/')
def profile_dashboard():
    return render_template('/profile/dashboard.html')


@app.get('/login/')
def show_login():
    if 'username' in session:
        return redirect(url_for('profile_dashboard'))
    error = None
    return render_template('login.html', error=error)


@app.post('/login/')
def login():

    username = None

    if 'username' in request.form and 'password' in request.form:

        username = request.form['username'].lstrip().lower()
        password = request.form['password']

        if validate_login_credentials(username, password):
            session['username'] = username
            session['password'] = password

            return redirect(url_for('profile_dashboard'))
        else:
            flash('The credentials you provided are invalid')
            return redirect(url_for('show_login'))

    if username is None:
        flash('The username field is required')
    else:
        flash('The password field is required')

    return redirect(url_for('show_login'))


@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/page_not_found.html'), 404


def validate_login_credentials(username, password):
    return username == 'ash' and password == 'password'
