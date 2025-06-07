<template>
  <div class="upload">
    <input type="file" @change="onFileChange" accept="image/*"/>
    <button @click="submit" :disabled="!file">Analyser</button>
    <p v-if="error" class="error">{{ error }}</p>
    <div v-if="result">
      <p>Code : {{ result.code }}</p>
      <p>Diagnostic : {{ result.label }}</p>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data(){ return { file:null,result:null,error:null } },
  methods:{
    onFileChange(e){ this.file=e.target.files[0]; this.result=this.error=null },
    async submit(){
      try {
        const f=new FormData(); f.append('image',this.file)
        const r=await axios.post('/predict',f)
        this.result=r.data
      } catch(e){ this.error=e.response?.data?.error||'Erreur' }
    }
  }
}
</script>
<style scoped>
.upload{display:flex;flex-direction:column;gap:1rem;align-items:center;}
.error{color:red;}
button{padding:0.5rem 1rem;}
</style>
