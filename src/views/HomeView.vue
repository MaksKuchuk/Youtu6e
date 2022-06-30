<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-20 px-5 pb-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 max-w-screen-2xl m-auto">
    <div v-for="video in videos" :key="video.id">
      <div class="relative mb-3 group">
        <router-link :to="{name: 'video', params: {id: video.id}}">
          <img :src="`${ video.preview}`" :alt="X" class="object-cover aspect-video">
        </router-link>
      </div>
      <div class="flex item-start mt-3 group">
        <img src="https://i.pravatar.cc/1000" class="mr-3 rounded-full w-9 h-9" alt="">
        <div class="text-sm">
          <router-link :to="{name: 'video', params: {id: video.id}}">
            <span class="font-semibold text-gray-800">{{ video.name }}</span>
          </router-link>
          <div class="mt-1 flex items-center">
            <span>Channel name</span>
          </div>
          <div>
            <span>{{ video.views }}</span>
            &middot;
            <span>{{ format(video.uploadtime) }}</span>
          </div>
        </div>
      </div>
    </div>

  </main>
</template>

<script>
import dayjs from '@/utils/dayjs';
import HeaderView from './HeaderView.vue';
import AsideView from './AsideView.vue';

function getTime(linktovideo) {
    x = document.createElement("video");
    x.src = linktovideo;
    sec = x.duration;

    hours = sec / 3600 % 24;
    minutes = sec / 60 % 60;
    seconds = sec % 60;

    return num(hours) + ":" + num(minutes) + ":" + num(seconds);
}
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
