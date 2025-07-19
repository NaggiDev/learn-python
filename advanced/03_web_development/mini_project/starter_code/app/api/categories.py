"""
Task Management API - Categories Routes

This module contains category-related API endpoints.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.category import Category
from app.utils.validation import validate_required_fields, validate_hex_color
from app.utils.auth import admin_required

# Create blueprint
categories_bp = Blueprint('categories', __name__)


@categories_bp.route('', methods=['GET'])
@jwt_required()
def get_categories():
    """Get all categories."""
    try:
        categories = Category.get_all_active()
        
        return jsonify({
            'categories': [category.to_dict() for category in categories],
            'total': len(categories)
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to get categories', 'details': str(e)}), 500


@categories_bp.route('/<int:category_id>', methods=['GET'])
@jwt_required()
def get_category(category_id):
    """Get specific category."""
    try:
        category = Category.query.get_or_404(category_id)
        
        return jsonify({
            'category': category.to_dict(include_tasks=True)
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to get category', 'details': str(e)}), 500


@categories_bp.route('', methods=['POST'])
@admin_required
def create_category():
    """Create new category (Admin only)."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['name']
        validation_errors = validate_required_fields(data, required_fields)
        
        if validation_errors:
            return jsonify({'error': 'Validation failed', 'details': validation_errors}), 422
        
        # Validate color if provided
        if 'color' in data and not validate_hex_color(data['color']):
            return jsonify({'error': 'Invalid color format. Use hex format like #FF0000'}), 422
        
        # Check if category already exists
        if Category.find_by_name(data['name']):
            return jsonify({'error': 'Category already exists'}), 409
        
        # Create category
        category = Category(
            name=data['name'].strip(),
            description=data.get('description', '').strip(),
            color=data.get('color', '#6c757d')
        )
        
        db.session.add(category)
        db.session.commit()
        
        return jsonify({
            'message': 'Category created successfully',
            'category': category.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create category', 'details': str(e)}), 500


@categories_bp.route('/<int:category_id>', methods=['PUT'])
@admin_required
def update_category(category_id):
    """Update category (Admin only)."""
    try:
        category = Category.query.get_or_404(category_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate color if provided
        if 'color' in data and not validate_hex_color(data['color']):
            return jsonify({'error': 'Invalid color format. Use hex format like #FF0000'}), 422
        
        # Check for name conflicts
        if 'name' in data:
            existing = Category.find_by_name(data['name'])
            if existing and existing.id != category_id:
                return jsonify({'error': 'Category name already exists'}), 409
            category.name = data['name'].strip()
        
        if 'description' in data:
            category.description = data['description'].strip()
        
        if 'color' in data:
            category.color = data['color']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Category updated successfully',
            'category': category.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update category', 'details': str(e)}), 500


@categories_bp.route('/<int:category_id>', methods=['DELETE'])
@admin_required
def delete_category(category_id):
    """Delete category (Admin only)."""
    try:
        category = Category.query.get_or_404(category_id)
        
        # Check if category has tasks
        if category.tasks.count() > 0:
            return jsonify({
                'error': 'Cannot delete category with existing tasks',
                'task_count': category.tasks.count()
            }), 409
        
        db.session.delete(category)
        db.session.commit()
        
        return jsonify({
            'message': 'Category deleted successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete category', 'details': str(e)}), 500