- [x] create registration/signup page
  - [x] disallow duplicate emails
  - [x] give token after login when signing up
  - [x] add "loading..." for when awaiting response for login
  - [x] add "loading..." for when awaiting response for signup
  - [ ] implement rate limiting (look in to aioredis)
  - [ ] implement signup form expectations (password strength, valid email, etc)
  - [ ] forgot password
  - [ ] change gap in +page.svelte to fit nav bar properly on smaller screens
  - [ ] while Token, loggedIn===True
- [x] Change login page to request login with email instead of username
- [ ] Create API calls to pull playlists to users from playlist api
- [ ] Import music from external apis
  - [ ] Spotify
  - [ ] Apple Music
  - [ ] SoundCloud
  - [ ] Etc
    - [ ] Add music to user playlists
    - [ ] Play music
- [ ] Setup profile page to render user data
  - [ ] account info
    - [ ] edit profile
    - [ ] pfp
  - [ ] playlists
  - [ ] whatever else a profile might need


next part is getting user details by potentially storing the login return values to either store or cookies so that we can then use it in our get playlists load function in our library routes +page.js