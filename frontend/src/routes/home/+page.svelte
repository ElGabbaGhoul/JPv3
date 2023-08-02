<script>
	import { onMount } from 'svelte';
	import { loginName } from '$lib/stores/stores';

	export let data;

	onMount(() => {
		console.log(data);
	});
</script>

<!-- Display first name only -->
<!-- currently displaying full name -->
<div>Hello {data.name}!</div>
<div>This is where the homepage lives!</div>
