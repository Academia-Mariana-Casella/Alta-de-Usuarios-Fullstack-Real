<script setup>
defineProps({
  form: {
    type: Object,
    required: true,
  },
  errors: {
    type: Object,
    required: true,
  },
  isSubmitting: {
    type: Boolean,
    required: true,
  },
  serverError: {
    type: String,
    default: "",
  },
  successMessage: {
    type: String,
    default: "",
  },
});

const emit = defineEmits(["submit", "update-field"]);

function onInput(field, event) {
  emit("update-field", { field, value: event.target.value });
}
</script>

<template>
  <section class="card">
    <h1 class="title">Alta de Usuarios</h1>
    <p class="subtitle">Primer caso de uso del ABM: registro de usuario.</p>

    <div v-if="serverError" class="server-error">{{ serverError }}</div>
    <div v-if="successMessage" class="success-box">{{ successMessage }}</div>

    <form @submit.prevent="emit('submit')">
      <div class="field">
        <label for="email">E-mail</label>
        <input
          id="email"
          type="email"
          autocomplete="email"
          :value="form.email"
          @input="onInput('email', $event)"
        />
        <span v-if="errors.email" class="error-text">{{ errors.email }}</span>
      </div>

      <div class="field">
        <label for="password">Contrasena</label>
        <input
          id="password"
          type="password"
          autocomplete="new-password"
          :value="form.password"
          @input="onInput('password', $event)"
        />
        <span v-if="errors.password" class="error-text">{{ errors.password }}</span>
      </div>

      <div class="field">
        <label for="repeatPassword">Repetir contrasena</label>
        <input
          id="repeatPassword"
          type="password"
          autocomplete="new-password"
          :value="form.repeatPassword"
          @input="onInput('repeatPassword', $event)"
        />
        <span v-if="errors.repeatPassword" class="error-text">{{ errors.repeatPassword }}</span>
      </div>

      <div class="button-row">
        <button class="submit-btn" type="submit" :disabled="isSubmitting">
          {{ isSubmitting ? "Registrando..." : "Registrar usuario" }}
        </button>
      </div>
    </form>
  </section>
</template>

