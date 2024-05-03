import { createApp } from 'vue'
import App from './App.vue'
import { createStore } from 'vuex'
import axios from "axios";
import router from "@/router";

const store =  createStore({
    state: () => ({
        refresh: '',
        auth_via_VK: false,
        flights_filter: {
            page: 1,
            from: '',
            to: '',
            set: true
        }
    }),
    actions: {
        async get_flight(_, id) {
            try {
                return (await axios.get('http://127.0.0.1:8000/api/flights/' + id + '/')).data;
            } catch (e) {
                console.log(e)
            }
        },
        set_filter({commit}, filter) {
            commit('SET_FILTER', filter)
        },
        async get_flights(_, filter) {
            return (await axios.get('http://127.0.0.1:8000/api/flights/by/', {params: filter})).data;
        },
        async get_tickets(_, flight_id) {
            try {
                return (await axios.get('http://127.0.0.1:8000/api/tickets/by/',
                    {params: {'flight_id': flight_id}})).data;
            } catch (e) {
                console.log(e)
            }
        },
        async get_bookings(_, user_id) {
            try {
                return (await axios.get('http://127.0.0.1:8000/api/bookings/by/',
                    {params: {'user_id': user_id}})).data;
            } catch (e) {
                console.log(e)
            }
        },
        async user_register({dispatch}, data) {
            try {
                await axios.post('http://127.0.0.1:8000/auth/users/', data).then(async () => {
                        await dispatch("auth_user", {
                            'username': data.username,
                            'password': data.password
                        })
                    })
            } catch (e) {
                return false;
            }
            return true
        },
        async edit_username(_, data) {
            try {
                await axios.post('http://127.0.0.1:8000/auth/users/set_username/', data)
            } catch (e) {
                return false
            }
            return true
        },
        async edit_email(_, data) {
            try {
                return (await axios.post('http://127.0.0.1:8000/auth/user/set_email/', data)).data.result
            } catch (e) {
                return 'ERROR'
            }
        },
        async edit_password(_, data) {
            try {
                await axios.post('http://127.0.0.1:8000/auth/users/set_password/', data)
            } catch (e) {
                console.log(e)
                return false
            }
            return true
        },
        async auth_user({commit}, data) {
            try {
                await axios.post('http://127.0.0.1:8000/auth/jwt/create/', data).then(
                    (response) => {
                        commit('AUTH_ACCOUNT', response.data);
                    })
            } catch (e) {
                return false;
            }
            return true
        },
        exit_from_account({commit}) {
            commit('EXIT_ACCOUNT')
        },
        async upload_user_image(_, data) {
            return (await axios.post('http://127.0.0.1:8000/auth/user/image/' + data.user_id, data.file)).data.result;
        },
        async get_account_data() {
            return (await axios.get('http://127.0.0.1:8000/auth/users/me/')).data;
        },
        set_auth_via_VK({commit}, status) {
            commit('AUTH_VIA_VK', status)
        },
        async auth_via_VK(_, data) {
            return (await axios.post('http://127.0.0.1:8000/auth/user/via/vk', data)).data.result;
        },
        async get_recovering_code(_, email) {
            return (await axios.get('http://127.0.0.1:8000/auth/user/recovering_password/',
                {'params': {'email': email}})).data.result;
        },
        async set_recovered_password(_, data) {
            return (await axios.post('http://127.0.0.1:8000/auth/user/recovering_password/',
                {'headers': data})).data.result;
        },
        async refresh_token({commit, getters}) {
            let data = (await axios.post('http://127.0.0.1:8000/auth/jwt/refresh/',
                {'headers': getters.get_refresh()})).data;
            commit('AUTH_ACCOUNT', data)
        }
    },
    mutations: {
        EXIT_ACCOUNT(state) {
            state.refresh = '';
            axios.defaults.headers.common['Authorization'] = '';
        },
        AUTH_ACCOUNT(state, data) {
            state.refresh = data.refresh;
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + data.access;
        },
        AUTH_VIA_VK(state, status) {
            state.auth_via_VK = status
        },
        SET_FILTER(state, filter) {
            state.flights_filter = filter
        }
    },
    getters: {
        is_auth(state) {
            return state.refresh;
        },
        is_auth_via_VK(state) {
            return state.auth_via_VK
        },
        get_filter(state) {
            return state.flights_filter
        },
        get_refresh(state) {
            return state.refresh
        }
    }
})

createApp(App).use(store).use(router).mount('#app')
