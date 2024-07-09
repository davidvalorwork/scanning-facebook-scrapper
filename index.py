from bottle import run, post, request, response, hook
from facebook_scraper import get_profile
from threading import Lock
profile_lock = Lock()
is_fetching_profile = False


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
    
    # Check if a profile is currently being fetched
    if is_fetching_profile:
        # Wait until the profile is not being fetched anymore
        while is_fetching_profile:
            pass

    # Acquire the lock to ensure only one thread can fetch a profile at a time
    with profile_lock:
        is_fetching_profile = True
        res = get_profile(facebook_link, cookies="cookies.txt", friends=True)
        # After fetching, set the flag to False
        is_fetching_profile = False
        return res


run(host="0.0.0.0", port=8080, debug=True, reloader=True)
