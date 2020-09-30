<template>
  <div v-if="show" class="example-drag">
    <div class="upload">
      <ul v-if="files.length">
			<li v-for="file in files" :key="file.id">
          <span>{{file.name}}</span> -
          <span>{{file.size | formatSize}}</span> -
          <span v-if="file.error">{{file.error}}</span>
          <span v-else-if="file.success">success</span>
          <span v-else-if="file.active">active</span>
          <span v-else></span>
        </li>
      </ul>
      <v-card class="center" v-else>
        <td colspan="7">
          <div class="text-center p-5">
            <h4>Drop files anywhere to upload<br/>or</h4>
            <label for="file" ><h4>Select Files</h4></label>
          </div>
        </td>
      </v-card>

      <div v-show="$refs.upload && $refs.upload.dropActive" class="drop-active">
			<h3>Drop files to upload</h3>
      </div>

      <div class="">
	<v-btn text>	
        <file-upload
          post-action="/upload/post"
          :multiple="true"
          :drop="true"
          :drop-directory="true"
          v-model="files"
          ref="upload">
				Select Files
        </file-upload>
	</v-btn>
        <v-btn text   v-if="!$refs.upload || !$refs.upload.active" @click.prevent="$refs.upload.active = true">
          <i class="fa fa-arrow-up" aria-hidden="true"></i>
          Start Upload
        </v-btn>
        <v-btn   class="red darken-1" v-else @click.prevent="$refs.upload.active = false">
          <i class="fa fa-stop" aria-hidden="true"></i>
          Stop Upload
        </v-btn>
      </div>
    </div>

  </div>
</template>



<script>
import FileUpload from 'vue-upload-component'
export default {
  components: {
    FileUpload,
  },
  props:['show'],
  data() {
    return {
      files: [],
    }
  }
}
</script>



<style>
.example-drag label.btn {
  margin-bottom: 0;
  margin-right: 1rem;
}


.center{
	display:flex;
	justify-content:center;
}

.example-drag .drop-active {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  position: fixed;
  z-index: 9999;
  opacity: .6;
  text-align: center;
  background: #000;
}
.example-drag .drop-active h3 {
  margin: -.5em 0 0;
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  font-size: 40px;
  color: #fff;
  padding: 0;
}
</style>

