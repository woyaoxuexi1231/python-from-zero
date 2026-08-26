import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  { path: '/', redirect: '/notes' },
  {
    path: '/notes',
    component: () => import('../views/notes/NotesLayout.vue'),
    children: [
      { path: '', name: 'NotesIndex', component: () => import('../views/notes/NotesIndex.vue') },
      { path: ':slug', name: 'NotesArticle', component: () => import('../views/notes/ArticleView.vue') }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(import.meta.env.VITE_APP_BASE),
  routes
})

export default router
