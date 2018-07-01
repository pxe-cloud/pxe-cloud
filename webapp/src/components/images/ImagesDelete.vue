<template>
 <!-- images Delete  -->
      <div class="container mb-5 ">
        <div class=" mt-5 text-dark p-5 rounded shadow-lg bg-home">
            
          <div class="container">
              <h2 class="text-left mb-4">{{ msg }}</h2>
              <input type="search" v-model="searching" class="form-control mb-3" placeholder="Search image">
              
                <!-- -------------------- -->
                <b-list-group v-if="images != null">
                  <b-list-group-item class="d-flex justify-content-between align-items-center" v-for=" (img, index) in  searchImages ">
                    {{ img.title}}
                    <button type="button" class="btn btn-danger">Delete</button>
                  </b-list-group-item>
                </b-list-group>
                <!-- -------------------- -->
                <b-alert show v-else>loading...</b-alert>
              <!-- --------------------------------- -->
          </div>
        </div>                
      </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'imagesDelete',
  mounted () {
    this.getImages()
  },
  data () {
    return {
      msg: 'images Delete',
      images: null,
      searching: ''
    }
  },
  computed: {
    searchImages () {
      return this.images.filter((img) => img.title.includes(this.searching))
    }
  },
  methods: {
    getImages () {
      axios.get('http://192.168.88.4:8001/images')
        .then((response) => {
          this.images = response.data.response
        })
    }
  }
}
</script>

<style>
.bg-home{
  background-color: #e6e6e6;
  /* background-color: #f2f2f2; */
}
</style>