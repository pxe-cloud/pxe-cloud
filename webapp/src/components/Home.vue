<template>
 <!-- Home  -->
    <div class="container mb-5 ">
        <div class=" mt-5 text-dark p-5 rounded shadow-lg bg-home">
            
                <div class="container">
                    <h2>Welcome to the ipxe database administrator</h2>
                    <p>Choose in the browser, the option you prefer.</p>
                    <p>{{ msg }}</p>
                </div>
        </div>                
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
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

