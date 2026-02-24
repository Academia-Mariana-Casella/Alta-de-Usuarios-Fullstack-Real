import { API_BASE_URL } from "../../../config/api";

export async function registerUser(payload) {
  const response = await fetch(`${API_BASE_URL}/api/users/register/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const body = await response.json().catch(() => ({}));

  if (!response.ok) {
    const error = new Error("User registration request failed.");
    error.errors = body.errors ?? {};
    throw error;
  }

  return body.data;
}

