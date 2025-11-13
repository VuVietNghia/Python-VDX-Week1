from flask import Flask, jsonify
from typing import List, Dict, Any
from db import get_db_connection

app = Flask(__name__)

def get_all_tasks() -> List[Dict[str, Any]]:
    """
    Retrieve all tasks from the Tasks table.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries, where each dictionary represents a task
    """
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            # Query to select all tasks
            cur.execute("""
                SELECT id, title, description, status 
                FROM Tasks
                ORDER BY id
            """)
            
            # Get column names from cursor description
            columns = [desc[0] for desc in cur.description]
            
            # Create a list of dictionaries where each dictionary represents a task
            tasks = [dict(zip(columns, row)) for row in cur.fetchall()]
            
            return tasks
            
    except Exception as e:
        print(f"Error fetching tasks: {e}")
        return []
        
    finally:
        if conn is not None:
            conn.close()

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """
    API endpoint to get all tasks
    Returns JSON response with all tasks
    """
    tasks = get_all_tasks()
    return jsonify({
        'status': 'success',
        'data': tasks,
        'count': len(tasks)
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
