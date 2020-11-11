import sinon , {expect} from "sinon"
import sinonChai from "sinon-chai"
import chai from "chai"

import {testCommitAction, testDispatchAction, mock} from "../testUtils"
import mapping from '@/store/modules/mapping'

chai.use(sinonChai)

const state = {misc :{cloak: {'token': 'id'}}}
let base_url = "http://localhost:5555/config/role-mapping/"

describe("Module: Mapping, Reply: 200, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getMappings", done =>{
		
		const response = {
			mapping : [ 
				{'id': '123', 'name': 'test_mapping_1', 'children': ['1','2']},
				{'id': '456', 'name': 'test_mapping_2', 'children': ['3']},
				{'id': '789', 'name': 'test_mapping_3', 'children': []}
			]
		}
		mock.onGet(base_url).reply(200, response)
		
		const actionPayload = null

		const expectedMutations =[
			{
				type: 'updateMapping',
				payload: response.mapping
			}
		]	
		testCommitAction(mapping.actions.getMappings, actionPayload, state, expectedMutations, done)
	})
	
	it("postMapping", done =>{
		console.log(base_url)
		mock.onPost(base_url ).reply(200)
		
		const actionPayload = null

		const expectedActions =
		[
			{
				type: 'getMappings',
				payload: null
			}
		]
		testDispatchAction(mapping.actions.postMapping, actionPayload, state, expectedActions, done)
	})

	it("deleteMapping", done =>{

		mock.onDelete(base_url + '1').reply(200)
		
		const actionPayload = 1

		const expectedActions =
		[
			{
				type: 'getMappings',
				payload: null
			}
		]
		testDispatchAction(mapping.actions.deleteMapping, actionPayload, state, expectedActions, done)
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
		testCommitAction(mapping.actions.getMappings, actionPayload, state, expectedMutations, done)
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
		testCommitAction(mapping.actions.postMapping, actionPayload, state, expectedMutations, done)
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
		testCommitAction(mapping.actions.deleteMapping, actionPayload, state, expectedMutations, done)
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
		testCommitAction(mapping.actions.getMappings, actionPayload, state, expectedMutations, done)
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
		testCommitAction(mapping.actions.postMapping, actionPayload, state, expectedMutations, done)
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
		testCommitAction(mapping.actions.deleteMapping, actionPayload, state, expectedMutations, done)
	})

})

