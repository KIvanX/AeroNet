<template>
  <div id="form">
    <p><label>Имя </label><input type="text" v-model="form.name"></p>
    <p><label>Email </label><input type="email" v-model="form.email"></p>
    <p><label>Пароль </label><input type="password" v-model="form.password"></p>
    <p><label>Повторить пароль </label><input type="password" v-model="check_password"></p>
    <p><button class="submit_button" @click="submit">Зарегистрироваться</button></p>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "registration_page",
  data() {
    return {
      form: {
        name: '',
        email: '',
        password: '',
      },
      check_password: ''
    }
  },
  methods: {
    async submit() {
      if (this.form.password !== this.check_password) alert('Пароли не совпадают')
      else {
        if (await this.user_register({
          "email": this.form.email,
          "username": this.form.name,
          "password": this.form.password})) alert('Регистрация прошла успешно');
        else alert('Что-то пошло не так')
      }
    },
    ...mapActions(["user_register"])
  }
}
</script>

<style scoped>
#form {
  padding-top: 10px;
  position: relative;
  background-color: #85a9ff;
  left: 500px;
  top: 200px;
  width: 500px;
  height: 270px;
}
input {
  margin: 3px;
}

</style>