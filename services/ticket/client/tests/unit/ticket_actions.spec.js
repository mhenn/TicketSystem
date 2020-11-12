/*eslint-disable */
import sinon , {expect} from "sinon"
import sinonChai from "sinon-chai"
import chai from "chai"

import {testCommitAction, testDispatchAction, mock} from "../testUtils"
import module from '@/store/modules/ticket'

chai.use(sinonChai)

var state = {}
const base_url = module.base_url


describe("Module: Ticket, Reply: 200, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
		state = {config :{cloak: {'token': 'id'}}}
	})

	it("getTickets", done =>{
		
		const response = {
			ticket : [ 
				{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
				{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]},
			]
		}

		mock.onGet(base_url).reply(200, response)
		
		const actionPayload = null

		const expectedMutations =[
			{
				type: 'update',
				payload: response.ticket
			}
		]	
		testCommitAction(module.actions.getTickets, actionPayload, state, expectedMutations, done)
	})
	
	it("postSelected", done =>{
		mock.onPost(base_url ).reply(200)
		
		const actionPayload = null
		state.selectedTicket = {'to':''}
		
		const expectedActions =
		[
			{
				type: 'getTickets',
				payload: null
			}
		]
		testDispatchAction(module.actions.postSelected, actionPayload, state, expectedActions, done)
	})

	it("putSelected", done =>{

		mock.onPut(base_url + '1').reply(200)
		
		const actionPayload = 1

		const expectedActions =
		[
			{
				type: 'getTickets',
				payload: null
			}
		]
		testDispatchAction(module.actions.putSelected , actionPayload, state, expectedActions, done)
	})

})

describe("Module: Mapping, Reply: fail, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getMappings", done =>{

		mock.onGet(base_url).reply(500)
		
		const actionPayload = null

		const expectedMutations = [
			{
				type: 'misc/updateFail',
				payload: 'getMappings'
			}
		]	
		testCommitAction(module.actions.getMappings, actionPayload, state, expectedMutations, done)
	})
	
	it("postMapping", done =>{

		mock.onPost(base_url ).reply(500)
		
		const actionPayload = null

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'postMapping'
			}
		]
		testCommitAction(module.actions.postMapping, actionPayload, state, expectedMutations, done)
	})

	it("deleteMapping", done =>{

		mock.onDelete(base_url + '1').reply(500)
		
		const actionPayload = 1

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'deleteMapping'
			}
		]
		testCommitAction(module.actions.deleteMapping, actionPayload, state, expectedMutations, done)
	})

})

describe("Module: Queue, Reply: timeout, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getMappingss", done =>{

		mock.onGet(base_url).timeout()
		
		const actionPayload = null

		const expectedMutations = [
			{
				type: 'misc/updateFail',
				payload: 'getMappings'
			}
		]	
		testCommitAction(module.actions.getMappings, actionPayload, state, expectedMutations, done)
	})
	
	it("postMapping", done =>{

		mock.onPost(base_url ).timeout
		
		const actionPayload = null

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'postMapping'
			}
		]
		testCommitAction(module.actions.postMapping, actionPayload, state, expectedMutations, done)
	})

	it("deleteMapping", done =>{

		mock.onDelete(base_url + '1').timeout()
		
		const actionPayload = 1

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'deleteMapping'
			}
		]
		testCommitAction(module.actions.deleteMapping, actionPayload, state, expectedMutations, done)
	})

})

