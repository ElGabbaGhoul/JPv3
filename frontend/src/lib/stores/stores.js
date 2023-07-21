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

// Function to check for access token in cookies
// export async function checkCookie() {
//   console.log('Checking for tokens...');
//   const match = document.cookie.match(/(?:^|; )access_token=([^;]*)/);
//   if (match) {
//     const token = match[1];
//     console.log('Token Found!')
//     const isValidToken = validateToken(token);
//     isLoggedIn.set(isValidToken);
//   } else {
//     isLoggedIn.set(false);
//   }
// }

// // Function to validate the access token
// function validateToken(token: string): boolean {
//   // Perform your token validation logic here
//   // Modify this function based on your token structure and validation requirements

//   // Example: Check if the token is not expired
//   const isValid = !isTokenExpired(token);

//   return isValid;
// }

// // Function to check if the token is expired
// function isTokenExpired(token: string): boolean {
//   // Implement your logic to check if the token is expired
//   // Modify this function based on your token structure and expiration date handling

//   // Example: Assuming the token has an 'exp' claim representing the expiration date in Unix timestamp format
//   const expirationDate = getTokenExpirationDate(token);
//   const currentDate = new Date();
//   return expirationDate !== null && expirationDate <= currentDate;
// }

// // Function to extract the token's expiration date
// function getTokenExpirationDate(token: string): Date | null {
//   // Implement your logic to extract the token's expiration date
//   // Modify this function based on your token structure and expiration date handling

//   // Example: Assuming the token has an 'exp' claim representing the expiration date in Unix timestamp format
//   const decodedToken = decodeToken(token);
//   if (decodedToken && decodedToken.exp) {
//     const expirationDate = new Date(decodedToken.exp * 1000);
//     return expirationDate;
//   }

//   // Return null if the expiration date cannot be determined
//   return null;
// }

// // Function to decode the token
// function decodeToken(token: string): any {
//   // Implement your logic to decode the token
//   // Modify this function based on your token structure and decoding library

//   // Example: Using JSON Web Token (JWT) library
//   try {
//     const decodedToken = jwt_decode(token);
//     return decodedToken;
//   } catch (error) {
//     console.error('Failed to decode token:', error);
//     return null;
//   }
// }
