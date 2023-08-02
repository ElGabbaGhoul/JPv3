import { writable } from 'svelte/store'

export const store = writable({
  user: {},
  tenantDetail: {},
})