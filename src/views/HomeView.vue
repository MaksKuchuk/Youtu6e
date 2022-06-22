<template>
  <HeaderView/>
  <AsideView/>
  <section class="pt-14 md:pl-24 xl:pl-64 w-full fixed bg-white bg-opacity-95 z-10">
    <div class="border-t border-b px-4 max-w-screen-2xl m-auto">
      <div class="py-3 flex space-x-3 overflow-auto text-sm whitespace-nowrap">
        <a href="#"
           class="px-3 py-1 transition bg-gray-500 border border-gray-600 rounded-full hover:bg-gray-500 text-white">Все</a>
        <a href="#"
           class="px-3 py-1 transition bg-gray-100 border border-gray-300 rounded-full hover:bg-gray-200">Машинки</a>
        <a href="#"
           class="px-3 py-1 transition bg-gray-100 border border-gray-300 rounded-full hover:bg-gray-200">Капибары</a>
      </div>
    </div>
  </section>
  <main class="md:ml-24 xl:ml-64 pt-32 px-5 pb-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 max-w-screen-2xl m-auto">
    <div v-for="video in videos" :key="video.id">
      <a href="#" class="mb-7 group">
          <div class="relative">
            <img :src="`${ video.preview}`" :alt="X" class="object-cover aspect-video">
            <span
              class="absolute opacity-100 group-hover:opacity-0 duration-500 bottom-0 right-0 bg-black text-white rounded-sm m-1 p-1 text-xs font-semibold">3:02</span>
          </div>
          <div class="flex item-start mt-3 group">
            <img src="https://i.pravatar.cc/1000" class="mr-3 rounded-full w-9 h-9" alt="">
            <div class="text-sm">
              <span class="font-semibold text-gray-800">{{ video.name }}</span>
              <div class="mt-1 flex items-center">
                <span>Channel name</span>
              </div>
              <div>
                <span>{{ video.views }}</span>
                &middot;
                <span>{{ format(video.uploadtime) }}</span>
              </div>
            </div>
            <button class="opacity-0 group-hover:opacity-100 mb-auto ml-auto p-1">
              <svg class="w-5 h-5 text-gray-500"  fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z"
                      clip-rule="evenodd"></path>
              </svg>
            </button>
          </div>
        </a>
    </div>
  </main>
</template>

<script>
import dayjs from '@/utils/dayjs';
import HeaderView from './HeaderView.vue';
import AsideView from './AsideView.vue';

export default {
  methods: {
    format(data) {
      return dayjs(data, 'hh:mm DD.MM.YYYY').fromNow(true);
    },
  },
  data() {
    return {
      videos: [],
      searchInput: '',
    };
  },
  async created() {
    const input = localStorage.getItem('searchInput');
    this.searchInput = input ? input : '';
    const request = 'http://localhost:8080/api/v1/findvideos/?find=' + this.searchInput;
    const response = await fetch(request);
    this.videos = await response.json();
    if (input)
      localStorage.removeItem('searchInput');
  },
  components: {
    HeaderView,
    AsideView,
  },
};
</script>

<style>

</style>
