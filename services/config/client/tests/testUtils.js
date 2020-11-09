import { expect } from "chai";

export const testCommitAction = (
	action,
	actionPayload,
	rootState,
	expectedMutations,
	done
) => {

	let count = 0
	let commit = (type, payload) => {
		let mutation = expectedMutations[count]
		try {
			expect(mutation.type).to.equal(type)
			if (payload) {
			  expect(mutation.payload).to.deep.equal(payload);
			}
			count++
			if (count == expectedMutations.length) {
				done()
			}
		} catch (error) {
			done(error)
		}
	}

	if (expectedMutations.length === 0) {
		expect(count).to.equal(0)
		done()
	} else {
		action({commit, rootState}, actionPayload)
	}
}


export const testDispatchAction = (
	action,
	actionPayload,
	rootState,
	expectedActions,
	done
) => {
	console.log(action)
	let count = 0
		let dispatch = (type, payload) => {
		
		let d_action = expectedActions[count]
		
		try{
			expect(d_action.type).to.equal(type)
			count++
			if(count == expectedActions.length){
				done()
			}
		} catch (error){
			done(error)
		}
	}

	if (expectedActions.length === 0) {
		expect(count).to.equal(0)
		done()
	} else {
		action({dispatch, rootState}, actionPayload)
	}
}
