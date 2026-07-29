from flask import Flask, jsonify

app = Flask(__name__)

# Sample Data
quotes = [
    "Verily, with hardship comes ease.",
    "Practice makes a man perfect.",
    "Consistency is the key to success."
    "CI/CD Pipeline Test Successful!"
    "Check automated Build,test and Deployment of the Flask App once pushed to the GitHub Repository.   "
]

# API Route
@app.route('/api/quotes')
def get_quotes():
    return jsonify(quotes)

# Serve Frontend HTML
@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)