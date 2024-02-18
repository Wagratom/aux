from flask import Flask, jsonify, request

app = Flask(__name__)
DATABASE = []

@app.route('/')
def all_users():
	return DATABASE

@app.route('/create-user', methods=['POST'])
def create_user():
	user = request.json
	if not user:
		return jsonify({"error": "No data provided"}), 400
	if 'name' not in user:
		return jsonify({"error": "No name provided"}), 400
	if user.get('name') in [u.get('name') for u in DATABASE]:
		return jsonify({"error": "User already exists"}), 400
	DATABASE.append(user)
	return user

@app.route('delete-user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	user = next((user for user in DATABASE if user["id"] == user_id), None)
	if user:
		DATABASE.remove(user)
		return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200
	else:
		return jsonify({"error": f"User with ID {user_id} not found"}), 404

# @app.route("update-user")
# def update_user():
# 	return "update user"

if __name__ == '__main__':
	app.run(debug=True)
