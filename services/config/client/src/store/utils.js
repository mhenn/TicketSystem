
const mapping_url = 'http://localhost:5555/config/role-mapping/'
const queue_url = 'http://localhost:5555/config/queues/'

function get_auth_header(token){
	return {'Authorization': 'Bearer ' + token}
}
