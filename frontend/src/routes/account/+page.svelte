<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { PUBLIC_BACKEND_USERS } from '$env/static/public';
	import { isLoggedIn } from '$lib/stores/stores';

	export let data;

	async function handleGoToLib() {
		goto('/library');
	}
	$: {
		if ($isLoggedIn) {
		}
	}
	// @ts-ignore
	async function getPlaylistDetails(id) {
		const response = await fetch(`${PUBLIC_BACKEND_USERS}/api/playlist/id/${id}`, {
			method: 'GET',
			headers: { 'Content-Type': 'application/json' }
		});
		// console.log('This is get playlist details', response);
		const details = await response.json();
		// console.log('This is the response', details);
		return details;
	}

	onMount(async () => {});
</script>

{#if $isLoggedIn == true}
	<div class="text-4xl font-bold mt-3 ml-2">Hello {data.name}!</div>

	<div class="mt-10 ml-5">
		<div class="text-xl font-bold mt-2">Your username (email address) is:</div>
		<div class="mt-1 ml-4">{data.username}</div>

		<div class="text-xl font-bold mt-2">Your role is:</div>
		<div class="mt-1 ml-4">{data.role}</div>

		<div class="text-xl font-bold mt-2">Your playlists:</div>
		{#each data.playlists as playlist}
			{#await getPlaylistDetails(playlist)}
				loading
			{:then playlistDetails}
				<div class="mt-1 ml-4">{playlistDetails.name}, {playlistDetails._id}</div>
			{/await}
			{#if data.playlists.length == 0}
				<div class="mt-1 ml-4">
					You currently have no playlists. Head to the library to make some!
				</div>
				<button
					class="ml-4 px-2 py-2 bg-green-400 rounded-lg text-white hover:bg-green-600 hover:underline"
					on:click={handleGoToLib}>Take me there!</button
				>
			{/if}
		{/each}
	</div>
{/if}
