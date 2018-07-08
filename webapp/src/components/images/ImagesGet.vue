<template>
 <!-- images Gert  -->
    <div class="container mb-5 ">
        <div class=" mt-5 text-dark p-5 rounded shadow-lg bg-home">
            
                <div class="container">
                    <h2 class="text-left mb-4">{{ msg }} 
                      <b-btn to="/imagesadd" variant="outline-success" class="float-right">Add new image</b-btn> 
                    </h2>
                    <!-- ------- alert --------------- -->
                    <b-alert v-if='deleteImg != null && deleteImg.includes("Successfully")' variant="success" show> {{ deleteImg }} </b-alert>
                    <b-alert v-if='deleteImg != null && deleteImg.includes("Error")' variant="danger" show> {{ deleteImg }} </b-alert>
                    <!-- --------end alert--------------- -->
                    
                    <input type="search" v-model="searching" class="form-control mb-3" placeholder="Search image">
                     
                    <!-- -------------------------------- -->
                      <div role="tablist"  v-if="images != null">
                        <b-card no-body class="mb-1" v-for=" (img, index) in  searchImages ">
                          <b-card-header header-tag="header" class="p-1 " role="tab">
                            <b-btn  href="#" v-b-toggle="'accordion'+index" class="col-10 text-left" variant="light"> {{ img.title }} </b-btn>
                            <router-link :to="{name:'ImagesEdit', params: {id: img.id}}" class="material-icons align-middle" >edit</router-link>
                            
                            <!-- ----------modal alert confirm, delete--------- -->
                            <span  @click="showModal(index)" class="material-icons align-middle cursorPoint">delete</span>
                            <b-modal ref="myModalRef" hide-footer>
                              <div class="d-block text-center">
                                Are you sure you want to erase the image {{ img.title }} 
                              </div>
                              <hr>
                              <b-btn @click="hideModal(index)" class="mt-3"  variant="primary">Cancel</b-btn>
                              <b-btn @click="deleteImage(img.id, index)" class="mt-3"  variant="danger">Delete</b-btn>
                            </b-modal>
                            <!-- --------end modal------------ -->
                            
                          </b-card-header>
                          <b-collapse :id="'accordion' + index"  accordion="my-accordion" role="tabpanel">
                            <b-card-body>
                              <b-list-group>
                                <b-list-group-item variant="primary" class="text-left"><span class="font-weight-bold">Type:</span> {{ img.type }}</b-list-group-item>
                                <b-list-group-item variant="success" class="text-left"> <span class="font-weight-bold">Image_source:</span> {{ img.image_source }}</b-list-group-item>
                                <b-list-group-item variant="warning" class="text-left" v-if="img.kernel_source != ''"><span class="font-weight-bold">Kernel_source:</span> {{ img.kernel_source }}</b-list-group-item>
                                <b-list-group-item variant="info" class="text-left" v-for=" value, key in img.boot_args "><span class="font-weight-bold">Boot_args:</span> {{ key }}: {{value}}</b-list-group-item>
                              </b-list-group>
                            </b-card-body>
                          </b-collapse>
                        </b-card>                        
                      </div>
                       <b-alert show v-else>loading...</b-alert>
                    <!-- --------------------------------- -->
                </div>
        </div>        
                
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'imagesGet',
  mounted () {
    this.getImages()
  },
  data () {
    return {
      msg: 'Images',
      images: null,
      searching: '',
      deleteImg: null
    }
  },
  methods: {
    getImages () {
      axios.get('http://api.jorgepastorr.tk:50022/images')
        .then((response) => {
          this.images = response.data.response
        })
    },
    deleteImage (id, index) {
      this.hideModal(index)
      axios.delete('http://api.jorgepastorr.tk:50022/image/' + id)
        .then((response) => {
          this.deleteImg = response.data.response
          setTimeout(function () {
            this.deleteImg = null
            this.getImages()
          }.bind(this), 2000)
        })
    },
    showModal (index) {
      console.log(this.$refs.myModalRef[index])
      this.$refs.myModalRef[index].show()
    },
    hideModal (index) {
      this.$refs.myModalRef[index].hide()
    }
  },
  computed: {
    searchImages () {
      return this.images.filter((img) => img.title.includes(this.searching))
    }
  }
}
</script>

<style>
.bg-home{
  background-color: #e6e6e6;
}
.cursorPoint{
  cursor: pointer;
}
</style>