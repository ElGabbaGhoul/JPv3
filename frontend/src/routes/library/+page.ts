import { browser } from '$app/environment'
import { PUBLIC_BACKEND_USERS } from '$env/static/public'

export const prerender = true

export const load = async ({ fetch }) => {
  const getPlaylists = async () => {
    let accessToken
    if (browser) {
      accessToken = document.cookie.split('=')[1]
    }
    const response = await fetch(`${PUBLIC_BACKEND_USERS}/accounts/profile/items`, {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    })
    console.log('LIBRARY RESPONSE HERE', response)
    // if (!response.ok) {
    //   const errorText = await response.text()
    //   throw new Error(`Failed to fetch playlists. Response status: ${response.status}. Response body: ${errorText}`)
    // }
    const playlist = await response.json()
    return {playlist}
  }


  // try {
  //   const playlists = await getPlaylists()
  //   return { playlists } // Wrap the playlists data in an object
  // } catch (error: Error) {
  //   console.error('Error fetching playlists:', error.message)
  //   throw error
  // }
  
  return getPlaylists()

}


