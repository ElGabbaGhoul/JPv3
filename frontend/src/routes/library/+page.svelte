<script>
	import { onMount } from 'svelte';
	export let data;

	onMount(async () => {});
</script>

<div>Hello Library</div>
<div>{data.playlist[0].name}</div>
<div>{data.playlist[1].name}</div>
