import axios from 'axios';

const API_BASE_URL = "http://localhost:80"

const api = axios.create({
    baseURL: API_BASE_URL,
})

export const taskService = {
    async getTasks() {
        const response = await api.get('/tasks');
        return response.data;
    },

    async createTask(taskData){
        const response = await api.post('/tasks', taskData);
        return response.data
    }
}

export default api;