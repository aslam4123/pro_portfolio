from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # or your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'muhmdaslam189@gmail.com'
app.config['MAIL_PASSWORD'] = 'iqqesdyzxmturwrj'
app.config['MAIL_DEFAULT_SENDER'] = 'muhmdaslam189@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Capture the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create the email message
        msg = Message('New Message from Contact Form',
                      sender=email,
                      recipients=['muhmdaslam189@gmail.com'])
        msg.body = f"Message from {name} ({email}):\n\n{message}"

        # Send the email
        try:
            mail.send(msg)
            return redirect(url_for('thank_you'))
        except Exception as e:
            print(f"Error sending email: {e}")
            return "There was an issue sending your message. Please try again."

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
