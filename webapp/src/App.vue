<template>
  <div id="app">
      <b-navbar toggleable="md" type="dark" variant="dark">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        
        <b-navbar-brand to="/home"><img src="./assets/logo2.png" width="60"/>  PxeCloud</b-navbar-brand>

        <b-collapse is-nav id="nav_collapse">

          <b-navbar-nav>
            <b-nav-item-dropdown text="Users">
              <b-dropdown-item to="/usersget">Get</b-dropdown-item>
              <b-dropdown-item to="/usersadd">Add</b-dropdown-item>
              <b-dropdown-item to="/usersedit">Edit</b-dropdown-item>
              <b-dropdown-item to="/usersdelete">Delete</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
          
          <b-navbar-nav>
            <b-nav-item-dropdown text="Organizations">
              <b-dropdown-item to="/organizationsget">Get</b-dropdown-item>
              <b-dropdown-item to="/organizationsadd">Add</b-dropdown-item>
              <b-dropdown-item to="/organizationsedit">Edit</b-dropdown-item>
              <b-dropdown-item to="/organizationsdelete">Delete</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>

          <b-navbar-nav>
            <b-nav-item-dropdown text="Groups">
              <b-dropdown-item to="/groupsget">Get</b-dropdown-item>
              <b-dropdown-item to="/groupsadd">Add</b-dropdown-item>
              <b-dropdown-item to="/groupsedit">Edit</b-dropdown-item>
              <b-dropdown-item to="/groupsdelete">Delete</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>

          <b-navbar-nav>
            <b-nav-item-dropdown text="Menus">
              <b-dropdown-item to="/menusget">Get</b-dropdown-item>
              <b-dropdown-item to="/menusadd">Add</b-dropdown-item>
              <b-dropdown-item to="/menusedit">Edit</b-dropdown-item>
              <b-dropdown-item to="/menusdelete">Delete</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>

          <b-navbar-nav>
            <b-nav-item to="/imagesget">Images</b-nav-item>
          </b-navbar-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item href="#" disabled>Singout</b-nav-item>
          </b-navbar-nav>

        </b-collapse>
     </b-navbar>

  <!-- navbar-1.vue -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}

body {
    background-image: url("./assets/registry.jpg");
}
</style>
