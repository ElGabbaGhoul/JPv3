<script>
	import { onMount } from 'svelte';
	export let data;

	onMount(async () => {
		console.log('library loading', data);
		console.log(data.playlist[0].name);
	});
</script>

<div>Hello Library</div>
<div>{data.playlist[0].name}</div>
