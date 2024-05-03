<template>
  <div>
    <img id="img" alt="AeroNet" src="@/assets/history.jpg">
    <h2>История</h2>
    <div v-for="booking in bookings" v-bind:key="booking.id">
      <router-link :to="'/flights/' + booking.ticket.flight.id">
        <div class="card">
          <h3>{{booking.ticket.flight.departure_airport.city}} - {{booking.ticket.flight.arrival_airport.city}}</h3>
          <button @click="del_ticket(booking.id)"> Удалить </button>
          <br>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "history_page",
  data() {
    return {
      bookings: []
    }
  },
  async mounted() {
    let user_id = (await this.get_account_data()).id
    console.log(user_id)
    this.bookings = await this.get_bookings(user_id)
    console.log(this.bookings)
  },
  methods: {
    async del_ticket(ticket_id) {
      await this.delete_ticket(ticket_id);
      window.location.href = 'http://45.147.177.245:8080/';
    },
    ...mapActions(['get_account_data', 'get_bookings', 'delete_ticket'])
  }
}
</script>

<style scoped>
img {
  width: 500px;
  height: 300px;
}
</style>