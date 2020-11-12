const state = () => ({
	dialog: false,
	failed: []
})

const mutations = {
	switch(state){
		state.dialog = state.dialog ? false : true
	},
	updateFail(state, type){
		if(!state.failed.includes)	
			state.failed.push(type)
	},
	clearFailType(state, type){
		state.failed = state.failed.filter(e => {return e != type})
	},
	clearFail(state){
		state.failed = []
	}
}
const actions = {}

export default{
	namespaced: true,
	state,
	actions,
	mutations
}
