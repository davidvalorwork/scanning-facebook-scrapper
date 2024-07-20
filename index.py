from bottle import run, post, request, response, hook
from facebook_scraper import get_profile


@hook("after_request")
def enable_cors():
    response.headers["Access-Control-Allow-Origin"] = "*"  # Permite todas las fuentes
    response.headers["Access-Control-Allow-Methods"] = "PUT, GET, POST, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = (
        "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"
    )

@post("/")
def receive_link():
    global is_fetching_profile
    facebook_link = request.body.read().decode("utf-8")
    print(facebook_link)
    res = get_profile(facebook_link, cookies="cookies.txt", friends=True)
    return res
    
run(host="0.0.0.0", port=4000)
