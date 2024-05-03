<template>
<div>
  <img alt="AeroNet" src="@/assets/flight.jpg">
  <h4>Рейс {{flight.departure_airport.name}}({{flight.departure_airport.city}}) - {{flight.arrival_airport.name}}({{flight.arrival_airport.city}})</h4><br>
  <h5>Самолёт {{flight.aircraft.model}}</h5>
  <h5>Дата отбытия {{ flight.departure_date }}</h5>
  <h5>Дата прибытия {{ flight.arrival_date }}</h5>
  <p><label>Места</label></p>
  <p><span v-for="ticket in tickets" v-bind:key="ticket.id">
    <label>{{ticket.seat.seat_number}}<input type="radio" :value="ticket.id" v-model="selected_ticket"></label>
  </span></p>
  <p><button @click="payment"> Забронировать </button></p>
</div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "flight_page",
  data() {
    return {
      flight: {
        departure_airport: {},
        arrival_airport: {},
        departure_date: '',
        arrival_date: '',
        aircraft: {},
      },
      tickets: [],
      selected_ticket: ''
    }
  },
  props: {
    flight_id: null,
  },
  methods: {
    async payment() {
      if (this.is_auth && this.selected_ticket) {
        let link = 'http://45.147.177.245:8010/success/?';
        link += 'ticket_id=' + this.selected_ticket + '&';
        link += 'user_id=' + (await this.get_account_data()).id;
        await axios.get(link);
        window.location.href = 'http://45.147.177.245:8080/';
      } else if (this.selected_ticket) alert('Чтобы забронировать билет, нужно авторизоваться');
      else alert('Выберите место, которое хотите забронировать');
    },
    ...mapActions(["get_flight", "get_tickets", "get_account_data"])
  },
  async mounted() {
    this.flight = await this.get_flight(this.flight_id);
    this.tickets = await this.get_tickets(this.flight_id)
  },
  computed: {
    ...mapGetters(["is_auth"])
  }
}
</script>

<style scoped>
img {
  width: 500px;
  height: 300px;
}

button {
  font-size: 20px;
  width: 180px;
  height: 40px;
  background-color: #85a9ff;
  border: #85a9ff;
  border-radius: 10px;
}

button:hover {
  background-color: #496dc3;
}
input {
  margin-right: 10px;
}
</style>