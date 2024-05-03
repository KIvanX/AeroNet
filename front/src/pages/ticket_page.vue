<template>
  <img id="img" alt="AeroNet" src="@/assets/flight.jpg">
  <h4>Рейс {{ticket.departure_airport.name}}({{ticket.departure_airport.city}}) - {{ticket.arrival_airport.name}}({{ticket.arrival_airport.city}})</h4><br>
  <h5>Самолёт {{ticket.aircraft.model}}</h5>
  <h5>Дата отбытия {{ ticket.departure_date }}</h5>
  <h5>Дата прибытия {{ ticket.arrival_date }}</h5>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "ticket_page",
  data() {
    return {
      ticket: {}
    }
  },
  mounted() {
    this.ticket = this.get_ticket()
  },
  methods: {
    ...mapActions(['get_ticket'])
  }
}
</script>

<style scoped>

</style>