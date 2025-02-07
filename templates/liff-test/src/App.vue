<script setup>
  import liff from "@line/liff";
  import CustomTextArea from "./components/CustomTextArea.vue";
  import { ref, onMounted } from "vue";
  import { RouterView, RouterLink } from "vue-router";

  /*  
  export default {
    data() {
      return {
        message: "",
        error: ""
      };
    },
    mounted() {
      liff
        .init({
          //liffId: import.meta.env.VITE_LIFF_ID
          liffId: '2006831755-QEdgjOA8'
        })
        .then(() => {
          this.message = "LIFF init succeeded.";
  
          alert(liff.getContext());
  
          liff
            .sendMessages([
              {
                type: "text",
                text: "Hello, World!",
              },
            ])
            .then(() => {
              alert("message sent");
            })
            .catch((err) => {
              alert("error", err);
            });
        })
        .catch((e) => {
          this.message = "LIFF init failed.";
          this.error = `${e}`;
        });
    }
  };
*/
const message = ref("");
const error = ref("");

  onMounted(
    function() {
      liff
      .init({
        //liffId: import.meta.env.VITE_LIFF_ID
        liffId: '2006831755-QEdgjOA8'
      })
      .then(() => {
        message.value = "LIFF init succeeded.";

        liff
          .sendMessages([
            {
              type: "text",
              text: "Hello, World!",
            },
          ])
          .then(() => {
            alert("message sent");
          })
          .catch((err) => {
            alert("error", err);
          });

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
    <a href="https://developers.line.biz/ja/docs/liff/" target="_blank" rel="noreferrer">
      LIFF Documentation
    </a>
  </div>
  <section>
    <CustomTextArea
      name="test1"
      value="tttttttt" />
  </section>
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
