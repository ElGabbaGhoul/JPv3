<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	export let data;

	async function handleGoToLib() {
		goto('/library');
	}

	onMount(async () => {
		console.log(data);
	});
</script>

<div class="text-4xl font-bold mt-3 ml-2">Hello {data.name}!</div>

<div class="mt-10 ml-5">
	<div class="text-xl font-bold mt-2">Your username(email address) is:</div>
	<div class="mt-1 ml-4">{data.username}</div>

	<div class="text-xl font-bold mt-2">Your role is:</div>
	<div class="mt-1 ml-4">{data.role}</div>

	<div class="text-xl font-bold mt-2">Your playlists:</div>
	<div class="mt-1 ml-4">{data.playlists}</div>
	{#if data.playlists.length == 0}
		<div class="mt-1 ml-4">You currently have no playlists. Head to the library to make some!</div>
		<button
			class="ml-4 px-2 py-2 bg-green-400 rounded-lg text-white hover:bg-green-600 hover:underline"
			on:click={handleGoToLib}>Take me there!</button
		>
	{/if}
</div>
