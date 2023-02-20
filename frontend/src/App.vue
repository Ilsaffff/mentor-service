<template>
  <v-app>
    <v-app-bar
      app
      color="indigo"
      dark
    >
      <div class="d-flex align-center">
        <span class="text-h4" style="width: 100%;text-align: center">uppoint</span>
      </div>

      <v-spacer></v-spacer>

    </v-app-bar>

    <v-main>
      <Registration/>
    </v-main>
  </v-app>
</template>

<script>


import Registration from "@/components/pages/Registration.vue";

export default {
  name: 'App',

  components: {
    Registration

  },

  data: () => ({
    //
  }),
};
</script>