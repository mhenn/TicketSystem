/* eslint-disable */
import sinon , {expect} from "sinon"
import sinonChai from "sinon-chai"
import chai from "chai"

import {testCommitAction, mock} from "../testUtils"
import module from '@/store/modules/config'

chai.use(sinonChai)
const mapping_url = 'http://localhost:5070/gateway/config/role-mapping/'
const queue_url = 'http://localhost:5070/gateway/queues/' 
const state = {cloak: {'token': 'id'}}

describe("Module: Config, Reply: 200, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getMappings", done =>{	
		const response = {
			mapping : [ 
				{'id': '123', 'name': 'test_module_1', 'children': ['1','2']},
				{'id': '456', 'name': 'test_module_2', 'children': ['3']},
				{'id': '789', 'name': 'test_module_3', 'children': []}
			]
		}
		mock.onGet(mapping_url).reply(200, response)
		
		const actionPayload = null
		const expectedMutations =[
			{
				type: 'updateMapping',
				payload: response.mapping
			}
		]	
		testCommitAction(module.actions.getMappings, actionPayload, state, expectedMutations, done)
	})
	
	it("getQueues", done =>{
			
		const actionPayload = null
	
		const response = {
			queues : [ 
				{'id': '123', 'title': 'test_module_1'},
			]
		}
		
		mock.onGet(queue_url ).reply(200, response)

		const expectedMutations =
		[
			{
				type: 'updateQueues',
				payload: response.queues
			}
		]

		testCommitAction(module.actions.getQueues , actionPayload, state, expectedMutations, done)
	})
})

describe("Module: Config, Reply: fail, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getMappings", done =>{
		mock.onGet(mapping_url).reply(500)
		
		const actionPayload = null

		const expectedMutations = [
			{
				type: 'misc/updateFail',
				payload: 'getMappings'
			}
		]	
		testCommitAction(module.actions.getMappings, actionPayload, state, expectedMutations, done)
	})
	
	it("getQueues", done =>{

		mock.onGet(queue_url ).reply(500)
		
		const actionPayload = null

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'getQueues'
			}
		]
		testCommitAction(module.actions.getQueues, actionPayload, state, expectedMutations, done)
	})
})

describe("Module: Config, Reply: timeout, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getMappings", done =>{

		mock.onGet(mapping_url).timeout()
		
		const actionPayload = null

		const expectedMutations = [
			{
				type: 'misc/updateFail',
				payload: 'getMappings'
			}
		]	
		testCommitAction(module.actions.getMappings, actionPayload, state, expectedMutations, done)
	})
	
	it("getQueues", done =>{

		mock.onPost(queue_url).timeout
		
		const actionPayload = null

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'getQueues'
			}
		]
		testCommitAction(module.actions.getQueues, actionPayload, state, expectedMutations, done)
	})
})

