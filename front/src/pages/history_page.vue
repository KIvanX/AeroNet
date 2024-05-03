<template>
  <div>
    <img id="img" alt="AeroNet" src="@/assets/history.jpg">
    <h2>История</h2>
    <div v-for="booking in bookings" v-bind:key="booking.id">
      <router-link :to="'/flights/' + booking.ticket.flight.id">
        <div class="card">
          <h3>{{booking.ticket.flight.departure_airport.city}} - {{booking.ticket.flight.arrival_airport.city}}
          <button @click="del_booking(booking.id)"> Удалить </button></h3>
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
    async del_booking(booking_id) {
      await this.delete_booking(booking_id);
      this.$router.push('/history');
    },
    ...mapActions(['get_account_data', 'get_bookings', 'delete_booking'])
  }
}
</script>

<style scoped>
img {
  width: 500px;
  height: 300px;
}
</style>