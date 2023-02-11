<template>
  <v-app>
    <v-app-bar
      app
      color="indigo"
      dark
    >
      <div class="d-flex align-center">
        <div class="text-sm-h4">uppoint</div>
      </div>

      <v-spacer></v-spacer>

    </v-app-bar>

    <v-main>
      <Registration/>
    </v-main>
  </v-app>
</template>

<script>


import Registration from "@/components/Registration.vue";

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
