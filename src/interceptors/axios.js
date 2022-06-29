import axios from 'axios'

let refresh = false

axios.interceptors.response.use(resp => resp, async error => {
    if (error.response.status === 401 && !refresh) {
        refresh = true

        const {status, data} = axios.post('http://localhost:8000/api/v1/auth/token/refresh/', {}, {
            withCredentials: true
        })

        if (status === 200) {
            localStorage.setItem('authToken', data.token)
            return axios(error.config)
        }
    }
    refresh = false
    return error
})