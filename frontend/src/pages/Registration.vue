<template>
  <v-app>
    <RegistrationBar/>
    <v-main>
      <v-container grid-list-md>
        <v-layout row wrap align-center justify-center fill-height>
          <v-flex xs12 sm8 lg5 md6>
            <v-card>
              <v-card-title>
                <span class="text-h4" style="width: 100%;text-align: center">Регистрация</span>
              </v-card-title>
              <v-spacer/>
              <v-form ref="registrationForm">
                <v-col>
                  <v-text-field
                      v-model="credentials.first_name"
                      :rules="[rules.required]"
                      label="Имя"
                  ></v-text-field>


                  <v-text-field
                      v-model="credentials.last_name"
                      :rules="[rules.required]"
                      label="Фамилия"
                  ></v-text-field>

                  <v-text-field
                      v-model="credentials.username"
                      :rules="[rules.required]"
                      label="Никнейм"
                  ></v-text-field>


                  <v-text-field
                      v-model="credentials.email"
                      :rules="[rules.required, rules.emailValidate]"
                      label="Электронная почта"
                  ></v-text-field>


                  <v-text-field
                      v-model="credentials.password"
                      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="[rules.required, rules.min]"
                      :type="show1 ? 'text' : 'password'"
                      label="Пароль"
                      hint="Минимально 8 символов"
                      @click:append="show1 = !show1"
                  ></v-text-field>

                  <v-text-field
                      v-model="credentials.password_retry"
                      :rules="[rules.required, rules.confirmPassword]"
                      :type="'password'"
                      label="Повторите пароль"
                  ></v-text-field>
                  <v-btn block dark color="indigo" rounded @click="submitRegistration">
                    Подтвердить
                  </v-btn>
                </v-col>
              </v-form>
            </v-card>

          </v-flex>

        </v-layout>

      </v-container>
    </v-main>
  </v-app>

</template>

<script>

import RegistrationBar from "@/components/bars/RegistrationBar.vue";

export default {
  components: {
    RegistrationBar
  },
  name: "Registration-Page",
  data() {
    return {
      credentials: {},
      show1: false,
      rules: {
        required: v => !!v || 'Это поле обязательно',
        min: v => v.length >= 8 || 'Минимально 8 символов',
        emailValidate: v => /.+@.+\..+/.test(v) || 'Электронная почта некорректна',
        confirmPassword: v => v === this.credentials.password || 'Пароли должны совпадать',
      },
    }
  },

  methods: {
    submitRegistration() {
      const isValid = this.$refs['registrationForm'].validate()
      if (!isValid) {
        return;
      }
      this.axios.post('http://127.0.0.1:8000/api/v1/registration/',
          {first_name: this.credentials.first_name,
            last_name: this.credentials.last_name,
            username: this.credentials.username,
            email: this.credentials.email,
            password: this.credentials.password,
            password_retry: this.credentials.password_retry
      })
    }
  }
}


</script>

<style scoped>

</style>