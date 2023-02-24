<template>
  <v-app>
    <AuthBar/>
    <v-main>
      <v-container grid-list-md>
        <v-layout row wrap align-center justify-center fill-height>
          <v-flex xs12 sm8 lg4 md5>
            <v-card class="login-card">
              <v-card-title>
                <span class="text-h4" style="width: 100%;text-align: center">Авторизация</span>
              </v-card-title>

              <v-spacer/>

              <v-card-text>

                <v-layout
                    row
                    fill-height
                    justify-center
                    align-center
                    v-if="loading"
                >
                  <v-progress-circular
                      :size="50"
                      color="primary"
                      indeterminate
                  />
                </v-layout>


                <v-form v-else ref="form" v-model="valid" lazy-validation>
                  <v-container>

                    <v-text-field
                        v-model="credentials.username"
                        label="Никнейм"
                        :rules="[rules.required]"
                        maxlength="70"
                        required
                    />

                    <v-text-field
                        type="password"
                        v-model="credentials.password"
                        label="Пароль"
                        :rules="[rules.required]"
                        maxlength="20"
                        required
                    />

                  </v-container>
                  <v-btn block dark color="indigo" rounded :disabled="!valid" @click="login">Войти</v-btn>

                </v-form>


              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import AuthBar from "@/components/bars/AuthBar.vue";

export default {
  components: {
    AuthBar
  },
  name: "Authentication-Page",
  data: () => ({
    credentials: {},
    valid: true,
    loading: false,
    rules: {
      required: v => !!v || 'Это поле обязательно',
      emailValidate: v => /.+@.+\..+/.test(v) || 'Электронная почта некорректна',
      // username: [
      //   v => !!v || "Username is required",
      //   v => (v && v.length > 3) || "A username must be more than 3 characters long",
      //   v => /^[a-z0-9_]+$/.test(v) || "A username can only contain letters and digits"
      // ],
      // password: [
      //   v => !!v || "Password is required",
      //   v => (v && v.length > 7) || "The password must be longer than 7 characters"
      // ]
    }
  }),
  methods: {
    login() {

    }
  }
}
</script>

<style scoped>

</style>