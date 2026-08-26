<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { listArticles, getLessonNumber } from '../../content/notes/registry.js'

const route = useRoute()

const filterSeries = computed(() => {
  const s = route.query.series
  if (!s || s === 'all') return null
  return String(s)
})

const articles = computed(() => {
  if (filterSeries.value) return listArticles({ series: filterSeries.value })
  return listArticles()
})

const firstArticle = computed(() => articles.value[0] ?? null)

const seriesTitle = computed(() => {
  if (filterSeries.value === 'Python 从零') return '🐍 Python 从零'
  if (filterSeries.value === 'Python 生态') return '🗺️ Python 生态'
  if (filterSeries.value) return filterSeries.value
  return '📚 全部笔记'
})
</script>

<template>
  <div class="notes-index">
    <header class="notes-index__hero">
      <h1 class="notes-index__title">{{ seriesTitle }}</h1>
      <p v-if="filterSeries === 'Python 从零'" class="notes-index__intro">
        ✨ 每次只学一小块：跑通、改一改、真正理解，再进入下一课。
        左侧目录可跳转任意章节；建议从第 1 课按顺序读。
      </p>
      <p v-else class="notes-index__intro">
        🗂️ 学习记录与部署笔记。选左侧章节开始阅读，或浏览下方列表。
      </p>
      <router-link
        v-if="firstArticle"
        :to="`/notes/${firstArticle.slug}`"
        class="notes-index__cta"
      >
        {{ filterSeries ? '▶️ 从第 1 课开始' : '▶️ 开始阅读' }}
      </router-link>
      <p class="notes-index__count">📄 共 {{ articles.length }} 篇</p>
    </header>

    <section v-if="articles.length" class="notes-index__list-section" aria-label="文章列表">
      <h2 class="notes-index__list-heading">📋 目录</h2>
      <ul class="notes-index__list">
        <li v-for="item in articles" :key="item.slug" class="notes-index__item">
          <router-link :to="`/notes/${item.slug}`" class="notes-index__link">
            <span v-if="getLessonNumber(item.title)" class="notes-index__no">
              {{ String(getLessonNumber(item.title)).padStart(2, '0') }}
            </span>
            <div class="notes-index__body">
              <h3 class="notes-index__item-title">{{ item.title }}</h3>
              <p class="notes-index__summary">{{ item.summary }}</p>
              <div class="notes-index__meta">
                <time>{{ item.updated }}</time>
                <span v-for="tag in item.tags" :key="tag" class="notes-index__tag">{{ tag }}</span>
              </div>
            </div>
          </router-link>
        </li>
      </ul>
    </section>

    <p v-else class="notes-index__empty">📭 这个分类还没有文章。</p>
  </div>
</template>

<style scoped>
.notes-index__hero {
  margin-bottom: 2.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--notes-border);
}

.notes-index__title {
  font-size: clamp(1.5rem, 3vw, 1.85rem);
  font-weight: 700;
  line-height: 1.3;
  color: var(--notes-text);
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}

.notes-index__intro {
  max-width: 42rem;
  font-size: 16px;
  line-height: 1.75;
  color: var(--notes-text-secondary);
  margin-bottom: 1.25rem;
}

.notes-index__cta {
  display: inline-block;
  padding: 8px 16px;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  background: var(--notes-brand);
  border-radius: 8px;
}

.notes-index__cta:hover {
  text-decoration: none;
  background: var(--notes-brand-dark);
  color: #fff;
}

.notes-index__count {
  margin-top: 1rem;
  font-size: 13px;
  color: var(--notes-text-muted);
}

.notes-index__list-heading {
  font-size: 14px;
  font-weight: 600;
  color: var(--notes-text-muted);
  margin-bottom: 1rem;
}

.notes-index__list {
  list-style: none;
  margin: 0;
  padding: 0;
  background: var(--notes-surface);
  border: 1px solid var(--notes-border);
  border-radius: 12px;
  overflow: hidden;
}

.notes-index__item {
  border-bottom: 1px solid var(--notes-border);
}

.notes-index__item:last-child {
  border-bottom: none;
}

.notes-index__link {
  display: flex;
  gap: 1.25rem;
  padding: 1.25rem;
  color: inherit;
  transition: background 0.12s;
}

.notes-index__link:hover {
  text-decoration: none;
  background: var(--notes-brand-soft);
}

.notes-index__no {
  flex: 0 0 auto;
  font-family: var(--font-mono);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--notes-brand);
  line-height: 1.3;
  min-width: 2.5rem;
}

.notes-index__body {
  flex: 1;
  min-width: 0;
}

.notes-index__item-title {
  font-size: 16px;
  font-weight: 600;
  line-height: 1.4;
  color: var(--notes-text);
  margin-bottom: 0.4rem;
}

.notes-index__summary {
  font-size: 14px;
  line-height: 1.65;
  color: var(--notes-text-secondary);
  margin-bottom: 0.65rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.notes-index__meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.65rem;
  font-size: 12px;
  color: var(--notes-text-muted);
}

.notes-index__tag {
  padding: 2px 8px;
  background: var(--notes-canvas);
  color: var(--notes-text-secondary);
  border-radius: 999px;
}

.notes-index__empty {
  color: var(--notes-text-muted);
  font-size: 14px;
}

@media (max-width: 600px) {
  .notes-index__link {
    gap: 0.75rem;
    padding: 1rem;
  }

  .notes-index__no {
    font-size: 1rem;
    min-width: 2rem;
  }
}
</style>
