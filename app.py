from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join_us', methods=['GET', 'POST'])
def join_us():
    message = None
    if request.method == 'POST':
        full_name = request.form.get('fullName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        preferred_contact = request.form.get('preferredContact')
        position = request.form.get('position')
        message = request.form.get('message')

        # Process form data here, e.g., send an email or save to database

        message = "Form submitted successfully"

    return render_template('join_us.html', message=message)

if __name__ == '__main__':
    app.run()
