/* ============================================================
   composables/useToast.js — 全局 toast 通知
   模块级单例状态：任何组件 push 的 toast 汇入同一列表，
   ToastContainer.vue 统一渲染。每条自动计时移除（error 5s，
   其余 3.5s），可点击手动关闭。类型：info | success | warning | error。
   ============================================================ */
import { reactive } from 'vue'

const state = reactive({ toasts: [] })
let seq = 0

function remove (id) {
  const i = state.toasts.findIndex(t => t.id === id)
  if (i >= 0) state.toasts.splice(i, 1)
}

function push (message, type = 'info', duration = 3500) {
  const id = ++seq
  state.toasts.push({ id, type, message })
  if (duration > 0) {
    setTimeout(() => remove(id), duration)
  }
  return id
}

export function useToast () {
  return {
    toasts: state.toasts,
    remove,
    push,
    info: m => push(m, 'info'),
    success: m => push(m, 'success'),
    warning: m => push(m, 'warning'),
    error: m => push(m, 'error', 5000)
  }
}
