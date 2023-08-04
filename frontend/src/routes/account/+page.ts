// import { userId } from '$store/stores'
// import { writable } from "svelte/store";
// import { loginName } from '$lib/stores/stores.js'
import { browser } from '$app/environment'
import { PUBLIC_BACKEND_USERS } from '$env/static/public'

export const prerender = true
// async function getAccountDetails(accessToken) {
// 	let data = null
// 	if (typeof localStorage !== 'undefined') {
// 		const response = await fetch(`${PUBLIC_BACKEND-USERS}/accounts/profile`, {
// 			headers: {
// 				Authorization: `Bearer ${accessToken}`
// 			}
// 		})
// 		data = await response.json()
// 		localStorage.setItem('userIdentity', JSON.stringify(data))
// 		userId.set(data._id)
// 		return data
// 	}
// }

// let loggedInUser: any = null;
// loginName.subscribe((value) => {
//   console.log(value)
//   loggedInUser = value
// })

export const load = async ({ fetch }) => {
  const getAccountDetails = async () => {
    let accessToken
		if (browser) {
			accessToken = document.cookie.split('=')[1]
			// console.log('accesstoken within my homes +page.js', accessToken.split('.'))
		}
		const response = await fetch(`${PUBLIC_BACKEND_USERS}/accounts/profile`, {
			headers: {
				Authorization: `Bearer ${accessToken}`
			}
		})
		const data = await response.json()
		return data
	}

	return getAccountDetails()
}