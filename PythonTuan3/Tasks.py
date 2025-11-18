from flask import Flask, jsonify, abort, request
from typing import List, Dict, Any
from db import get_db_connection

app = Flask(__name__)

# ============================================================================
# POST /api/tasks: Create a new task
# ============================================================================

def create_task(title: str, description: str = None, status: str = 'pending') -> Dict[str, Any]:
    """
    Insert a new task into the database
    
    Args:
        title (str): The title of the task (required)
        description (str, optional): The description of the task. Defaults to None.
        status (str, optional): The status of the task. Defaults to 'pending'.
        
    Returns:
        Dict[str, Any]: The created task with its ID or None if creation failed
    """
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO Tasks (title, description, status)
                VALUES (%s, %s, %s)
                RETURNING id, title, description, status
            """, (title, description, status))
            
            task = cur.fetchone()
            conn.commit()
            
            if task:
                columns = [desc[0] for desc in cur.description]
                return dict(zip(columns, task))
            return None
    except Exception as e:
        print(f"Error creating task: {e}")
        if conn:
            conn.rollback()
        return None
    finally:
        if conn:
            conn.close()

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    
    # Validate required fields
    if not data or 'title' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Title is required'
        }), 400
    
    # Create the task
    title = data.get('title')
    description = data.get('description')
    status = data.get('status', 'pending')
    
    task = create_task(title, description, status)
    
    if task is None:
        return jsonify({
            'status': 'error',
            'message': 'Failed to create task'
        }), 500
        
    return jsonify({
        'status': 'success',
        'data': task
    }), 201


# ============================================================================
# GET /api/tasks: List all tasks
# ============================================================================

def get_all_tasks() -> List[Dict[str, Any]]:
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("""
                select * from Tasks
            """)
            columns = [desc[0] for desc in cur.description]
            tasks = [dict(zip(columns, row)) for row in cur.fetchall()]
            return tasks
    except Exception as e:
        print(f"Error fetching tasks: {e}")
        return []
    finally:
        if conn:
            conn.close()

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = get_all_tasks()
    return jsonify({
        'status': 'success',
        'data': tasks,
        'count': len(tasks)
    })


# ============================================================================
# GET /api/tasks/{id}: Retrieve a specific task
# ============================================================================

def get_task_by_id(task_id: int) -> Dict[str, Any]:
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM Tasks WHERE id = %s
            """, (task_id,))
            task = cur.fetchone()
            if task is None:
                return None
            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, task))
    except Exception as e:
        print(f"Error fetching task {task_id}: {e}")
        return None
    finally:
        if conn:
            conn.close()

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = get_task_by_id(task_id)
    if task is None:
        return jsonify({
            'status': 'error',
            'message': 'Task not found'
        }), 404
    return jsonify({
        'status': 'success',
        'data': task
    })


# ============================================================================
# PUT /api/tasks/{id}: Update a task
# ============================================================================

def update_task(task_id: int, title: str = None, description: str = None, status: str = None) -> Dict[str, Any]:
    """
    Update a task in the database
    
    Args:
        task_id (int): The ID of the task to update
        title (str, optional): The new title of the task
        description (str, optional): The new description of the task
        status (str, optional): The new status of the task
        
    Returns:
        Dict[str, Any]: The updated task or None if update failed
    """
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            # Build the UPDATE query dynamically based on provided fields
            updates = []
            values = []
            
            if title is not None:
                updates.append("title = %s")
                values.append(title)
            if description is not None:
                updates.append("description = %s")
                values.append(description)
            if status is not None:
                updates.append("status = %s")
                values.append(status)
            
            if not updates:
                # No fields to update
                return get_task_by_id(task_id)
            
            values.append(task_id)
            query = f"""
                UPDATE Tasks 
                SET {', '.join(updates)}
                WHERE id = %s
                RETURNING id, title, description, status
            """
            
            cur.execute(query, values)
            task = cur.fetchone()
            conn.commit()
            
            if task:
                columns = [desc[0] for desc in cur.description]
                return dict(zip(columns, task))
            return None
    except Exception as e:
        print(f"Error updating task {task_id}: {e}")
        if conn:
            conn.rollback()
        return None
    finally:
        if conn:
            conn.close()

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task_route(task_id):
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

    # Lấy dữ liệu từ request
    title = data.get('title')
    description = data.get('description')
    status = data.get('status')

    # Gọi hàm logic 'update_task'
    updated_task = update_task(task_id, title, description, status)

    if updated_task is None:
        return jsonify({
            'status': 'error',
            'message': 'Task not found or failed to update'
        }), 404

    return jsonify({
        'status': 'success',
        'data': updated_task
    }), 200


# ============================================================================
# DELETE /api/tasks/{id}: Delete a task
# ============================================================================

def delete_task(task_id: int) -> bool:
    """
    Delete a task from the database by its ID

    Args:
        task_id (int): The ID of the task to delete

    Returns:
        bool: True if the task was deleted, False otherwise
    """
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM Tasks 
                WHERE id = %s
                RETURNING id
            """, (task_id,))

            deleted = cur.fetchone() is not None
            conn.commit()
            return deleted
    except Exception as e:
        print(f"Error deleting task {task_id}: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    """
    Delete a task by its ID

    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID of the task to delete
    responses:
      200:
        description: Task deleted successfully
        schema:
          type: object
          properties:
            status:
              type: string
              example: success
            message:
              type: string
              example: Task deleted successfully
      404:
        description: Task not found
        schema:
          type: object
          properties:
            status:
              type: string
              example: error
            message:
              type: string
              example: Task not found
    """
    if delete_task(task_id):
        return jsonify({
            'status': 'success',
            'message': 'Task deleted successfully'
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Task not found'
        }), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
