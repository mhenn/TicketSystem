import sinon , {expect} from "sinon"
import sinonChai from "sinon-chai"
import chai from "chai"
import axios from "axios"
import MockAdapter from "axios-mock-adapter"

import {testCommitAction, testDispatchAction} from "../testUtils"
import queues_n from '@/store/modules/queues'

let mock = new MockAdapter(axios)

chai.use(sinonChai)

let base_url = "http://localhost:5555/config/queues/"

describe("Module: Queue, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getQueues", done =>{
		
		const response = {
			queues : [ 
				{'id': '123', 'title': 'test_queue_1'},
				{'id': '456', 'title': 'test_queue_2'}
			]
		}

		mock.onGet(base_url).reply(200, response)
		
		const actionPayload = null
		const state = {cloak: {'token': 'id'}}

		const expectedMutations =[
			{
				type: 'updateQueues',
				payload: response.queues
			}
		]	
		testCommitAction(queues_n.actions.getQueues, actionPayload, state, expectedMutations, done)
	})
	
	it("postQueue", done =>{

		mock.onPost(base_url ).reply(200)
		
		const actionPayload = null
		const state = {cloak : {'token': 'id'}}

		const expectedActions =
		[
			{
				type: 'getQueues',
				payload: null
			}
		]
		testDispatchAction(queues_n.actions.postQueue, actionPayload, state, expectedActions, done)
	})

	it("deleteQueue", done =>{

		mock.onDelete(base_url + '1').reply(200)
		
		const actionPayload = 1
		const state = {cloak : {'token': 'id'}}

		const expectedActions =
		[
			{
				type: 'getQueues',
				payload: null
			}
		]
		testDispatchAction(queues_n.actions.deleteQueue, actionPayload, state, expectedActions, done)
	})

})

