from flask import Blueprint, jsonify, request
from app.models.job import JobApplication
from app import db

bp = Blueprint('jobs', __name__)

@bp.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = JobApplication.query.all()
    return jsonify([{
        'id': job.id,
        'company': job.company,
        'position': job.position,
        'status': job.status
    } for job in jobs])

@bp.route('/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    job = JobApplication(
        company=data['company'],
        position=data['position'],
        status=data.get('status', 'Applied'),
        source=data.get('source'),
        job_description=data.get('description')
    )
    db.session.add(job)
    db.session.commit()
    return jsonify({'message': 'Job application created'}), 201