<script>
	import HomeIcon from '$lib/components/Icons/HomeIcon.svelte';
	import SearchIcon from '$lib/components/Icons/SearchIcon.svelte';
	import LibraryIcon from '$lib/components/Icons/LibraryIcon.svelte';
	import AccountIcon from '$lib/components/Icons/AccountIcon.svelte';
	import LogoutIcon from '$lib/components/Icons/LogoutIcon.svelte';
	import { isLoggedIn } from '$lib/stores/stores';
	import { browser } from '$app/environment';

	$: {
		if (browser) {
			if (!document.cookie) {
				$isLoggedIn = false;
			}
		}
	}

	const logout = () => {
		$isLoggedIn = false;
		document.cookie = 'access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
	};
</script>

<nav class=" grid grid-cols-1">
	<ul class=" bg-slate-700 flex flex-row px-5 text-white">
		<li><a class="flex flex-row px-2 items-center" href="/home"><HomeIcon />Home</a></li>
		<li><a class="flex flex-row px-1.5 items-center" href="/search"><SearchIcon />Search</a></li>
		<li><a class="flex flex-row px-2 items-center" href="/library"><LibraryIcon />Library</a></li>
		<li>
			<a class="flex flex-row px-1 items-center" href="/account"><AccountIcon />Account</a>
		</li>
		<li class="flex flex-grow justify-end">
			<a class="flex flex-row px-1 items-center bg-slate-700" href="/" on:click={logout}
				><LogoutIcon />Logout</a
			>
		</li>
	</ul>
</nav>
