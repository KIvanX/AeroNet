<template>
  <div id="app">
    <div id="top">
      <router-link class="main_top_a" to="/">AeroNet</router-link>
      <router-link class="a" to="/about">О нас</router-link>
      <span v-if="is_auth">
        <router-link class="a" to="/history">История</router-link>
        <router-link class="a" to="/account">Личный кабинет</router-link>
        <router-link class="a" to="/" @click="exit">Выход</router-link>
      </span>
      <span v-else>
        <router-link class="a" to="/authorization">Авторизация</router-link>
        <router-link class="a" to="/registration">Регистрация</router-link>
      </span>
    </div>

    <router-view></router-view>
  </div>
</template>

<script>
import {mapGetters, mapActions} from "vuex";

export default {
  name: 'App',
  computed: {
    ...mapGetters(["is_auth"])
  },
  methods: {
    exit() {
      this.exit_from_account()
    },
    ...mapActions(["exit_from_account"])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#top {
  position: absolute;
  text-align: right;
  padding-top: 10px;
  left: 0;
  top: 0;
  width: 100%;
  height: 35px;
  background-color: rgb(100, 100, 179);
}
.a {
  color: black;
  margin-right: 20px;
}
a:hover {
  color: white;
}
.main_top_a {
  position: absolute;
  color: black;
  font-size: 30px;
  font-family: Avenir, serif;
  top: 5px;
  left: 20px;
  text-decoration: none;
}
.card {
  text-align: center;
  padding: 1px;
  margin-top: 20px;
  border-radius: 10px;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  height: 55px;
  background-color: #85a9ff;
}

.submit_button {
  font-size: 14px;
  width: 150px;
  height: 40px;
  background-color: #496dc3;
  border-radius: 10px;
  border: #496dc3;
}
.submit_button:hover {
  background-color: #334d87;
}
</style>
