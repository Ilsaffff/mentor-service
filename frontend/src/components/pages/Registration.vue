<template>
  <v-container>
    <v-layout row wrap align-center justify-center fill-height>
      <v-flex xs12 sm8 lg5 md6>
        <v-card-title>
          <span class="text-h4" style="width: 100%;text-align: center">Регистрация</span>
        </v-card-title>
        <v-spacer/>
        <v-form ref="registrationForm">
          <v-col>
            <v-text-field
                v-model="credentials.firstName"
                :rules="[rules.required]"
                label="Имя"
            ></v-text-field>


            <v-text-field
                v-model="credentials.lastName"
                :rules="[rules.required]"
                label="Фамилия"
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
                :rules="[rules.required, rules.confirmPassword]"
                :type="'password'"
                label="Повторите пароль"
            ></v-text-field>
            <v-btn block color="indigo" rounded @click="submitRegistration">
              Подтвердить
            </v-btn>
          </v-col>
        </v-form>

      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>

export default {
  name: "registration-user",
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
    }
  }
}


</script>

<style scoped>

</style>