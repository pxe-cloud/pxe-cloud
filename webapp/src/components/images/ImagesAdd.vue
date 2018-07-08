<template>
 <!-- images edit  -->
    <div class="container mb-5 ">
        <div class=" mt-5 text-dark p-5 rounded shadow-lg bg-home">
          
          <h2 class="text-left mb-4">{{ msg }}</h2>
          <!-- ------- alert --------------- -->
          <b-alert v-if='responseAdd != null && responseAdd.includes("Successfully")' variant="success" show> {{ responseAdd }} </b-alert>
          <b-alert v-if='responseAdd != null && responseAdd.includes("Error")' variant="danger" show> {{ responseAdd }} </b-alert>
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
                  <b-btn variant="outline-danger" @click="deleteArg(key)"><span class="material-icons align-middle">remove</span></b-btn>
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
  name: 'ImagesAdd',
  mounted () {
    this.getImage()
  },
  data () {
    return {
      msg: 'Images Add',
      image: {
        boot_args: {},
        image_source: '',
        kernel_source: '',
        title: '',
        type: null
      },
      show: true,
      modelArg: '',
      modelArgValue: '',
      responseAdd: null
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      axios.post('http://api.jorgepastorr.tk:50022/images',
        {
          'title': this.image.title,
          'type': this.image.type,
          'image_source': this.image.image_source,
          'kernel_source': this.image.kernel_source
        }
      )
        .then((response) => {
          this.responseAdd = response.data.response
          if (Object.keys(this.image.boot_args).length !== 0) {
            axios.get('http://api.jorgepastorr.tk:50022/images')
              .then((response) => {
                var answer = response.data.response
                for (var index in answer) {
                  if (this.image.title === answer[index].title) {
                    for (var key in this.image.boot_args) {
                      axios.post('http://api.jorgepastorr.tk:50022/image/' + answer[index].id + '/boot-args',
                        {
                          'arg': key,
                          'value': this.image.boot_args[key]
                        })
                          .then((response) => {
                            this.responseAdd = response.data.response
                            setTimeout(function () {
                              this.responseAdd = null
                            }.bind(this), 1000)
                          })
                    }
                  }
                }
                this.clearImage()
              })
          } else {
            setTimeout(function () {
              this.responseAdd = null
              this.clearImage()
            }.bind(this), 1000)
          }
        })
    },
    showModal () {
      this.$refs.myModalRef.show()
    },
    hideModal () {
      this.modelArg = ''
      this.modelArgValue = ''
      this.$refs.myModalRef.hide()
    },
    addArrayArg () {
      this.image.boot_args[this.modelArg] = this.modelArgValue
      this.hideModal()
    },
    deleteArg (arg) {
      this.$delete(this.image.boot_args, arg)
    },
    clearImage () {
      this.image.boot_args = {}
      this.image.image_source = ''
      this.image.kernel_source = ''
      this.image.title = ''
      this.image.type = null
    }
  }
}
</script>

<style>
.bg-home{
  background-color: #e6e6e6;
}
</style>


