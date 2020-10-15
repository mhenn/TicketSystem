<template>

	<v-list>
		<v-list-group
			v-for="item in fick"
		>
		
			<template v-slot:activator>
				<v-list-item-content>
					<v-list-item-title v-text="item"></v-list-item-title>
				</v-list-item-content>
			</template>		

			<v-list-item
			>
				<v-list-item-content>
					<v-card>
						OOOO
					</v-card>
				</v-list-item-content>
			</v-list-item>
	
		</v-list-group>
	</v-list>

</template>

<script>


export default {
	name: 'QueueContent',
	data: () => ({
		fick : [1,2,3,4]
	})

}

</script>
