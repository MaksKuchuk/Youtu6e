<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-14 pb-5">
    <div class="h-20 sm:h-32 xl:h-52 bg-center bg-cover" :style="{backgroundImage: `url(${require('../assets/image.jpg')})`}"></div>
    <div class="px-20 pt-4 bg-grey-600 bg-gray-100">
      <div class="flex flex-col sm:flex-row justify-between items-start md:items-center mb-4">
        <div class="flex md:items-center">
          <div class="w-16 h-16 rounded-full mr-4 hidden sm:inline" :style="{backgroundImage: `url(${require('../assets/bg.jpg')})`}"></div>
          <div>
            <div class="flex items-center">
              <span class="text-2xl text-gray-700">Название</span>
            </div>
            <div class="text-sm">5 подписчиков</div>
          </div>
        </div>
        <button class="bg-red-700 text-white text-xs uppercase mt-2 xl:mt-0 py-2 px-4 rounded-sm" >Подписаться</button>
      </div>
      <div class="flex pb-5">
        <nav class="mt-2">
          <router-link to="/channel/:id" class="px-6 uppercase text-xs font-medium text-gray-500 hover:text-gray-900 py-2">О канале</router-link>

        </nav>
        <nav class="mt-2">
          <router-link to="/channel/videos/:id" class="px-6 uppercase text-xs font-medium text-gray-500 hover:text-gray-900 py-2">Видео</router-link>
        </nav>
        <div></div>
      </div>
    </div>
    <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 max-w-screen-2xl m-auto pt-6 px-5 ">
      <a href="#" class="mb-7 group">
        <div class="relative">
          <img src="https://picsum.photos/seed/image100/720/400" alt="">
          <span
            class="absolute opacity-100 group-hover:opacity-0 duration-500 bottom-0 right-0 bg-black text-white rounded-sm m-1 p-1 text-xs font-semibold">3:02</span>
        </div>
        <div class="flex item-start mt-3 group">
          <div class="text-sm">
            <span class="font-semibold text-gray-800">Title 1</span>
            <div>
              <span>10 views</span>
              &middot;
              <span>10 day</span>
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
      <a href="#" class="mb-7 group">
        <div class="relative">
          <img src="https://picsum.photos/seed/image200/720/400" alt="">
          <span
            class="absolute opacity-100 group-hover:opacity-0 duration-500 bottom-0 right-0 bg-black text-white rounded-sm m-1 p-1 text-xs font-semibold">3:02</span>
        </div>
        <div class="flex item-start mt-3 group">
          <div class="text-sm">
            <span class="font-semibold text-gray-800">Title 1</span>
            <div>
              <span>10 views</span>
              &middot;
              <span>10 day</span>
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
      <a href="#" class="mb-7 group">
        <div class="relative">
          <img src="https://picsum.photos/seed/image300/720/400" alt="">
          <span
            class="absolute opacity-100 group-hover:opacity-0 duration-500 bottom-0 right-0 bg-black text-white rounded-sm m-1 p-1 text-xs font-semibold">3:02</span>
        </div>
        <div class="flex item-start mt-3 group">
          <div class="text-sm">
            <span class="font-semibold text-gray-800">Title 1</span>
            <div>
              <span>10 views</span>
              &middot;
              <span>10 day</span>
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
      <a href="#" class="mb-7 group">
        <div class="relative">
          <img src="https://picsum.photos/seed/image400/720/400" alt="">
          <span
            class="absolute opacity-100 group-hover:opacity-0 duration-500 bottom-0 right-0 bg-black text-white rounded-sm m-1 p-1 text-xs font-semibold">3:02</span>
        </div>
        <div class="flex item-start mt-3 group">
          <div class="text-sm">
            <span class="font-semibold text-gray-800">Title 1</span>
            <div>
              <span>10 views</span>
              &middot;
              <span>10 day</span>
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
      <a href="#" class="mb-7 group">
        <div class="relative">
          <img src="https://picsum.photos/seed/image500/720/400" alt="">
          <span
            class="absolute opacity-100 group-hover:opacity-0 duration-500 bottom-0 right-0 bg-black text-white rounded-sm m-1 p-1 text-xs font-semibold">3:02</span>
        </div>
        <div class="flex item-start mt-3 group">
          <div class="text-sm">
            <span class="font-semibold text-gray-800">Title 1</span>
            <div>
              <span>10 views</span>
              &middot;
              <span>10 day</span>
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
      <a href="#" class="mb-7 group">
        <div class="relative">
          <img src="https://picsum.photos/seed/image600/720/400" alt="">
          <span
            class="absolute opacity-100 group-hover:opacity-0 duration-500 bottom-0 right-0 bg-black text-white rounded-sm m-1 p-1 text-xs font-semibold">3:02</span>
        </div>
        <div class="flex item-start mt-3 group">
          <div class="text-sm">
            <span class="font-semibold text-gray-800">Title 1</span>
            <div>
              <span>10 views</span>
              &middot;
              <span>10 day</span>
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
import HeaderView from './HeaderView.vue';
import AsideView from './AsideView.vue';
import ChannelView from './ChannelView.vue';

export default {
  components: {
    HeaderView,
    AsideView,
  },
};
</script>

<style>

</style>
