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

def create_task(title: str, description: str = None, status: str = 'pending') -> Dict[str, Any]:
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


def update_task(task_id: int, title: str = None, description: str = None, status: str = None) -> Dict[str, Any]:
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
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

def delete_task(task_id: int) -> bool:
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

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Title is required'
        }), 400

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

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task_route(task_id):
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

    title = data.get('title')
    description = data.get('description')
    status = data.get('status')

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

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_route(task_id):
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
