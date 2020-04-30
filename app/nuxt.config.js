export default {
  mode: 'spa',
  head: {
    title: 'Amera',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  loading: { color: '#ffa010', height: '5px' },
  css: ['@/assets/stylesheets/main.scss'],
  plugins: [],
  buildModules: ['@nuxtjs/eslint-module'],
  modules: ['@nuxtjs/axios'],
  axios: {},
  build: {
    extend(config, ctx) {}
  },
  generate: { dir: '../amera/built' }
}
