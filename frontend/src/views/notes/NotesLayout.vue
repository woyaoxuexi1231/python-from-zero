<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import {
  noteSeries,
  noteArticles,
  listArticles,
  getArticleBySlug,
  getLessonNumber
} from '../../content/notes/registry.js'

const route = useRoute()

const isArticle = computed(() => route.name === 'NotesArticle')
const activeSlug = computed(() => (isArticle.value ? String(route.params.slug) : ''))

const filterSeries = computed(() => {
  if (isArticle.value) {
    return getArticleBySlug(route.params.slug)?.series ?? null
  }
  const s = route.query.series
  if (!s || s === 'all') return null
  return String(s)
})

const sidebarArticles = computed(() => {
  if (filterSeries.value) return listArticles({ series: filterSeries.value })
  return listArticles()
})

const seriesGroups = computed(() => {
  if (filterSeries.value) return []
  const map = new Map()
  for (const article of noteArticles) {
    if (!map.has(article.series)) map.set(article.series, [])
    map.get(article.series).push(article)
  }
  return [...map.entries()].map(([name, articles]) => ({ name, articles }))
})
</script>

<template>
  <section class="notes-shell">
    <aside class="notes-sidebar" aria-label="笔记导航">
      <div class="notes-sidebar__head">
        <router-link to="/notes" class="notes-sidebar__brand">📝 学习笔记</router-link>
        <p class="notes-sidebar__desc">📖 教程与随笔，按章阅读。</p>
      </div>

      <nav class="notes-sidebar__series" aria-label="系列分类">
        <router-link
          v-for="item in noteSeries"
          :key="item.id"
          :to="item.id === 'all' ? { path: '/notes' } : { path: '/notes', query: { series: item.id } }"
          class="notes-sidebar__series-link"
          :class="{
            'notes-sidebar__series-link--active':
              filterSeries === item.id ||
              (item.id === 'all' && !filterSeries && !isArticle)
          }"
        >
          {{ item.label }}
        </router-link>
      </nav>

      <div v-if="filterSeries" class="notes-sidebar__chapters">
        <p class="notes-sidebar__chapters-label">{{ filterSeries }}</p>
        <ol class="notes-sidebar__chapter-list">
          <li
            v-for="item in sidebarArticles"
            :key="item.slug"
            class="notes-sidebar__chapter-item"
          >
            <router-link
              :to="`/notes/${item.slug}`"
              class="notes-sidebar__chapter-link"
              :class="{ 'notes-sidebar__chapter-link--active': activeSlug === item.slug }"
            >
              <span v-if="getLessonNumber(item.title)" class="notes-sidebar__chapter-no">
                {{ getLessonNumber(item.title) }}
              </span>
              <span class="notes-sidebar__chapter-title">{{ item.title }}</span>
            </router-link>
          </li>
        </ol>
      </div>

      <div v-else class="notes-sidebar__groups">
        <div v-for="group in seriesGroups" :key="group.name" class="notes-sidebar__group">
          <p class="notes-sidebar__chapters-label">{{ group.name }}</p>
          <ol class="notes-sidebar__chapter-list">
            <li
              v-for="item in group.articles"
              :key="item.slug"
              class="notes-sidebar__chapter-item"
            >
              <router-link
                :to="`/notes/${item.slug}`"
                class="notes-sidebar__chapter-link"
                :class="{ 'notes-sidebar__chapter-link--active': activeSlug === item.slug }"
              >
                <span v-if="getLessonNumber(item.title)" class="notes-sidebar__chapter-no">
                  {{ getLessonNumber(item.title) }}
                </span>
                <span class="notes-sidebar__chapter-title">{{ item.title }}</span>
              </router-link>
            </li>
          </ol>
        </div>
      </div>
    </aside>

    <div class="notes-main">
      <router-view />
    </div>
  </section>
</template>

<style scoped>
.notes-shell {
  display: grid;
  grid-template-columns: minmax(220px, 280px) minmax(0, 1fr);
  gap: var(--space-8);
  align-items: start;
  padding-top: var(--space-6);
  padding-bottom: var(--space-8);
  color: var(--notes-text);
}

