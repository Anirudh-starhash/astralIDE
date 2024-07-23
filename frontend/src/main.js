import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

const instance=axios.create({
  baseURL:"http://127.0.0.1:5000",
});

const app = createApp(App)



app.config.globalProperties.$http=instance;


app.use(router)

app.mount('#app')
