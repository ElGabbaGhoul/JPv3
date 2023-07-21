// import { userId } from '$store/stores'
// import { browser } from '$app/environment'
// import { PUBLIC_BACKEND_PLAYLISTS } from '$env/static/public'

// export const prerender = true


// export const load = async ({ fetch }) => {
//   const getUser = async () => {
//     const
//   }

// 	const getPlaylists = async () => {
// 		const response = await fetch(`${PUBLIC_BACKEND_PLAYLISTS}/api/playlist`)
// 		const data = await response.json()
// 		return data
// 	}


	// const getAccountDetails = async () => {
	// 	let accessToken
	// 	if (browser) {
	// 		accessToken = document.cookie.split('=')[1]
	// 		console.log('accesstoken within my homes +page.js', accessToken.split('.'))
	// 	}
	// 	const response = await fetch(`${PUBLIC_BACKEND_USERS}/accounts/profile`, {
	// 		headers: {
	// 			Authorization: `Bearer ${accessToken}`
	// 		}
	// 	})
	// 	const data = await response.json()
	// 	return data
	// }

// 	return {
// 		playlists: getPlaylists()
// 		// identity: getAccountDetails()
// 	}
// }