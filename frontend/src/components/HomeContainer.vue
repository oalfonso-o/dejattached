<template>
  <div class="homecontainer">
    <div id="nav">
      <router-link to="/"> Reservations </router-link>
      <router-link to="/numberdisplay"> numberdisplay </router-link>
      <router-link to="/submitnumber"> submitnumber </router-link>
      <router-link to="/logout"> Logout </router-link>
    </div>
    <div>
      <router-view/>
    </div>
  </div>
</template>

<script>
  export default {
    created: function () {
      this.$http.interceptors.response.use(undefined, function (err) {
        return new Promise(function () {
          if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
            this.$router.push('/logout')
          }
          throw err;
        });
      });
    },
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn }
    }
  }
</script>
