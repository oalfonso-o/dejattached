<template>
  <div id="app">
    <LoginContainer v-if="!isLoggedIn"/>
    <HomeContainer v-if="isLoggedIn"/>
  </div>
</template>

<script>
  import LoginContainer from '@/components/LoginContainer.vue'
  import HomeContainer from '@/components/HomeContainer.vue'
  export default {
    components : {
      LoginContainer,
      HomeContainer
    },
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn }
    }
  }
</script>

<style lang="scss">
$color: #2c3e50;
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: $color;
}
</style>

