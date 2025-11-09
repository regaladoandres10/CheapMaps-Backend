LOCAL_IPS = [
    '192.168.1.121'
]


BASE_URLS = [

    "http://localhost:3000",
] + [f"http://{ip}" for ip in LOCAL_IPS]