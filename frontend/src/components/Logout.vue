<template><div></div></template>

<script>
  export default {
    created: function () {
        this.logout()
    },
    methods: {
      logout: function () {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
      }
    },
  }
</script>
