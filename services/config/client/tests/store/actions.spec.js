import sinon , {expect} from "sinon"
import sinonChai from "sinon-chai"
import chai from "chai"
import axios from "axios"
import MockAdapter from "axios-mock-adapter"

import {testAction} from "/testUtils"

import store from "@/store"

let mock - new MockAdapter(axios)



chai.use(sinonChai)

describe("actions", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("should process payload and commits mutation for succesfull GET", done =>{
		
		const response = {
			data: {"queues" : [ 
				{'id': '123', 'title': 'test_queue_1'},
				{'id': '456', 'title': 'test_queue_2'}
			]}
		}

		mock.onGet("http://localhost:5555/config/queues/").reply(200, response)
		
		const actionPayload = null
		const state = { queues: []}

		const expectedMutations =[
			{
				type: 'getQueues',
				payload: response
			},
			{
				type: 'updateQueues',
				payload: response.data.queues
			}
		]
		testAction(getQueues,actionPayload, state, expectedMutations )

	})
})

