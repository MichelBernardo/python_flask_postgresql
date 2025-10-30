from flask import Blueprint, jsonify, request
from src.database import db


# Creates a Blueprint. The first argument is the blueprint name.
api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_users():
    """
        Endpoint to retrieve all users.
    """
    conn = db.get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email FROM users;')
    users = cursor.fetchall()
    cursor.close()

    # Tranforms the results into a list of dictionaries.
    users_list = [{'id': row[0], 'name':row[1], 'email':row[2]} for row in users]

    return jsonify(users_list)

@api_bp.route('/users', methods=['POST'])
def create_user():
    """
        Endpoint for creating a new user.
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({
            'error': 'Name and e-mail are required.'
        }), 400

    conn = db.get_conn()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;',
        (name, email)
    )
    user_id = cursor.fetchone()[0]
    conn.commit()  # The transaction is completed.
    cursor.close()

    return jsonify({
        'id': user_id,
        'name': name,
        'email': email
    }), 201