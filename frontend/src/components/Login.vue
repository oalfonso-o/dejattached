<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Login</h1>
      <label>username</label>
      <input required v-model="username" type="text" placeholder="Username"/>
      <label>Password</label>
      <input required v-model="password" type="password" placeholder="Password"/>
      <hr/>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        username : "",
        password : ""
      }
    },
    methods: {
      login: function () {
        let username = this.username
        let password = this.password
        this.$store.dispatch('login', { username, password })
          .then(() => this.$router.push('/'))
      }
    }
  }
</script>
