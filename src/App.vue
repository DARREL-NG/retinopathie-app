<template>
  <div id="app">
    <h1>Diagnostic Rétinopathie Diabétique</h1>
    <Upload />
  </div>
</template>

<script>
import Upload from './components/Upload.vue'

export default {
  components: { Upload }
}
</script>

<style>
#app {
  max-width: 600px;
  margin: 2rem auto;
  font-family: Arial, sans-serif;
  text-align: center;
}
</style>
