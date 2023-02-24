<template>
    <v-container fluid>
      <v-app-bar

          color="indigo"
          dark
      >
        <div class="d-flex align-center">
          <span class="text-h4" style="width: 100%;text-align: center">uppoint</span>
        </div>
        <v-spacer/>
        <v-btn outlined class="ml-3" color="">
          <router-link to="/auth">Войти</router-link>
        </v-btn>

      </v-app-bar>
    </v-container>
</template>

<script>
export default {
  name: "RegistrationBar"
}
</script>

<style scoped>

</style>