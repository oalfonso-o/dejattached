<template>
  <div class="submit_number">
    <h1>Submit a number</h1>
      <input v-model="numberInput" type="number" />
      <button @click="addNumber(numberInput)">
        Add new number
      </button>
  </div>
</template>

<script>
export default {
  name: "SubmitNumber",
  data() {
    return {
      numberInput: 0
    };
  },
  methods: {
    addNumber(numberInput) {
      this.$store.dispatch("addNumber", Number(numberInput));
    }
  }
};
</script>
