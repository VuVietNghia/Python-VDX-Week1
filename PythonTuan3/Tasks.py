from flask import Flask, jsonify, abort, request
from typing import List, Dict, Any
from db import get_db_connection

app = Flask(__name__)

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

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = get_all_tasks()
    return jsonify({
        'status': 'success',
        'data': tasks,
        'count': len(tasks)
    })

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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
