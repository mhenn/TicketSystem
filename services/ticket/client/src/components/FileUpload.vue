<template>
  <v-card class="example-vuex">
    <div class="upload">
      <ul>
        <li v-for="(file, index) in files" :key="file.id">
          <span>{{file.name}}</span> -
          <span>{{file.size }}</span> -
          <span v-if="file.error">{{file.error}}</span>
          <span v-else-if="file.success">success</span>
          <span v-else-if="file.active">active</span>
          <span v-else-if="file.active">active</span>
          <span v-else>{{index}}</span>
        </li>
      </ul>
      <div class="example-btn">
        <file-upload
          class="btn btn-primary"
          post-action="/upload/post"
          extensions="gif,jpg,jpeg,png,webp"
          accept="image/png,image/gif,image/jpeg,image/webp"
          :multiple="true"
          :size="1024 * 1024 * 10"
          :value="files"
          @input="inputUpdate"
          ref="upload">
          <i class="fa fa-plus"></i>
          Select files
        </file-upload>
      </div>
    </div>
  </v-card>
</template>
<style>
.example-vuex label.btn {
  margin-bottom: 0;
  margin-right: 1rem;
}
</style>

<script>
import { mapState } from 'vuex'
import FileUpload from 'vue-upload-component'
export default {
  name : 'Upload',
  components: {
    FileUpload,
  },
  computed: {
    ...mapState([
      'files',
    ])
  },
  methods: {
    inputUpdate(files) {
      this.$store.commit('updateFiles', files)
    },
  }
}
</script>
