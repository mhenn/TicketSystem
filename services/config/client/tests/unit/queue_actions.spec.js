import sinon , {expect} from "sinon"
import sinonChai from "sinon-chai"
import chai from "chai"

import {testCommitAction, testDispatchAction, mock} from "../testUtils"
import queues_n from '@/store/modules/queues'

chai.use(sinonChai)

const state = {misc :{cloak: {'token': 'id'}}}
let base_url = "http://localhost:5555/config/queues/"

describe("Module: Queue, Reply: 200, Action :", ()=>{
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

describe("Module: Queue, Reply: fail, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getQueues", done =>{

		mock.onGet(base_url).reply(500)
		
		const actionPayload = null

		const expectedMutations = [
			{
				type: 'misc/updateFail',
				payload: 'getQueue'
			}
		]	
		testCommitAction(queues_n.actions.getQueues, actionPayload, state, expectedMutations, done)
	})
	
	it("postQueue", done =>{

		mock.onPost(base_url ).reply(500)
		
		const actionPayload = null

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'postQueue'
			}
		]
		testCommitAction(queues_n.actions.postQueue, actionPayload, state, expectedMutations, done)
	})

	it("deleteQueue", done =>{

		mock.onDelete(base_url + '1').reply(500)
		
		const actionPayload = 1

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'deleteQueue'
			}
		]
		testCommitAction(queues_n.actions.deleteQueue, actionPayload, state, expectedMutations, done)
	})

})

describe("Module: Queue, Reply: timeout, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getQueues", done =>{

		mock.onGet(base_url).timeout()
		
		const actionPayload = null

		const expectedMutations = [
			{
				type: 'misc/updateFail',
				payload: 'getQueue'
			}
		]	
		testCommitAction(queues_n.actions.getQueues, actionPayload, state, expectedMutations, done)
	})
	
	it("postQueue", done =>{

		mock.onPost(base_url ).timeout
		
		const actionPayload = null

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'postQueue'
			}
		]
		testCommitAction(queues_n.actions.postQueue, actionPayload, state, expectedMutations, done)
	})

	it("deleteQueue", done =>{

		mock.onDelete(base_url + '1').timeout()
		
		const actionPayload = 1

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'deleteQueue'
			}
		]
		testCommitAction(queues_n.actions.deleteQueue, actionPayload, state, expectedMutations, done)
	})

})

