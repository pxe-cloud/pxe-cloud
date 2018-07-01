<template>
 <!-- users get -->
    <div class="container mb-5 ">
        <div class=" mt-5 text-dark p-5 rounded shadow-lg bg-home">
            
                <div class="container">
                    <p>{{ msg }}</p>
                </div>
        </div>                
  </div>
</template>

<script>
export default {
  name: 'usersGet',
  data () {
    return {
      msg: 'users get'
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