from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    preferredContact = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Application {self.fullName}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tongan_index')
def tongan_index():
    return render_template('tongan_index.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/join_us', methods=['GET', 'POST'])
def join_us():
    if request.method == 'GET':
        return render_template('join_us.html')

    full_name = request.form.get('fullName')
    email = request.form.get('email')
    phone = request.form.get('phone')
    preferred_contact = request.form.get('preferredContact')
    position = request.form.get('position')
    message = request.form.get('message')

    # Create a new Application object with the form data
    application = Application(fullName=full_name, email=email, phone=phone, preferredContact=preferred_contact, position=position, message=message)

    # Add the new Application object to the session
    db.session.add(application)

    # Commit the session to save the Application object to the database
    db.session.commit()

    response = {"success": True, "message": "Form submitted successfully"}
    return jsonify(response)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create tables in the database
    app.run()
