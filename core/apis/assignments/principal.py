from flask import Blueprint, jsonify, request
from core import db
from core.models import Assignment, Teacher
from sqlalchemy.exc import IntegrityError

principal_bp = Blueprint('principal_bp', __name__)

@principal_bp.route('/assignments', methods=['GET'])
def get_principal_assignments():
    assignments = Assignment.query.filter(Assignment.state.in_(["SUBMITTED", "GRADED"])).all()
    return jsonify({'data': [assignment.to_dict() for assignment in assignments]})

@principal_bp.route('/teachers', methods=['GET'])
def get_principal_teachers():
    teachers = Teacher.query.all()
    return jsonify({'data': [teacher.to_dict() for teacher in teachers]})

@principal_bp.route('/assignments/grade', methods=['POST'])
def principal_grade_assignment():
    data = request.json
    assignment = Assignment.query.filter_by(id=data['id']).first()
    if assignment and assignment.state == "GRADED":
        assignment.grade = data['grade']
        db.session.commit()
        return jsonify({"data": assignment.to_dict()}), 200
    return jsonify({"error": "Assignment not found or not re-gradable"}), 404
