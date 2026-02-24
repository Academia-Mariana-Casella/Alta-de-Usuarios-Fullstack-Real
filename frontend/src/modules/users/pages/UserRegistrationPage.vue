<script setup>
import UserRegistrationForm from "../components/UserRegistrationForm.vue";
import { useUserRegistration } from "../composables/useUserRegistration";

const {
  form,
  errors,
  isSubmitting,
  successMessage,
  serverError,
  updateField,
  submit,
} = useUserRegistration();
</script>

<template>
  <UserRegistrationForm
    :form="form"
    :errors="errors"
    :is-submitting="isSubmitting"
    :server-error="serverError"
    :success-message="successMessage"
    @update-field="updateField"
    @submit="submit"
  />
</template>

