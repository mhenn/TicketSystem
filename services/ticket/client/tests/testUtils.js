/*eslint-disable*/
import { expect } from "chai";

import axios from "axios"
import MockAdapter from "axios-mock-adapter"
export var mock = new MockAdapter(axios)


export const testCommitAction = (
	action,
	actionPayload,
	rootState,
	expectedMutations,
	done
) => {
	let state = rootState
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
		action({commit, rootState, state}, actionPayload)
	}
}


export const testDispatchAction = (
	action,
	actionPayload,
	rootState,
	expectedActions,
	done
) => {
	let state = rootState
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
		action({dispatch, rootState, state}, actionPayload)
	}
}
