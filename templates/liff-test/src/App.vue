<script setup>
  import liff from "@line/liff";
  import CustomTextArea from "./components/CustomTextArea.vue";
  import { ref, onMounted } from "vue";

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
  let message = "";
  let error = "";
  
  onMounted(
    function() {
      liff
      .init({
        //liffId: import.meta.env.VITE_LIFF_ID
        liffId: '2006831755-QEdgjOA8'
      })
      .then(() => {
        message = "LIFF init succeeded.";

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
        message = "LIFF init failed.";
        error = `${e}`;
      });
      console.log("message:"+message);
      console.log("error:"+error);
      const message_disp = ref(message);
      const error_disp = ref(error);  
    }
  )

</script>

<template>
  <div>
    <h1>create-liff-app</h1>
    <p v-if="message_disp">{{ message_disp }}</p>
    <p v-if="error_disp">
      <code>{{ error_disp }}</code>
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
