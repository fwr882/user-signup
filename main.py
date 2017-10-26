from flask import Flask, request, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template("signup.html", title="signup")


@app.route('/signup', methods=['POST'])
def signup():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        username_error=""
        password_error=""
        verify_error=""
        email_error=""

    #validation checks
    if len(username) < 1:
        username_error = "Please enter a username"
    if len(password) < 1:
        password_error = "Please enter a password"
    if len(verify) < 1:
        verify_error = "Passwords don't match"
    for letter in str(username):
        if letter == ' ':
            username_error = "No spaces please"
    for letter in str(password):
        if letter == ' ':
            password_error = "No spaces please"
    if len(username) >=1 and len(username) < 3 or len(username) > 20:
          username_error = "Your username needs to be in between 3 and 20 characters"
    if len(password) >= 1 and len(password) < 3  or len(password) > 20:
          password_error = "Your password needs to be in between 3 and 20 characters"
    if str(password) != str(verify):
        verify_error = "Passwords don't match"
    
    if len(email) != 0:
        if len(email) < 3 or len(email) > 20:
            email_error = "Your email needs to be between 3 and 20 spaces and be formatted as 'howdydoody@thisiswhatanemaillookslike.com'"
        for letter in str(email):
            if letter == ' ':
                email_error = "No spaces please"
        if '@' not in email and '.' not in email:
            email_error = "Your email needs to be between 3 and 20 spaces and be formatted as 'howdydoody@thisiswhatanemaillookslike.com'"

       
    if username_error == '' and password_error == '' and email_error == '' and verify_error == '':
        return  render_template("welcome.html", username=username)
        
    return render_template('signup.html', title="signup", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)



if __name__ == '__main__':
    app.run()