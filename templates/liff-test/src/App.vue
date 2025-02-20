<script setup>
  import liff from "@line/liff";
  import CustomTextArea from "./components/CustomTextArea.vue";
  import { ref, onMounted } from "vue";
  import { RouterView, RouterLink } from "vue-router";

  const message = ref("");
  const error = ref("");

  onMounted(
    function() {
      liff
      .init({
        //liffId: import.meta.env.VITE_LIFF_ID
        //liffId: '2006831755-QEdgjOA8'
        liffId: '2006899352-ndBbWrOK'
      })
      .then(() => {
        message.value = "LIFF init succeeded.";

        liff.getProfile()
          .then(
            function(profile) {
              alert('userId:'+profile.userId);
            }
          )

      })
      .catch((e) => {
        message.value = "LIFF init failed.";
        error.value = `${e}`;
      });
      console.log('message:' + message);
      console.log("error:"+error);  
    }
  )

</script>

<template>
  <div>
    <h1>create-liff-app</h1>
    <p v-if="message">{{ message }}</p>
    <p v-if="error">
      <code>{{ error }}</code>
    </p>
  </div>
  <section>
    <RouterLink to="/test1">リンクテスト</RouterLink>
  </section>
  <section>
    <RouterLink to="/test2">リンクテスト2</RouterLink>
  </section>
  <section> 
    <RouterView />
  </section>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
