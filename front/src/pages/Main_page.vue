<template>
  <img id="logo" alt="AeroNet" src="@/assets/logo.png">
  <h1 class="">Добро пожаловать на сайт AeroNet</h1>
  <label>Откуда <input v-model="filter.from"></label> <label>Куда <input v-model="filter.to"></label>
  <div v-for="fl in flights" v-bind:key="fl.id">
    <router-link :to="'/flights_date/' + fl.id">
      <div class="card">
        <h3>{{fl.departure_airport.city}} - {{fl.arrival_airport.city}}</h3><br>
      </div>
    </router-link>
  </div>
  <div class="nav">
    <button @click="prev_page">Назад</button> <label>{{filter.page}}</label> <button @click="next_page">Вперёд</button>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: 'Main_page',
  data() {
    return {
      flights: [],
      filter: {}
    }
  },
  methods: {
    async prev_page() {
      if (this.filter.page > 1) this.filter.page -= 1;
    },
    async next_page() {
      this.filter.page += 1;
    },
    ...mapActions(["get_flights", "set_filter"])
  },
  async mounted() {
    this.filter = this.get_filter;
    this.flights = await this.get_flights(this.filter);
  },
  watch: {
    filter: {
      async handler() {
        this.flights = await this.get_flights(this.filter);
        this.set_filter(this.filter)
      },
      deep: true
    }
  },
  computed: {
    ...mapGetters(["get_filter"])
  }
}
</script>

<style scoped>
#logo {
  width: 400px;
  height: 100px;
}
button {
  width: 100px;
  height: 30px;
  background-color: #85a9ff;
  border-radius: 10px;
  border: #85a9ff;
}
button:hover {
  background-color: #496dc3;
}
.nav {
  margin-top: 20px;
}
</style>
