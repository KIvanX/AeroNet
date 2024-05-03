<template>
<div>
  <img id="logo" alt="AeroNet" src="@/assets/logo.png">
  <h3>Рейс {{temp.departure_airport.city}} - {{temp.arrival_airport.city}}</h3><br>
  <div v-for="fl in flights" v-bind:key="fl.id">
    <router-link :to="'/flights/' + fl.id">
      <div class="card">
        <h3>{{fl.departure_airport.name}} - {{fl.arrival_airport.name}} {{fl.departure_date}}</h3><br>
      </div>
    </router-link>
  </div>
</div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "flight_page",
  data() {
    return {
      temp: {
        departure_airport: {city: ''},
        arrival_airport: {city: ''}
      },
      flights: {}
    }
  },
  props: {
    flight_id: null,
  },
  methods: {
    ...mapActions(["get_flight", "get_flights"])
  },
  async mounted() {
    this.temp = await this.get_flight(this.flight_id);
    this.flights = await this.get_flights({
      from: this.temp.departure_airport.city,
      to: this.temp.arrival_airport.city
    });
  },
}
</script>

<style scoped>
#img {
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
</style>