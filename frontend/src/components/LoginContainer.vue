<template>
  <div class="logincontainer">
    <div id="nav">
      <Login v-if="login_form"/>
      <Register v-if="register_form"/>
      <span> <a @click="login">Login</a></span>
      <span> | <a @click="register">Register</a></span>
    </div>
  </div>
</template>

<script>
  import Login from '@/components/Login.vue'
  import Register from '@/components/Register.vue'
  export default {
    components : {
      Login,
      Register
    },
    data(){
      return {
        login_form : true,
        register_form : false
      }
    },
    methods : {
      login () {
        this.login_form = true; this.register_form = false
      },
      register () {
        this.register_form = true; this.login_form = false
      }
    }
  }
</script>