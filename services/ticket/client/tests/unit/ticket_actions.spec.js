/*eslint-disable */
import sinon , {expect} from "sinon"
import sinonChai from "sinon-chai"
import chai from "chai"

import {testCommitAction, testDispatchAction, mock} from "../testUtils"
import module from '@/store/modules/ticket'

chai.use(sinonChai)

var state = {}
const base_url = module.base_url
const supporter_url = 'http://localhost:5070/gateway/supporter/ticket/'

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
		
		const actionPayload = null
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		const response = {
			id:'1'
		}

		mock.onPost(base_url ).reply(200, response)

		const url = new RegExp(base_url + '1/message/*');
		mock.onPost(url).reply(200)	

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

	
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		
		mock.onPut(base_url + '1').reply(200)
		const url = new RegExp(base_url + '1/message/*');
		mock.onPost(url).reply(200)	

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
	
	it("getSupporterTickets", done =>{

		state.config.mappings= [{'id': '123', 'name': 'test_module_1', 'children': ['1','2']}]

		const response = {
			tickets : [ 
				{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
				{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]},
			]
		}
	
		
		mock.onPost(supporter_url).reply(200, response)

		const expectedMutations =
		[
			{
				type: 'update',
				payload: response.tickets
			}
		]
		testCommitAction(module.actions.getSupporterTickets ,null, state, expectedMutations, done)
	})

	it("downloadFiles", done =>{

		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1'}
		const response = null 
		mock.onGet( base_url +'1/message/2a3/file/test.json').reply(200, response)

		const actionPayload = ['test.json', '2 a 3']

		const expectedMutations =
		[
			{
				type: 'downloadedFile',
				payload: null
			}
		]
		testCommitAction(module.actions.downloadFile , actionPayload, state, expectedMutations, done)
	})
})

describe("Module: Mapping, Reply: fail, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getTickets", done =>{
		
		const response = {
			ticket : [ 
				{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
				{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]},
			]
		}

		mock.onGet(base_url).reply(500)
		
		const actionPayload = null

		const expectedMutations =[
			{
				type: 'misc/updateFail',
				payload: 'getTickets'
			}
		]	
		testCommitAction(module.actions.getTickets, actionPayload, state, expectedMutations, done)
	})
	
	it("postSelected", done =>{
		
		const actionPayload = null
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		const response = {
			id:'1'
		}

		mock.onPost(base_url ).reply(500)

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'postSelected'
			}
		]
		testCommitAction(module.actions.postSelected, actionPayload, state, expectedMutations, done)
	})

	it("putSelected", done =>{

	
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		
		mock.onPut(base_url + '1').reply(500)

		const actionPayload = 1

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'putSelected'
			}
		]
		testCommitAction(module.actions.putSelected , actionPayload, state, expectedMutations, done)
	})

	
	it("postSelected/uploadFiles", done =>{
		
		const actionPayload = null
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		const response = {
			id:'1'
		}

		mock.onPost(base_url ).reply(200, response)
		const url = new RegExp(base_url + '1/message/*');
		mock.onPost(url).reply(500)	
		
		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'postSelected/uploadFiles'
			}
		]
		testCommitAction(module.actions.postSelected, actionPayload, state, expectedMutations, done)
	})

	it("putSelected/uploadFiles", done =>{

	
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		
		mock.onPut(base_url + '1').reply(200)

		const url = new RegExp(base_url + '1/message/*');
		mock.onPost(url).reply(500)	
		
		const actionPayload = 1

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'putSelected/uploadFiles'
			}
		]
		testCommitAction(module.actions.putSelected , actionPayload, state, expectedMutations, done)
	})



	
	it("getSupporterTickets", done =>{

		state.config.mappings= [{'id': '123', 'name': 'test_module_1', 'children': ['1','2']}]
		
		mock.onPost(supporter_url).reply(500)

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'getSupporterTickets'
			}
		]

		testCommitAction(module.actions.getSupporterTickets ,null, state, expectedMutations, done)
	})

	it("downloadFiles", done =>{

		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1'}
		const response = null 
		mock.onGet( base_url +'1/message/2a3/file/test.json').reply(500)

		const actionPayload = ['test.json', '2 a 3']

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'downloadFile'
			}
		]

		testCommitAction(module.actions.downloadFile , actionPayload, state, expectedMutations, done)
	})




})

describe("Module: Queue, Reply: timeout, Action :", ()=>{
	beforeEach(function(){
		mock.reset()
	})

	it("getTickets", done =>{
		
		const response = {
			ticket : [ 
				{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
				{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]},
			]
		}

		mock.onGet(base_url).timeout()
		
		const actionPayload = null

		const expectedMutations =[
			{
				type: 'misc/updateFail',
				payload: 'getTickets'
			}
		]	
		testCommitAction(module.actions.getTickets, actionPayload, state, expectedMutations, done)
	})
	
	it("postSelected", done =>{
		
		const actionPayload = null
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		const response = {
			id:'1'
		}

		mock.onPost(base_url ).timeout()

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'postSelected'
			}
		]
		testCommitAction(module.actions.postSelected, actionPayload, state, expectedMutations, done)
	})

	it("putSelected", done =>{

	
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		
		mock.onPut(base_url + '1').timeout()

		const actionPayload = 1

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'putSelected'
			}
		]
		testCommitAction(module.actions.putSelected , actionPayload, state, expectedMutations, done)
	})

	
	it("postSelected/uploadFiles", done =>{
		
		const actionPayload = null
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		const response = {
			id:'1'
		}

		mock.onPost(base_url ).reply(200, response)
		const url = new RegExp(base_url + '1/message/*');
		mock.onPost(url).timeout()
		
		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'postSelected/uploadFiles'
			}
		]
		testCommitAction(module.actions.postSelected, actionPayload, state, expectedMutations, done)
	})

	it("putSelected/uploadFiles", done =>{

	
		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
		state.ticket.files = [{ 'file':new File(['asdf'], 'test')}]
		
		mock.onPut(base_url + '1').reply(200)

		const url = new RegExp(base_url + '1/message/*');
		mock.onPost(url).timeout()
		
		const actionPayload = 1

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'putSelected/uploadFiles'
			}
		]
		testCommitAction(module.actions.putSelected , actionPayload, state, expectedMutations, done)
	})



	
	it("getSupporterTickets", done =>{

		state.config.mappings= [{'id': '123', 'name': 'test_module_1', 'children': ['1','2']}]
		
		mock.onPost(supporter_url).timeout()

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'getSupporterTickets'
			}
		]

		testCommitAction(module.actions.getSupporterTickets ,null, state, expectedMutations, done)
	})

	it("downloadFiles", done =>{

		state.ticket = {}
		state.ticket.selectedTicket = {'id': '1'}
		const response = null 
		mock.onGet( base_url +'1/message/2a3/file/test.json').timeout()

		const actionPayload = ['test.json', '2 a 3']

		const expectedMutations =
		[
			{
				type: 'misc/updateFail',
				payload: 'downloadFile'
			}
		]

		testCommitAction(module.actions.downloadFile , actionPayload, state, expectedMutations, done)
	})




})

