import { reactive, ref } from "vue";

import { registerUser } from "../services/userService";
import { validateUserRegistrationForm } from "../validators/userRegistrationValidator";

export function useUserRegistration() {
  const form = reactive({
    email: "",
    password: "",
    repeatPassword: "",
  });

  const errors = reactive({});
  const isSubmitting = ref(false);
  const successMessage = ref("");
  const serverError = ref("");

  function clearErrors() {
    for (const key of Object.keys(errors)) {
      delete errors[key];
    }
  }

  function setErrors(nextErrors) {
    clearErrors();
    for (const [key, value] of Object.entries(nextErrors)) {
      errors[key] = value;
    }
  }

  function updateField({ field, value }) {
    form[field] = value;
    if (errors[field]) {
      delete errors[field];
    }
  }

  async function submit() {
    successMessage.value = "";
    serverError.value = "";

    const formErrors = validateUserRegistrationForm(form);
    setErrors(formErrors);

    if (Object.keys(formErrors).length > 0) {
      return;
    }

    isSubmitting.value = true;
    try {
      const createdUser = await registerUser({
        email: form.email,
        password: form.password,
        repeat_password: form.repeatPassword,
      });

      successMessage.value = `Usuario creado: ${createdUser.email}`;
      form.email = "";
      form.password = "";
      form.repeatPassword = "";
      clearErrors();
    } catch (error) {
      if (error?.errors) {
        setErrors(mapBackendErrors(error.errors));
      } else {
        serverError.value = "No se pudo registrar el usuario. Intenta de nuevo.";
      }
    } finally {
      isSubmitting.value = false;
    }
  }

  return {
    form,
    errors,
    isSubmitting,
    successMessage,
    serverError,
    updateField,
    submit,
  };
}

function mapBackendErrors(backendErrors) {
  const mapped = {};
  if (backendErrors.email) {
    mapped.email = backendErrors.email;
  }
  if (backendErrors.password) {
    mapped.password = backendErrors.password;
  }
  if (backendErrors.repeat_password) {
    mapped.repeatPassword = backendErrors.repeat_password;
  }
  return mapped;
}

