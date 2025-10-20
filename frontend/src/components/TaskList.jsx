import React from 'react';

const TaskList = ({ tasks, loading, error, onRefresh }) => {
  const formatDate = (dateString) => {
    if (!dateString) return 'Дата не указана';
    
    try {
      const date = new Date(dateString);
      return date.toLocaleString('ru-RU', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    } catch {
      return 'Неверный формат даты';
    }
  };

  if (loading) {
    return (
      <div className="card">
        <div className="loading">Загрузка задач...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="card">
        <div className="error">
          Ошибка: {error}
          <button onClick={onRefresh} className="btn btn-secondary" style={{marginLeft: '10px'}}>
            Повторить
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="card">
      <div className="tasks-header">
        <h2>📋 Список задач ({tasks.length})</h2>
        <button onClick={onRefresh} className="btn btn-secondary">
          🔄 Обновить
        </button>
      </div>

      <div className="tasks-list">
        {tasks.length === 0 ? (
          <div className="empty-state">
            <p>Задачи отсутствуют</p>
            <p>Создайте первую задачу!</p>
          </div>
        ) : (
          tasks.map((task) => (
            <div key={task.id} className="task-item">
              <div className="task-header">
                <h3 className="task-title">{task.name}</h3>
                <span className="task-id">ID: {task.id}</span>
              </div>
              
              {task.description && (
                <p className="task-description">{task.description}</p>
              )}
              
              {task.created_at && (
                <p className="task-date">
                  📅 Создано: {formatDate(task.created_at)}
                </p>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default TaskList;