import React, { useState, useEffect } from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import { taskService } from './services/api';
import './index.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

// В App.jsx в функции fetchTasks
const fetchTasks = async () => {
  setLoading(true);
  setError(null);
  
  try {
    const tasksData = await taskService.getTasks();
    setTasks(tasksData || []);
  } catch (err) {
    console.error('App: Ошибка:', err);
    setError(err.message);
  } finally {
    setLoading(false);
  }
};

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleTaskCreated = (newTask) => {
    fetchTasks();
  };

  return (
    <div className="container">
      <header className="header">
        <h1>Менеджер задач</h1>
        <p>Управляйте своими задачами легко и просто</p>
      </header>

      <div className="main-content">
        <TaskForm onTaskCreated={handleTaskCreated} />
        <TaskList 
          tasks={tasks} 
          loading={loading}
          error={error}
          onRefresh={fetchTasks}
        />
      </div>
    </div>
  );
}

export default App;