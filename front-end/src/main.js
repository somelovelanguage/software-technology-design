import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import router from "./router.js"

Vue.prototype.$http=axios

Vue.config.productionTip = false
Vue.use(ElementUI)



new Vue({
	router,
  render: h => h(App),
}).$mount('#app')
