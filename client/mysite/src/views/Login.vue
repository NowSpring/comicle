<template>
  <div class="overlay">
    <v-card 
      width="400px" 
      class="mx-auto mt-5"
    >
      <v-card-title class="d-flex justify-center">
        <h3 class="title font-weight-bold">
          Welcome to Comicle!!
        </h3>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field 
            prepend-icon="mdi-account-circle" 
            label="UserName" 
            v-model="formState.username" 
          />
          <v-text-field 
            :type="showPassword ? 'text' : 'password'"
            @click:append="showPassword = !showPassword"
            prepend-icon="mdi-lock" 
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            label="Password"
            v-model="formState.password"
          />   
          <v-card-actions class="d-flex justify-center">
            <div class="button-container">
              <v-btn 
                class="info" 
                :disabled="formState.username === '' || formState.password === ''"
                @click.prevent="submitLogin"
              >
                ログイン
              </v-btn>
              <v-btn>
                新規作成
              </v-btn>
            </div>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup>
import { ref, reactive, toRaw } from 'vue';
import { useRouter } from 'vue-router';
import EventService from '@/plugins/EventService.js';

const router = useRouter();

const formState = reactive({
  username: '',
  password: '',
});

const showPassword = ref(false);

const submitLogin = () => {
  EventService.submitLogin(toRaw(formState))
    .then((response) => {
      console.log(response.data);
      window.localStorage.setItem('token', response.data.token);
      window.localStorage.setItem('user_id', response.data.user_id);
      window.localStorage.setItem('user_name', response.data.user_name);
      router.push({ name: 'comicmaster' });
    })
    .catch((error) => {
      console.log("Error" + error);
    });
};
</script>

<style>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.button-container {
  display: flex;
  justify-content: space-between; 
}
</style>
