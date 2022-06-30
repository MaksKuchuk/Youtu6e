<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-14">
    <section class="section" id="app">
        <div class="container">
            <h1 class="title mb-6">Загрузить Видео</h1>
            <div v-if="document" class="progress mb-6">
              <progress class="progress" :value="progress" max="100">{{this.progress}}%</progress>              
            </div>
            <div class="file">
              <label class="file-label">
                <input type="file" ref="file" class="file-input" @change="selectFile">    
              </label>
            </div>
            <button v-if="document" class="mt-2" @click="upload">Загрузить</button>
            <div v-if="message">{{this.message}}</div>
        </div>
    </section>
  </main>
</template>

<script>
import HeaderView from './HeaderView.vue'
import AsideView from './AsideView.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

export default {
  components: {
    HeaderView,
    AsideView,
  },

  data() {
    return {
      message: '',
      progress: 0,
      document: null,
    }
  },

  methods: {
    selectFile() {
      this.document = this.$refs.file.files.item(0)
    },

    async upload() {
      const headers = {
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Token ' + localStorage.getItem('authToken')
      }
      alert(this.document.type)
      let formData = new FormData()
      formData.append('header', this.document)
      await axios.post('http://localhost:8000/api/v1/userinfo/', formData, {headers})
        .catch(error => {
          console.log(error)
        })
    }

  },
  
};
</script>

<style scoped>
.router-link-active{
  @apply border-b-2 border-gray-300 text-gray-900;
}
</style>
