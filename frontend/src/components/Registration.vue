<template>
  <v-container>

    <v-form ref="registrationForm">
      <div class="text-sm-h4" align="center">Регистрация</div>
      <v-col align="center" md="4">
        <v-text-field
            v-model="firstName"
            :rules="[rules.required]"
            label="Имя"
            required
        ></v-text-field>


        <v-text-field
            v-model="lastName"
            :rules="[rules.required]"
            label="Фамилия"
            required
        ></v-text-field>


        <v-text-field
            v-model="email"
            :rules="[rules.required, rules.emailValidate]"
            label="Электронная почта"
            required
        ></v-text-field>


        <v-text-field
            v-model="password1"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            label="Пароль"
            hint="Минимально 8 символов"
            @click:append="show1 = !show1"
        ></v-text-field>

        <v-text-field
            v-model="password2"
            :rules="[rules.required, rules.confirmPassword]"
            :type="'password'"
            label="Повторите пароль"
        ></v-text-field>
        <v-btn block color="indigo" rounded @click="submitRegistration">
          Подтвердить
        </v-btn>
      </v-col>
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: "registration-user",
  data() {
    return {
      firstName: null,
      lastName: null,
      email: null,
      password1: null,
      password2: null,
      show1: false,
      rules: {
        required: v => !!v || 'Это поле обязательно',
        min: v => v.length >= 8 || 'Минимально 8 символов',
        emailValidate: v => /.+@.+\..+/.test(v) || 'Электронная почта некорректна',
        confirmPassword: v => v === this.password1 || 'Пароли должны совпадать',
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