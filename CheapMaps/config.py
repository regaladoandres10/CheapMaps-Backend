LOCAL_IPS = [
    '192.168.1.68', 
    '172.20.10.2', 
    '192.168.20.223'
]


BASE_URLS = [

    "http://localhost:3000",
] + [f"http://{ip}" for ip in LOCAL_IPS]