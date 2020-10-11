<template>
	<Inferno>
		<iframe src="http://localhost:8000/auth/realms/Odonata/account"></iframe>
	</Inferno>
</template>

<script>

import Inferno from '@/components/Inferno'

export default {
	name: 'Settings',
	components: {
		Inferno
	}
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
