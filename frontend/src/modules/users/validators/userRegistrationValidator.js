const EMAIL_REGEX = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;

export function validateUserRegistrationForm(form) {
  const errors = {};

  if (!form.email?.trim()) {
    errors.email = "El e-mail es obligatorio.";
  } else if (!EMAIL_REGEX.test(form.email.trim())) {
    errors.email = "Formato de e-mail invalido.";
  }

  if (!form.password) {
    errors.password = "La contrasena es obligatoria.";
  } else if (form.password.length < 8) {
    errors.password = "La contrasena debe tener al menos 8 caracteres.";
  }

  if (!form.repeatPassword) {
    errors.repeatPassword = "Debes repetir la contrasena.";
  } else if (form.password !== form.repeatPassword) {
    errors.repeatPassword = "Las contrasenas deben ser iguales.";
  }

  return errors;
}
