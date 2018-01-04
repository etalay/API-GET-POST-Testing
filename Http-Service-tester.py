import http.client
import time

start_time = time.time()

for x in range(0, 60):

	#GET Example
 
    conn = http.client.HTTPConnection(" type url address or ip address ")

    headers = {
        'cache-control': "no-cache",
        'token': "8a92eac4-8114-58a7-97db-d1fbdf803af5"
        }
    
    conn.request("GET", "/example_url", headers=headers)
    
    res = conn.getresponse()
    data = res.read()
        
print("--- %s seconds ---" % (time.time() - start_time))
    
    #POST Example
    
'''
    conn = http.client.HTTPConnection("type url address or ip address")
    
    payload = " type your post parameter "
    
	headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'token': "0ccca05e-6bf1-a5cd-6b1a-e130244d1fc1"
        }
    
    conn.request("POST", "/example_url", payload, headers)
    
    res = conn.getresponse()
    data = res.read()
    
    print(data.decode("utf-8"))
'''





