import json
# /pubs/
#get

url = '/pubsub/'
key = 'publisher'
def test_pubs_get_specific_pub(app, client, insert_pub):
    res = client.get(url+insert_pub[0][key])
    pubs = json.loads(res.data)['publishers']
    print(pubs)
    assert res.status_code == 200
    assert pubs
    assert pubs[key] == insert_pub[0][key]

def test_pubs_get_with_many_pubs(app, client, insert_multiple_pubs):
    res = client.get(url + insert_multiple_pubs[0][1][key])
    pubs = json.loads(res.data)['publishers']
    assert res.status_code == 200
    assert pubs 

def test_pubs_get_no_pubs(app, client, insert_nothing):
    res = client.get(url+'test')
    pubs = json.loads(res.data)['publishers']
    assert res.status_code == 200
    

##POST Message

def test_message_post(app,client, insert_pub):
    res = client.post(url+insert_pub[0][key] , data='{"message":{"id": "1"}}')
    d = insert_pub[1]
    count = d.pub.count_documents({})
    assert res.status_code == 200
    assert count == 1

def test_message_post_wrong(app,client, insert_pub):
    res = client.post(url+insert_pub[0][key],  data='{"caption":"test"}')
    d = insert_pub[1]
    count = d.pub.count_documents({})
    assert res.status_code == 400

def test_message_post_empty(app, client, insert_pub):
    res = client.post(url+insert_pub[0][key],  data='')
    d = insert_pub[1]
    count = d.pub.count_documents({})
    assert res.status_code == 400

#PUT 


def test_sub_put(app,client, insert_pub):
    subs = '{"subscriber":"test", "callback": "http://localhost"}'
    res = client.put(url+insert_pub[0][key] , data=subs)
    d = insert_pub[1]
    pub = d.pub.find()

    assert res.status_code == 200
    for p in pub:
        for sub in p['subscribers']:
            assert sub['subscriber'] == 'test'
            assert sub['callback'] == 'http://localhost'
    

def test_mub_put_wrong(app,client,insert_pub):
    res = client.post(url+insert_pub[0][key] , data='{"caption":"test"}')
    assert res.status_code == 400

def test_sub_put_empty(app, client, insert_pub):
    res = client.put(url+insert_pub[0][key] , data='')
    assert res.status_code == 400


