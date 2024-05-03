<template>
  <div id="form">
    <p><img :src="'http://127.0.0.1:8000/auth/user/image/' + user.id" alt="image" :key="img_id"></p>
    <p><input @change='new_file' type="file"></p>
    <p><label>Имя </label><input type="text" v-model="user.username"></p>
    <p><label>Email </label><input type="email" v-model="user.email"></p>
    <p><label>Изменить пароль </label><input type="checkbox" v-model="change_password"></p>
    <p v-if="change_password"><label>Новый пароль </label><input type="password" v-model="user.password"></p>
    <p v-if="change_password"><label>Повторить новый пароль </label><input type="password" v-model="user.check_password"></p>
    <p><button @click="save" class="submit_button">Сохранить</button></p>
    <p><label>Введите пароль </label><input type="password" v-model="current_password"></p>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "account_page",
  data() {
    return {
      user: {
        id: 0,
        username: '',
        email: '',
        password: '',
        check_password: ''
      },
      old_user: {
        id: null,
        user_name: '',
        email: '',
      },
      current_password: '',
      change_password: false,
      img_id: 0
    }
  },
  methods: {
    async save() {
      if (this.old_user.username !== this.user.username) {
        if (await this.edit_username({
          "current_password": this.current_password,
          "new_username": this.user.username
        })) {
          alert('Имя успешно изменено');
          this.old_user.user_name = this.user.username;
        } else alert('Что-то пошло не так')
      }

      if (this.user.password)
        if (this.user.password !== this.user.check_password) alert('Пароли не совпадают')
        else {
          if (await this.edit_password({
            "current_password": this.current_password,
            "new_password": this.user.password
          })) alert('Пароль успешно изменён'); else alert('Что-то пошло не так')
        }

      if (this.old_user.email !== this.user.email) {
        if ((await this.edit_email({
          "current_password": this.current_password,
          "new_email": this.user.email
        })) === 'OK') {
          alert('Email успешно изменён');
          this.old_user.email = this.user.email;
        } else alert('Что-то пошло не так')
      }
    },
    async new_file(event) {
      if ((await this.upload_user_image({'file': event.target.files[0], 'user_id': this.user.id})) === 'OK') {
        this.img_id++;
        alert('Аватарка изменена');
      } else alert('Что-то пошло не так');
    },
    ...mapActions(['get_account_data', 'edit_username', 'edit_email', 'edit_password', 'upload_user_image'])
  },
  async mounted() {
    this.old_user = await this.get_account_data();
    this.user.id = this.old_user.id;
    this.user.email = this.old_user.email;
    this.user.username = this.old_user.username;
  }
}
</script>

<style scoped>
#form {
  padding-top: 10px;
  position: relative;
  background-color: #85a9ff;
  left: 500px;
  top: 100px;
  width: 500px;
  height: 480px;
}
img {
  object-fit: cover;
  width: 120px;
  height: 120px;
  border-radius: 60px;
}
</style>