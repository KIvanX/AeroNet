import Main_page from "@/pages/Main_page";
import {createRouter, createWebHistory} from "vue-router"
import About_page from "@/pages/about_page";
import registration_page from "@/pages/registration_page";
import authorization_page from "@/pages/authorization_page";
import flight_page from "@/pages/flight_page";
import account_page from "@/pages/account_page";
import flights_date_page from "@/pages/flights_date_page";
import recovering_password_page from "@/pages/recovering_password_page";
import history_page from "@/pages/history_page";
import ticket_page from "@/pages/ticket_page";

const routes = [
    {
        path: '/',
        component: Main_page
    },
    {
        path: '/about',
        component: About_page
    },
    {
        path: '/authorization',
        component: authorization_page
    },
    {
        path: '/registration',
        component: registration_page
    },
    {
        path: '/flights_date/:flight_id',
        component: flights_date_page,
        props: true,
    },
    {
        path: '/flights/:flight_id',
        component: flight_page,
        props: true,
    },
    {
        path: '/account',
        component: account_page,
    },
    {
        path: '/recovering_password',
        component: recovering_password_page,
    },
    {
        path: '/history',
        component: history_page,
    },
    {
        path: '/ticket/:ticket_id',
        component: ticket_page,
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;
