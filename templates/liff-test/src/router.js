import { createWebHistory, createRouter } from 'vue-router';

import Test1 from './views/Test1.vue';
import Test2 from './views/Test2.vue';


const routes = [
  {
    path: '/',
    name: 'Test2',
    component: Test2, 
  },
  {
    path: '/test1',
    name: 'Test1',
    component: Test1,
  },
  {
    path: '/test2',
    name: 'Test2',
    component: Test2, 
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;