<template>
  <div class="banner w-full min-h-screen flex flex-col sm:justify-center items-center pt-6 sm:pt-0" >
    <div class="w-full sm:max-w-md p-5 mx-auto">
      <h2 class="mb-12 text-center text-5xl font-extrabold text-gray-200">Регистрация</h2>
      <form>
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="nickname">Никнейм</label>
          <input id="nickname" type="text" name="nickname" class="bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="email">Почта</label>
          <input id="email" type="text" name="" class="email bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="password">Пароль</label>
          <input id="password1" type="password" name="password1" class="bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="password">Повторите пароль</label>
          <input id="password2" type="password" name="password2" class="bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mt-6">
          <router-link to="/login">
            <button class="w-full inline-flex items-center justify-center px-4 py-2 bg-yellow-700 border border-transparent rounded-md font-semibold capitalize text-white hover:bg-yellow-800 active:bg-red-700 focus:outline-none focus:border-red-700  disabled:opacity-25 transition">Зарегистрироваться</button>
          </router-link>
        </div>
        <div class="mt-6 text-center text-white">
          <router-link to="/login" class="underline">Уже есть аккаунт? Войдите.</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.banner {
  background: url(http://4.bp.blogspot.com/-v2qV3ee8ikA/Vfu1-fWSGtI/AAAAAAAABrs/hiv3sAkszYo/s1600/Sugar-bag-final-animation.gif);
  background-repeat: no-repeat;
  background-size: cover
}
</style>
