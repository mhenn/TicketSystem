<template>
		<v-list-group>
		
			<template v-slot:activator>
				<v-list-item-content>
					<v-list-item-title v-text="title"></v-list-item-title>
				</v-list-item-content>
			</template>		

			<slot></slot>
	
		</v-list-group>

</template>

<script>

export default{
	props:{
		title: String,
		
	}
}

</script>