.notes-sidebar {
  position: sticky;
  top: calc(var(--nav-height) + var(--space-4));
  max-height: calc(100vh - var(--nav-height) - var(--space-8));
  overflow: auto;
  padding: var(--space-4);
  border: 1px solid var(--notes-border);
  border-radius: 12px;
  background: var(--notes-surface);
}

.notes-sidebar__head {
  margin-bottom: var(--space-5);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--notes-border);
}

.notes-sidebar__brand {
  display: block;
  font-size: var(--font-md);
  font-weight: var(--weight-semibold);
  color: var(--notes-text);
  margin-bottom: var(--space-2);
}

.notes-sidebar__brand:hover {
  text-decoration: none;
  color: var(--notes-brand);
}

.notes-sidebar__desc {
  font-size: var(--font-xs);
  line-height: 1.6;
  color: var(--notes-text-muted);
}

.notes-sidebar__series {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  margin-bottom: var(--space-5);
}

.notes-sidebar__series-link {
  padding: 4px 10px;
  font-size: var(--font-xs);
  color: var(--notes-text-secondary);
  background: var(--notes-canvas);
  border-radius: 999px;
}

.notes-sidebar__series-link:hover {
  text-decoration: none;
  color: var(--notes-brand-dark);
  background: var(--notes-brand-soft);
}

.notes-sidebar__series-link--active {
  color: var(--notes-brand-dark);
  background: var(--notes-brand-soft);
  font-weight: var(--weight-semibold);
}

.notes-sidebar__chapters-label {
  font-size: var(--font-xs);
  font-weight: var(--weight-medium);
  color: var(--notes-text-muted);
  margin-bottom: var(--space-3);
}

.notes-sidebar__group + .notes-sidebar__group {
  margin-top: var(--space-5);
}

.notes-sidebar__chapter-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 2px;
}

.notes-sidebar__chapter-link {
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
  padding: 6px 8px;
  border-radius: 6px;
  color: var(--notes-text-secondary);
  font-size: var(--font-sm);
  line-height: 1.45;
}

.notes-sidebar__chapter-link:hover {
  text-decoration: none;
  background: var(--notes-canvas);
  color: var(--notes-text);
}

.notes-sidebar__chapter-link--active {
  background: var(--notes-brand-soft);
  color: var(--notes-brand-dark);
  font-weight: var(--weight-semibold);
}

.notes-sidebar__chapter-no {
  flex: 0 0 auto;
  min-width: 1.5em;
  font-family: var(--font-mono);
  font-size: var(--font-xs);
  color: var(--notes-text-muted);
}

.notes-sidebar__chapter-link--active .notes-sidebar__chapter-no {
  color: var(--notes-brand);
}

.notes-sidebar__chapter-title {
  flex: 1;
  min-width: 0;
}

.notes-main {
  min-width: 0;
}

@media (max-width: 900px) {
  .notes-shell {
    grid-template-columns: 1fr;
    gap: var(--space-5);
    padding-top: var(--space-4);
  }

  .notes-sidebar {
    position: static;
    max-height: none;
  }

  .notes-sidebar__chapter-list {
    display: flex;
    flex-wrap: nowrap;
    gap: var(--space-2);
    overflow-x: auto;
    padding-bottom: var(--space-2);
    -webkit-overflow-scrolling: touch;
  }

  .notes-sidebar__chapter-item {
    flex: 0 0 auto;
  }

  .notes-sidebar__chapter-link {
    flex-direction: column;
    align-items: center;
    gap: 2px;
    min-width: 3.5rem;
    padding: var(--space-2) var(--space-3);
    text-align: center;
    border: var(--border-weak);
    background: var(--color-surface);
  }

  .notes-sidebar__chapter-title {
    display: none;
  }

  .notes-sidebar__groups {
    display: flex;
    flex-wrap: nowrap;
    gap: var(--space-2);
    overflow-x: auto;
  }

  .notes-sidebar__group {
    flex: 0 0 auto;
  }

  .notes-sidebar__chapters-label {
    display: none;
  }
}
</style>
