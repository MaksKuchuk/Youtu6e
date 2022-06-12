<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-14">
    <div class="h-24" :style="{backgroundImage: `url(${require('../assets/image.jpg')})`}"></div>
  </main>
</template>

<script>
import HeaderView from './HeaderView.vue';
import AsideView from './AsideView.vue';

export default {
  components: {
    HeaderView,
    AsideView,
  },
};
</script>

<style>

</style>
