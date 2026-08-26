<script setup>
import { computed, shallowRef, watch } from 'vue'
import { useRoute } from 'vue-router'
import {
  getArticleBySlug,
  getAdjacentArticles,
  getLessonNumber
} from '../../content/notes/registry.js'

const route = useRoute()

const meta = computed(() => getArticleBySlug(route.params.slug))
const adjacent = computed(() => getAdjacentArticles(route.params.slug))
const lessonNo = computed(() => meta.value ? getLessonNumber(meta.value.title) : null)

const articleComp = shallowRef(null)
const loadError = shallowRef('')

watch(
  () => route.params.slug,
  async (slug) => {
    articleComp.value = null
    loadError.value = ''
    const item = getArticleBySlug(slug)
    if (!item) {
      loadError.value = '文章不存在'
      return
    }
    try {
      const mod = await item.component()
      articleComp.value = mod.default
    } catch (e) {
      loadError.value = e?.message || '加载失败'
    }
  },
  { immediate: true }
)
</script>

<template>
  <article class="article-view">
    <p v-if="loadError" class="article-view__error">❌ {{ loadError }}</p>

    <template v-else-if="meta">
      <header class="article-view__head">
        <p class="article-view__series">📁 {{ meta.series }}</p>
        <h1 class="article-view__title">
          <span v-if="lessonNo" class="article-view__lesson">📌 第 {{ lessonNo }} 课</span>
          {{ meta.title.replace(/^第\s*\d+\s*课[：:]\s*/, '') }}
        </h1>
        <p class="article-view__meta">
          <time>🗓️ {{ meta.updated }}</time>
          <span v-if="meta.tags?.length" class="article-view__tags">
            <span v-for="tag in meta.tags" :key="tag">🏷️ {{ tag }}</span>
          </span>
        </p>
      </header>

      <div class="article-view__body prose">
        <component :is="articleComp" v-if="articleComp" />
        <p v-else class="article-view__loading">⏳ 加载中…</p>
      </div>

      <nav v-if="adjacent.prev || adjacent.next" class="article-view__nav" aria-label="章节导航">
        <router-link
          v-if="adjacent.prev"
          :to="`/notes/${adjacent.prev.slug}`"
          class="article-view__nav-link article-view__nav-link--prev"
        >
          <span class="article-view__nav-label">⬅️ 上一课</span>
          <span class="article-view__nav-title">{{ adjacent.prev.title }}</span>
        </router-link>
        <router-link
          v-if="adjacent.next"
          :to="`/notes/${adjacent.next.slug}`"
          class="article-view__nav-link article-view__nav-link--next"
        >
          <span class="article-view__nav-label">下一课 ➡️</span>
          <span class="article-view__nav-title">{{ adjacent.next.title }}</span>
        </router-link>
      </nav>
    </template>
  </article>
</template>

<style scoped>
.article-view {
  max-width: 46rem;
  color: var(--notes-text);
}

.article-view__head {
  margin-bottom: 1.75rem;
  padding-bottom: 1.25rem;
  border-bottom: 1px solid var(--notes-border);
}

.article-view__series {
  font-size: 13px;
  font-weight: 600;
  color: var(--notes-brand);
  margin-bottom: 0.75rem;
}

.article-view__title {
  font-size: clamp(1.5rem, 3.5vw, 2rem);
  font-weight: 700;
  line-height: 1.35;
  color: var(--notes-text);
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}

.article-view__lesson {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: var(--notes-brand);
  margin-bottom: 0.35rem;
}

.article-view__meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem;
  font-size: 13px;
  color: var(--notes-text-muted);
}

.article-view__tags {
  display: flex;
  gap: 0.5rem;
}

.article-view__tags span {
  padding: 2px 8px;
  background: var(--notes-brand-soft);
  color: var(--notes-brand-dark);
  border-radius: 999px;
}

/* Vue Docs 风格正文 */
.prose {
  font-size: 16px;
  line-height: 1.75;
  color: var(--notes-text-secondary);
}

.prose :deep(h2) {
  margin: 2.25rem 0 1rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--notes-border);
  font-size: 1.35rem;
  font-weight: 700;
  line-height: 1.4;
  color: var(--notes-text);
  letter-spacing: -0.01em;
}

.prose :deep(h2:first-child) {
  border-top: none;
  padding-top: 0;
  margin-top: 0;
}

