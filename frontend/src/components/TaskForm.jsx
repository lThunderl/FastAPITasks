import React, { useState } from 'react';
import { taskService } from '../services/api';

const TaskForm = ({ onTaskCreated }) => {
  const [formData, setFormData] = useState({
    name: '',
    description: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.name?.trim()) {
      setError('Пожалуйста, введите название задачи');
      return;
    }

    setLoading(true);
    setError(null);
    
    try {
      const result = await taskService.createTask(formData);
      onTaskCreated(result);
      setFormData({ 
        name: '', 
        description: '' 
      });
    } catch (err) {
      console.error('Error creating task:', err);
      setError('Ошибка при создании задачи: ' + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value || '' 
    }));
    if (error) setError(null);
  };

  return (
    <div className="card">
      <h2>➕ Новая задача</h2>
      
      {error && (
        <div className="error" style={{marginBottom: '15px'}}>
          {error}
        </div>
      )}
      
      <form onSubmit={handleSubmit} className="task-form">
        <div className="form-group">
          <label htmlFor="name">Название задачи:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name || ''}
            onChange={handleChange}
            placeholder="Введите название задачи"
            disabled={loading}
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="description">Описание:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description || ''} 
            onChange={handleChange}
            placeholder="Введите описание задачи (необязательно)"
            disabled={loading}
          />
        </div>
        
        <button 
          type="submit" 
          className="btn btn-primary"
          disabled={loading || !formData.name?.trim()}
        >
          {loading ? 'Создание...' : 'Создать задачу'}
        </button>
      </form>
    </div>
  );
};

export default TaskForm;