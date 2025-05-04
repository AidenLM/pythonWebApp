from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aid_messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class AidMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_need = db.Column(db.Boolean, default=False)  # True if need, False if have

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'location': self.location,
            'created_at': self.created_at.isoformat(),
            'is_need': self.is_need
        }

with app.app_context():
    db.create_all()

def analyze_message(message, is_need_checkbox):
    # Keywords that strongly indicate a need
    need_keywords = [
        r'\bneed\b', r'\bneeds\b', r'\bneeded\b', r'\bneeding\b',
        r'\brequire\b', r'\brequires\b', r'\brequired\b', r'\brequiring\b',
        r'\bseeking\b', r'\bseeks\b', r'\bsought\b',
        r'\blooking for\b', r'\bsearching for\b',
        r'\brequest\b', r'\brequests\b', r'\brequested\b',
        r'\bhelp\b', r'\bhelping\b', r'\bhelped\b',
        r'\bemergency\b', r'\bemergencies\b',
        r'\bdesperate\b', r'\bdesperately\b',
        r'\bplease\b', r'\bkindly\b',
        r'\banyone\b', r'\bsomeone\b',
        r'\bcan you\b', r'\bcould you\b',
        r'\bwould you\b', r'\bwill you\b',
        r'\bif possible\b', r'\bif available\b'
    ]

    # Keywords that strongly indicate an offer
    offer_keywords = [
        r'\bhave\b', r'\bhas\b', r'\bhad\b', r'\bhaving\b',
        r'\bavailable\b', r'\bavailability\b',
        r'\boffer\b', r'\boffers\b', r'\boffered\b', r'\boffering\b',
        r'\bprovide\b', r'\bprovides\b', r'\bprovided\b', r'\bproviding\b',
        r'\bsupply\b', r'\bsupplies\b', r'\bsupplied\b', r'\bsupplying\b',
        r'\bdonate\b', r'\bdonates\b', r'\bdonated\b', r'\bdonating\b',
        r'\bcan help\b', r'\bcan assist\b',
        r'\bwilling to\b', r'\bready to\b',
        r'\bcontact me\b', r'\bmessage me\b',
        r'\bwe have\b', r'\bwe can\b',
        r'\bwe are\b', r'\bwe\'re\b'
    ]

    # Count matches for each type
    need_matches = sum(1 for pattern in need_keywords if re.search(pattern, message.lower()))
    offer_matches = sum(1 for pattern in offer_keywords if re.search(pattern, message.lower()))

    # If checkbox is checked, prioritize that
    if is_need_checkbox:
        return True

    # If there are clear keyword matches, use that
    if need_matches > offer_matches:
        return True
    elif offer_matches > need_matches:
        return False

    # Default to checkbox value if no clear keyword matches
    return is_need_checkbox

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/messages', methods=['GET'])
def get_messages():
    messages = AidMessage.query.order_by(AidMessage.created_at.desc()).all()
    return jsonify([message.to_dict() for message in messages])

@app.route('/api/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    is_need = analyze_message(data['message'], data.get('is_need', False))
    
    new_message = AidMessage(
        message=data['message'],
        location=data['location'],
        is_need=is_need
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201

@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = AidMessage.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)