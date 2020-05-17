import Vue from "vue"
import VueRouter from 'vue-router'


import Exam1 from "./components/Exam1.vue"
import Exam2 from "./components/Exam2.vue"
import Exam3 from "./components/Exam3.vue"
import Exam4 from "./components/Exam4.vue"

Vue.use(VueRouter)

const routes = [{
    path: '/exam1',
    component: Exam1
},{
    path: '/exam2',
    component: Exam2
},{
    path: '/exam3',
    component: Exam3
},{
    path: '/exam4',
    component: Exam4
},
//重定向
	{
		path:'/',
		redirect:'/exam1'
	}
]
var router = new VueRouter({
    routes
})
export default router;