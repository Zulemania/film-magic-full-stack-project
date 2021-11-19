import os
from flask import (Flask, jsonify, request, abort)
from models import setup_db
from flask_cors import CORS
from models import setup_db

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    

    @app.route('/')
    def get_greeting():
        return jsonify({
            'success': True,
            'message': 'Alive!!!'
        })
        
    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()