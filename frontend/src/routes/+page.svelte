<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import PasswordStrengthMeter from '$lib/components/PasswordStrengthMeter.svelte';
	import { PUBLIC_BACKEND_USERS } from '$env/static/public';
	import WaveComponent from '$lib/components/WaveComponent.svelte';
	import { isLoggedIn, loginName } from '$lib/stores/stores';
	import Resume from '$lib/components/Resume.svelte';

	let isMouseOver = false;

	function handleMouseOver() {
		isMouseOver = true;
	}

	function handleMouseOut() {
		isMouseOver = false;
	}

	let isLoading = false;

	let username = '';
	let password = '';
	let accessToken = '';

	let showSignUpForm = false;

	async function handleLogin() {
		isLoading = true;
		const formData = new FormData();
		formData.append('username', username);
		formData.append('password', password);

		try {
			const response = await fetch(`${PUBLIC_BACKEND_USERS}/token`, {
				method: 'POST',
				body: formData
			});
			if (response.ok) {
				const data = await response.json();
				accessToken = data.access_token;
				console.log('Access Token: ', accessToken);
				document.cookie = `access_token=${encodeURIComponent(accessToken)}`;
				$loginName = username;
				$isLoggedIn = true;
				goto('/account');
			} else {
				console.error('Login failed');
				console.log(response.status);
				// Handle login failure
			}
		} catch (error) {
			console.error('An error occurred during login:', error);
			// Handle error
		} finally {
			isLoading = false;
		}
	}

	let signupPassword = '';
	let signupEmail = '';
	let signupName = '';
	let signupProfilePic = '';

	async function handleSignUp() {
		isLoading = true;
		const formData = new FormData();
		formData.append('email', signupEmail);
		formData.append('name', signupName);
		formData.append('profile_picture', signupProfilePic);
		formData.append('role', 'User');
		formData.append('hashed_password', signupPassword);

		const payload = {
			username: signupEmail,
			name: signupName,
			profile_picture: signupProfilePic,
			role: 'User',
			hashed_password: signupPassword
		};

		try {
			const response = await fetch(`${PUBLIC_BACKEND_USERS}/api/user`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(payload)
			});
			if (response.ok) {
				const data = await response.json();
				username = signupEmail;
				password = signupPassword;
				await handleLogin();
				console.log('Account creation successful! Logging you in...');
				alert('Account creation successful! Logging you in...');

				// Handle success, e.g., display a success message
			} else {
				const responseData = await response.json();
				if (response.status === 409) {
					console.error('User already exists');
					alert('A user with that email address already exists. Try another email address.');
					signupEmail = '';
					signupPassword = '';
					signupName = '';
					signupProfilePic = '';
				}
				// Handle failure, e.g., display an error message
			}
		} catch (error) {
			console.error('An error occurred during account creation:', error);
			// Handle error, e.g., display an error message
		} finally {
			isLoading = false;
		}
	}

	function toggleSignUpForm() {
		showSignUpForm = !showSignUpForm;
	}

	// Example function to perform actions after the component mounts
	onMount(async () => {});
</script>

<!-- // Retrieve the access token from the cookie
const cookies = document.cookie.split(';');
let storedAccessToken = null; -->

<!-- for (let cookie of cookies) {
  const [name, value] = cookie.trim().split('=');
  if (name === 'access_token') {
    storedAccessToken = decodeURIComponent(value);
    break;
  }
}

console.log('Stored Access Token:', storedAccessToken); -->

<svelte:head>
	<title>Welcome to JamPack'd</title>
	<meta name="description" content="JamPack'd! Create playlists from every music library!" />
</svelte:head>

<main class="flex items-center justify-center min-h-screen bg-gray-100">
	<div class="bg-white p-8 rounded shadow-md w-96">
		<div
			class="flex flex-row w-full justify-center font-bold text-[28px] whitespace-nowrap text-rainbow"
		>
			Welcome to JamPack'd!
		</div>
		{#if isLoading}
			<div class="loader flex flex-row gap-1"><WaveComponent /><WaveComponent /></div>
		{:else}
			{#if !showSignUpForm}
				<!-- Login Form -->
				<h1 class="text-2xl font-semibold mb-6">Login</h1>
				<form on:submit|preventDefault={handleLogin}>
					<div class="mb-4">
						<label for="username" class="block text-sm font-medium text-gray-700"
							>Email Address</label
						>
						<input
							type="text"
							id="username"
							class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
							bind:value={username}
							required
						/>
					</div>
					<div class="mb-6">
						<label for="password" class="block text-sm font-medium text-gray-700">Password</label>
						<input
							type="password"
							id="password"
							class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
							bind:value={password}
							required
						/>
					</div>
					<button
						type="submit"
						class="w-full py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
					>
						Login
					</button>
				</form>
			{:else}
				<!-- Signup Form -->
				<div class="mt-4">
					<h2 class="text-xl font-semibold mb-2">Sign up</h2>
					<form on:submit|preventDefault={handleSignUp}>
						<div class="mb-4">
							<label for="signup-username" class="block text-sm font-medium text-gray-700"
								>Email Address</label
							>
							<input
								type="text"
								id="signup-username"
								class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
								bind:value={signupEmail}
								required
							/>
						</div>
						<div class="mb-4">
							<label for="signup-password" class="block text-sm font-medium text-gray-700"
								>Password</label
							>
							<!-- <input
								type="password"
								id="signup-password"
								class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
								bind:value={signupPassword}
								required
							/> -->
							<PasswordStrengthMeter bind:password={signupPassword} />
						</div>
						<div class="mb-4">
							<label for="signup-name" class="block text-sm font-medium text-gray-700">Name</label>
							<input
								type="text"
								id="signup-name"
								class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
								bind:value={signupName}
								required
							/>
						</div>
						<div class="mb-6">
							<label for="signup-profile-pic" class="block text-sm font-medium text-gray-700"
								>Profile Picture (optional)</label
							>
							<input type="file" id="signup-profile-pic" bind:value={signupProfilePic} />
						</div>
						<button
							type="submit"
							class="w-full py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
						>
							Create Account
						</button>
					</form>
				</div>
			{/if}

			<button
				class="w-full py-2 px-4 mt-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
				on:click={toggleSignUpForm}
			>
				{#if showSignUpForm}
					Back to Login
				{:else}
					Sign up
				{/if}
			</button>
		{/if}
		<div
			class="{isMouseOver
				? 'text-rainbow'
				: ''} text-black w-32 mx-auto flex justify-center items-center mt-10 bg-gray-300 rounded"
			role="button"
			tabindex="0"
			on:mouseover={handleMouseOver}
			on:mouseout={handleMouseOut}
			on:focus={handleMouseOver}
			on:blur={handleMouseOut}
		>
			<a href="https://www.buymeacoffee.com/scnideffer">Buy me a coffee!</a>
		</div>
	</div>
</main>

<style>
	.text-rainbow {
		background-image: linear-gradient(
			to right,
			red,
			red,
			orange,
			yellow,
			green,
			rgb(23, 23, 216),
			indigo,
			violet,
			indigo,
			rgb(23, 23, 216),
			green,
			yellow,
			orange,
			red
		);
		-webkit-background-clip: text;
		background-clip: text;
		background-size: 200% auto;
		color: transparent;
		animation: rainbow-animation 3s linear infinite;
	}

	@keyframes rainbow-animation {
		0% {
			background-position: 100% 50%;
		}
		100% {
			background-position: -100% 50%;
		}
	}
</style>
