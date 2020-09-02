<template>
	<div class="gate">
		<GateOfHell msg="Abandon all hope, ye who enter here" btnmsg="Venture deeper"/>
	</div>
</template>

<script>

import GateOfHell from '@/components/GateOfHell.vue'

export default {
	name: 'EnterHell',
	components: {
		GateOfHell
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
