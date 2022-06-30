<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-20 px-5 pb-5 grid max-w-screen-2xl m-auto">
    <form class="max-w-screen-2xl">
      <div class="flex">
        <div class="w-1/2">
          <div class="pt-3 pb-3 pl-2 font-bold uppercase bg-red-100 rounded">Изменить аватарку и шапку канала</div>
          <div class="flex pt-5">
            <img
                src="https://mdbcdn.b-cdn.net/img/new/avatars/1.webp"
                class="rounded-full w-20 shadow-lg"
                alt="Avatar"
            />
            <div class="flex justify-center pr-5">
              <div class="mb-3 w-96 pl-5">
                <label class="form-label inline-block mb-2 text-gray-700 text-xs font-bold uppercase">Выберите аватарку</label>
                <input class="form-control block w-full px-2 py-1 text-sm font-normal text-gray-700 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="" type="file">
              </div>
            </div>
            <button type="button" class="inline-block px-6 border-2 border-pink-400 text-pink-400 font-medium text-xs leading-tight uppercase rounded-xl hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 ">Применить</button>
          </div>
          <div class="pt-5 flex">
            <img
                src="https://stylecss.ru/wp-content/themes/css/demo/bird.jpg"
                class="w-full pr-10 h-2/3"
                alt="Avatar"
            />
            <div class="flex flex-col">
              <div class="mb-3 w-96">
                <label class="form-label inline-block mb-2 text-gray-700 text-xs font-bold uppercase">Выберите шапку</label>
                <input class="form-control block w-full px-2 py-1 text-sm font-normal text-gray-700 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="" type="file">
              </div>
              <button type="button" class="inline-block pt-5 pb-5 px-10 border-2 border-pink-400 text-pink-400 font-medium text-xs leading-tight uppercase rounded-xl hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 ">Применить</button>
            </div>
          </div>
        </div>
      </div>
    </form>
    <form class="max-w-screen-2xl pt-7">
      <div class="font-bold uppercase pt-3 pb-3 pl-2 bg-red-100 rounded w-1/2">Добавить видео</div>
      <div class="flex pb-5 pt-5">
        <div class="w-1/2">
          <div class="flex flex-wrap -mx-3 mb-3">
            <div class="w-full w-full px-3 pr-10">
              <label class="block uppercase text-gray-700 text-xs font-bold mb-2">
                Название
              </label>
              <input class="appearance-none block w-full text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="" type="text" >
            </div>
          </div>
          <div class="flex justify-start">
            <div class="mb-3 w-96">
              <label for="formFileLg" class="form-label inline-block mb-2 text-gray-700 block uppercase text-xs font-bold">Превью</label>
              <input class="form-control block w-fullpx-2 py-1.5 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-red-500 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="" type="file">
            </div>
          </div>
          <div class="flex justify-start">
            <div class="mb-3 w-96">
              <label for="formFileLg" class="form-label inline-block mb-2 text-gray-700 block uppercase text-xs font-bold">Видео</label>
              <input class="form-control block w-fullpx-2 py-1.5 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-red-500 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="" type="file">
            </div>
          </div>
        </div>
        <div class="w-1/2 pb-5">
          <label class="block uppercase text-gray-700 text-xs font-bold pb-2">Описание</label>
          <textarea class="w-full h-full p-3 font-medium border border-solid border-gray-300 focus:border-gray-600 focus:outline-none resize-none"></textarea>
        </div>
      </div>
      <button type="button" class="w-full inline-block px-6 py-2.5 bg-pink-500 text-white font-medium text-xs uppercase rounded shadow-lg hover:shadow-lg active:bg-pink-700 active:shadow-lg focus:outline-none transition duration-150 ease-in-out">Добавить</button>
    </form>
  </main>
  <main class="hidden md:ml-24 xl:ml-64 pt-20 px-5 pb-5 grid max-w-screen-2xl m-auto">
    <div class="font-bold uppercase flex justify-center h-1/2">
      Пожалуйста, авторизируйтесь!
    </div>
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
