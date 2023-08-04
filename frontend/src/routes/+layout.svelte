<script>
	import '../app.postcss';
	import NavMenu from '$lib/components/NavMenu.svelte';
	import { isLoggedIn } from '$lib/stores/stores';
	import { onMount } from 'svelte';

	$: {
		if ($isLoggedIn) {
		}
	}

	onMount(async () => {});
</script>

{#if $isLoggedIn == true}
	<NavMenu />
{/if}
<div class="app">
	<main>
		<slot />
	</main>
</div>

<style>
</style>
