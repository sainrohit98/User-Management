from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import threading
import time

app = Flask(__name__)
CORS(app)

# In-memory data structure to store users
users = [
    {"id": 1, "name": "Rohit", "status": "Busy"},
    {"id": 2, "name": "Mohit", "status": "Busy"},
    {"id": 3, "name": "Shivam", "status": "Busy"},
    {"id": 4, "name": "Gaurav", "status": "Busy"},
    {"id": 5, "name": "Rani", "status": "Busy"}
]

def update_statuses():
    time.sleep(300) # Wait for 5 minutes (300 seconds)
    while True:
        for user in users[:3]:  # Update first three users
            user["status"] = "Hello"
        print("Updated statuses")

# Start the background thread for automatic updates
update_thread = threading.Thread(target=update_statuses)
update_thread.daemon = True
update_thread.start()

@app.route('/')
def dashboard():
    return render_template('dashboard.html', users=users)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    new_user['id'] = max(user['id'] for user in users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user.update(request.json)
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)