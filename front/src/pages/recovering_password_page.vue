<template>
<div id="form">
  <div v-if="!code">
    <p><label>Email <input v-model="email"></label></p>
    <p><button @click="send">Отправить код</button></p>
  </div>
  <div v-else>
    <p><label>На вашу почту должно прийти письмо с кодом</label></p>
    <p><input v-model="check_code"></p>
    <br>
    <p><label>Новый пароль <input type="password" v-model="password"></label></p>
    <p><label>Повторить новый пароль <input type="password" v-model="check_password"></label></p>
    <p><button @click="save_password" class="submit_button">Сохранить</button></p>
  </div>
</div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "recovering_password_page",
  data() {
    return {
      email: '',
      code: '',
      check_code: '',
      password: '',
      check_password: ''
    }
  },
  methods: {
    async save_password() {
      if (this.code === this.check_code) {
        if (this.password !== this.check_password) alert('Пароли не совпадают');
        else {
          if ((await this.set_recovered_password({
            'email': this.email,
            'password': this.password
          })) === 'OK') {
            this.$router.push('/authorization');
            alert('Пароль восстановлен')
          }
        }
      } else alert('Код не верен');
    },
    async send() {
      this.code = await this.get_recovering_code(this.email)
    },
    ...mapActions(['get_recovering_code', 'set_recovered_password'])
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
  height: 270px;
}
</style>