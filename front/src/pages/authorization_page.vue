
<template>
  <div id="form">
    <p><label>Имя <input type="text" v-model="username"></label></p>
    <p><label>Пароль <input type="password" v-model="password"></label></p>
    <p><button class="submit_button" @click="auth">Войти</button></p>
    <p><button @click="OAuth2">Войти через VK</button></p>
    <p><router-link class="link" to="/recovering_password">Забыли пароль?</router-link></p>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "authorization_page",
  data() {
    return {
      username: '',
      password: '',
      token: ''
    }
  },
  methods: {
    async auth() {
      if (await this.auth_user({
        'username': this.username,
        'password': this.password
      })) this.$router.push('/');
      else alert('Пользователь не найден')
    },
    OAuth2() {
      window.open('https://oauth.vk.com/authorize?client_id=51621727&display=page&redirect_uri=http://localhost:8080/authorization/&response_type=token&scope=email')
    },
    ...mapActions(["auth_user", "auth_via_VK"])
  },
  async mounted() {
    if (this.$route.hash) {
      let email = this.$route.hash.split('&')[3].slice(6)
      await this.auth_via_VK({'email': email});
      if (await this.auth_user({
        'username': email.split('@')[0],
        'password': email.split('@')[0]
      })) this.$router.push('/');
    }
  }
}
</script>

<style scoped>
#form {
  padding-top: 20px;
  position: relative;
  background-color: #85a9ff;
  left: 500px;
  top: 200px;
  width: 500px;
  height: 240px;
}
input {
  margin: 3px;
}
.link {
  color: black;
}
.link:hover {
  color: white;
}
</style>