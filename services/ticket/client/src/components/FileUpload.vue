<template>
    <div class="upload">
  <v-card class="example-vuex">
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
  </v-card>
      <div >
        <file-upload
			class="swole"
          post-action="/upload/post"
          :multiple="true"
          :value="files"
          @input="inputUpdate"
          ref="upload">
          <v-btn dark class="swole">Select Files</v-btn>
        </file-upload>
      </div>
    </div>
</template>

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


<style scoped>

.swole{
	width:100%;
}


.example-vuex label.btn {
  margin-bottom: 0;
  margin-right: 1rem;
}
</style>
