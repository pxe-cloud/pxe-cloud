<template>
 <!-- images edit  -->
    <div class="container mb-5 ">
        <div class=" mt-5 text-dark p-5 rounded shadow-lg bg-home">
          
          <h2 class="text-left mb-4">{{ msg }}</h2>
          <!-- ------- alert --------------- -->
          <b-alert v-if='responseEdit != null && responseEdit.includes("Successfully")' variant="success" show> {{ responseEdit }} </b-alert>
          <b-alert v-if='responseEdit != null && responseEdit.includes("Error")' variant="danger" show> {{ responseEdit }} </b-alert>
          <!-- --------end alert--------------- -->
          
          <!-- -------------------- -->
           <b-form @submit="onSubmit" v-if="show" class="text-left">
            
            <b-form-group horizontal :label-cols="2" label="Title:" class="text-left" description="This is the title of the image">
              <b-form-input type="text" v-model="image.title" required placeholder="Enter title image"></b-form-input>
            </b-form-group>

            <b-form-group label="Type:" horizontal :label-cols="2" class="text-left" description="This is the type of the image (iso, kernel_initrd)">
              <b-form-select required v-model="image.type">
                <option :value="null">Please select an option</option>
                <option value="iso">Iso</option>
                <option value="kernel_initrd">kernel_initrd</option>
              </b-form-select>
            </b-form-group>

            <b-form-group v-if="image.type == 'kernel_initrd'" label="Kernel source:" horizontal :label-cols="2" class="text-left" description="This is the url (the source) of the kernel">
              <b-form-input type="text" v-model="image.kernel_source" :required="image.type == 'kernel_initrd'" placeholder="Enter kernel"></b-form-input>
            </b-form-group>
            
            <b-form-group v-if="image.type != null" label="Image source:"  horizontal :label-cols="2" class="text-left" description="This is the url (the source) of the image (iso, initramfs)">
              <b-form-input type="text" v-model="image.image_source" required placeholder="Enter image"></b-form-input>
            </b-form-group>

            <b-form-group v-if="image.type != null" label="Boot args:"  horizontal :label-cols="2" class="text-left" 
            description="The 'key' of the boot argument. If the boot arg has no value, just add the arg. The value of the boot argument ">
              
              <b-btn v-if="Object.keys(image.boot_args).length === 0" @click="showModal()" class="float-right" variant="info"><span  class="material-icons align-middle">add</span></b-btn>

              <b-input-group v-else v-for="(value, key, index) in image.boot_args" >          
                <b-form-input class="col-2" placeholder="Arg" v-model="key" disabled ></b-form-input>
                <b-form-input placeholder="Value" v-model="image.boot_args[key]"></b-form-input>
                <b-input-group-append>
                  <b-btn variant="outline-danger" @click="showModal2(key)"><span  class="material-icons align-middle">remove</span></b-btn>
                  <b-btn @click="showModal()" variant="info"><span  class="material-icons align-middle">add</span></b-btn>
                </b-input-group-append>
              </b-input-group>

              <!-- ----------modal alert confirm, add  boot_arg--------- -->
                <b-modal ref="myModalRef" title="Insert new argument" hide-footer>
                  <b-form-input type="text" placeholder="Enter your argument" v-model="modelArg"></b-form-input>
                  <b-form-input type="text" placeholder="Enter your value" class="mt-1" v-model="modelArgValue"></b-form-input>
                  <hr>
                  <b-btn @click="hideModal()" class="mt-3"  variant="primary">Cancel</b-btn>
                  <b-btn @click="addArrayArg()" class="mt-3" >Add</b-btn>
                </b-modal>
                <!-- --------end modal------------ -->
                
                <!-- ----------modal alert confirm, delete boot_arg--------- -->
                <b-modal ref="myModalRef2" title="Delete argument" hide-footer>
                  <p> The argument will be permanently deleted </p>
                  <hr>
                  <b-btn @click="hideModal()" class="mt-3"  variant="primary">Cancel</b-btn>
                  <b-btn @click="deleteArg()" class="mt-3" >Delete</b-btn>
                </b-modal>
                <!-- --------end modal------------ -->
            
            </b-form-group>

            <b-button type="submit" variant="primary">Submit</b-button>

          </b-form>
          <!-- ------------------- -->
        </div>                
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ImagesEdit',
  mounted () {
    this.getImage()
  },
  data () {
    return {
      msg: 'Images Edit',
      id: null,
      image: {
        boot_args: {},
        id: '',
        image_source: '',
        kernel_source: '',
        title: '',
        type: null
      },
      show: true,
      modelArg: '',
      modelArgValue: '',
      responseEdit: null,
      argDelete: ''
    }
  },
  methods: {
    getImage () {
      this.id = this.$route.params.id
      axios.get('http://api.jorgepastorr.tk:50022/image/' + this.id)
          .then((response) => {
            this.image = response.data.response
          })
    },
    onSubmit (evt) {
      evt.preventDefault()
      axios.put('http://api.jorgepastorr.tk:50022/image/' + this.id,
        {
          'title': this.image.title,
          'type': this.image.type,
          'image_source': this.image.image_source,
          'kernel_source': this.image.kernel_source
        }
      )
        .then((response) => {
          this.responseEdit = response.data.response
          setTimeout(function () {
            this.responseEdit = null
          }.bind(this), 3000)
        })
      for (var key in this.image.boot_args) {
        axios.put('http://api.jorgepastorr.tk:50022/image/' + this.id + '/boot-arg/' + key,
          {
            'value': this.image.boot_args[key]
          })
          .then((response) => {
            this.responseEdit = response.data.response
            setTimeout(function () {
              this.responseEdit = null
            }.bind(this), 1000)
          })
      }
    },
    showModal2 (arg) {
      this.$refs.myModalRef2.show()
      this.argDelete = arg
    },
    showModal () {
      this.$refs.myModalRef.show()
    },
    hideModal () {
      this.$refs.myModalRef.hide()
      this.modelArg = ''
      this.modelArgValue = ''
      this.$refs.myModalRef2.hide()
    },
    addArrayArg () {
      axios.post('http://api.jorgepastorr.tk:50022/image/' + this.id + '/boot-args',
        {
          'arg': this.modelArg,
          'value': this.modelArgValue
        })
        .then((response) => {
          this.responseEdit = response.data.response
          setTimeout(function () {
            this.responseEdit = null
            this.getImage()
          }.bind(this), 1000)
        })
      this.hideModal()
    },
    deleteArg () {
      this.$refs.myModalRef2.hide()
      axios.delete('http://api.jorgepastorr.tk:50022/image/' + this.id + '/boot-arg/' + this.argDelete)
        .then((response) => {
          this.responseEdit = response.data.response
          setTimeout(function () {
            this.responseEdit = null
            this.getImage()
          }.bind(this), 1000)
        })
    }
  }
}
</script>

<style>
.bg-home{
  background-color: #e6e6e6;
}
</style>