.prose :deep(h3) {
  margin: 1.75rem 0 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--notes-text);
}

.prose :deep(p),
.prose :deep(li) {
  font-size: 16px;
  line-height: 1.75;
  color: var(--notes-text-secondary);
}

.prose :deep(p + p) {
  margin-top: 1rem;
}

.prose :deep(strong) {
  color: var(--notes-text);
  font-weight: 600;
}

.prose :deep(a) {
  color: var(--notes-brand-dark);
  font-weight: 500;
  text-decoration: underline;
  text-underline-offset: 3px;
}

.prose :deep(ul),
.prose :deep(ol) {
  margin: 1rem 0;
  padding-left: 1.35rem;
  display: grid;
  gap: 0.4rem;
}

/* 行内代码 */
.prose :deep(:not(pre) > code) {
  font-family: var(--font-mono);
  font-size: 0.875em;
  color: var(--notes-inline-code-fg);
  background: var(--notes-inline-code-bg);
  border-radius: 4px;
  padding: 0.15em 0.4em;
  font-weight: 500;
}

/* 代码块：深色，从正文里跳出来 */
.prose :deep(pre) {
  margin: 1.25rem 0;
  padding: 1.1rem 1.25rem;
  background: var(--notes-code-bg);
  border: 1px solid #2e2e32;
  border-radius: 10px;
  overflow-x: auto;
  font-size: 13.5px;
  line-height: 1.7;
}

.prose :deep(pre code) {
  display: block;
  font-family: var(--font-mono);
  background: transparent !important;
  color: var(--notes-code-fg) !important;
  border: none;
  padding: 0;
  font-size: inherit;
  font-weight: 400;
  white-space: pre;
  line-height: inherit;
}

/* tip / warning 风格 callout */
.prose :deep(.callout) {
  margin: 1.25rem 0;
  padding: 0.9rem 1.1rem;
  border-radius: 8px;
  border: 1px solid transparent;
  border-left-width: 4px;
  background: var(--notes-canvas);
}

.prose :deep(.callout--principle) {
  background: var(--notes-tip-bg);
  border-color: color-mix(in srgb, var(--notes-brand) 22%, transparent);
  border-left-color: var(--notes-tip-border);
}

.prose :deep(.callout--pitfall) {
  background: var(--notes-warn-bg);
  border-color: color-mix(in srgb, var(--notes-warn-border) 28%, transparent);
  border-left-color: var(--notes-warn-border);
}

.prose :deep(.callout__label) {
  display: block;
  margin-bottom: 0.35rem;
  font-size: 13px;
  font-weight: 700;
  color: var(--notes-text);
}

.prose :deep(.callout--principle .callout__label) {
  color: var(--notes-brand-dark);
}

.prose :deep(.callout--principle .callout__label)::before {
  content: '💡 ';
}

.prose :deep(.callout--pitfall .callout__label) {
  color: #b8821a;
}

.prose :deep(.callout--pitfall .callout__label)::before {
  content: '⚠️ ';
}

.prose :deep(.callout p) {
  margin: 0;
  font-size: 15px;
  line-height: 1.7;
  color: var(--notes-text-secondary);
}

.article-view__nav {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 2.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--notes-border);
}

.article-view__nav-link {
  display: block;
  padding: 1rem 1.15rem;
  border: 1px solid var(--notes-border);
  border-radius: 10px;
  background: var(--notes-surface);
  color: inherit;
  transition: border-color 0.12s, background 0.12s;
}

.article-view__nav-link:hover {
  text-decoration: none;
  border-color: var(--notes-brand);
  background: var(--notes-brand-soft);
}

.article-view__nav-link--next {
  text-align: right;
}

.article-view__nav-label {
  display: block;
  font-size: 12px;
  color: var(--notes-text-muted);
  margin-bottom: 0.35rem;
}

.article-view__nav-title {
  display: block;
  font-size: 14px;
  font-weight: 600;
  line-height: 1.45;
  color: var(--notes-text);
}

.article-view__loading,
.article-view__error {
  font-size: 14px;
  color: var(--notes-text-muted);
}

.article-view__error {
  color: var(--color-error);
}

@media (max-width: 600px) {
  .article-view__nav {
    grid-template-columns: 1fr;
  }

  .article-view__nav-link--next {
    text-align: left;
  }
}
</style>
