<script>
	import { onMount } from 'svelte';
	export let data;

	onMount(async () => {
		console.log(data);
	});
</script>

<div>Hello Library</div>
<div>This is where your library of playlists will go.</div>
