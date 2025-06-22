from flask import Blueprint, jsonify, request
from server.app import db
from server.models.episode import Episode
from server.models.appearance import Appearance
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode_bp', __name__, url_prefix='/episodes')

@episode_bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {"id": ep.id, "date": ep.date.isoformat(), "number": ep.number}
        for ep in episodes
    ])

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return {
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": [
            {
                "id": app.id,
                "guest_id": app.guest_id,
                "rating": app.rating
            } for app in episode.appearances
        ]
    }

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return {"message": "Episode deleted successfully"}, 200
