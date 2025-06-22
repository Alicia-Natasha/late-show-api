from flask import Blueprint, request, jsonify
from server.app import db
from server.models.appearance import Appearance
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance_bp', __name__, url_prefix='/appearances')

@appearance_bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    try:
        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()
        return {
            "id": appearance.id,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "rating": appearance.rating
        }, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
