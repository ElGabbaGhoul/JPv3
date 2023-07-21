<script>
	import { onMount } from 'svelte';
	import zxcvbn from 'zxcvbn';

	export let password = '';
	let passwordStrength = null;

	let passwordStrengthColor = {
		0: 'bg-blue-300',
		1: 'bg-red-300',
		2: 'bg-orange-300',
		3: 'bg-yellow-300',
		4: 'bg-green-500'
	};

	// Update the password strength as the user types
	function updatePasswordStrength() {
		passwordStrength = zxcvbn(password);
		console.log(passwordStrength);
	}

	// Example function to perform actions after the component mounts
	onMount(() => {
		// Perform any initial actions or data fetching here
	});
</script>

<input
	class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
	type="password"
	bind:value={password}
	on:input={updatePasswordStrength}
/>
<div class="flex flex-row w-full h-3 rounded-full" />
{#if passwordStrength !== null}
	<div class="flex flex-row w-full">
		<div
			class="{passwordStrength.score
				? passwordStrengthColor[passwordStrength.score]
				: ''} h-3 w-1/4 rounded-l-full"
		/>
		{#if passwordStrength.score > 1}
			<div
				class="{passwordStrength.score
					? passwordStrengthColor[passwordStrength.score]
					: ''} h-3 w-1/4"
			/>
			{#if passwordStrength.score > 2}
				<div
					class="{passwordStrength.score
						? passwordStrengthColor[passwordStrength.score]
						: ''} h-3 w-1/4"
				/>
				{#if passwordStrength.score > 3}
					<div
						class="{passwordStrength.score
							? passwordStrengthColor[passwordStrength.score]
							: ''} h-3 w-1/4 rounded-r-full"
					/>
				{/if}
			{/if}
		{/if}
	</div>
{/if}
