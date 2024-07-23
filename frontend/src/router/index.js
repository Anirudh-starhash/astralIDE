import { createRouter, createWebHistory } from 'vue-router'
import editor_page from '@/components/editor_page.vue'
import code_header from '@/components/code_header.vue'
import index from '@/components/index.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/editor_page',
      name: 'editor_page',
      component: editor_page
    },
    {
      path: '/code_header',
      name: 'code_header',
      component: code_header
    },
    {
      path:'/',
      name:'index',
      component:index
    }
  ]
})

export default router
