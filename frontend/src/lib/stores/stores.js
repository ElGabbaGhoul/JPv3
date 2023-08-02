import { browser } from "$app/environment";
import { writable } from "svelte/store";
let initialIsLoggedInValue;

if (browser) {
  const hasAccessTokenCookie = () => {
  const cookies = document.cookie.split(";").map((c) => c.trim());
  return cookies.some((cookie) => cookie.startsWith("access_token="));
  };
  initialIsLoggedInValue = hasAccessTokenCookie();
}

export const isLoggedIn = writable(initialIsLoggedInValue);

export const loginName = writable('')
