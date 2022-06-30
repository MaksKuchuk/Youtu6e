<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-14">
    <section class="section" id="app">
        <div class="container">
            <h1 class="title mb-6">Загрузите новое Видео</h1>
            <div v-if="document && preview && videoName" class="progress mb-6">
              <progress class="progress" :value="progress" max="100">{{this.progress}}%</progress>              
            </div>
            <div class="name">
              <label for="name">Название</label>
              <input required="true" class="border-gray-300 border" type="text" v-model="videoName">
            </div>
            <div class="file">
              <label for="file">Выбрать видео</label>
              <input required="true" type="file" ref="file" class="file-input" @change="selectFile">                 
            </div>
            <div class="file">
              <label for="preview">Выбрать превью</label>
              <input required="true" type="file" ref="preview" class="file-input" @change="selectPreview">                 
            </div>
            <div class="description">
              <label for="description">Добавьте описание</label>
              <input v-model="description" type="textarea" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-red-600 focus:outline-none">
            </div>
            <button v-if="document && preview && videoName" class="mt-2" @click="upload">Загрузить</button>
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
      preview: null,
      videoName: '',
      description: '',
    }
  },

  methods: {
    selectFile() {
      this.document = this.$refs.file.files.item(0)
    },

    selectPreview() {
      this.preview = this.$refs.preview.files.item(0)
    },

    async upload() {      
      const headers = {
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Token ' + localStorage.getItem('authToken')
      }      
      let formData = new FormData()
      formData.append('name', this.videoName)
      formData.append('video', this.document)
      formData.append('preview', this.preview)
      formData.append('description', this.description)
      await axios.post('http://localhost:8080/api/v1/addvideo/', formData, {headers})
        .catch(error => {
          console.log(error.response)
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
