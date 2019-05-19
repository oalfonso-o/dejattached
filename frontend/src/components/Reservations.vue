<template>
  <div class="reservations">
    <h1>{{ msg }}</h1>
    <p>reservations</p>
  </div>
</template>

<script>
export default {
  name: 'reservations',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
a {
  color: #42b983;
}
</style>
