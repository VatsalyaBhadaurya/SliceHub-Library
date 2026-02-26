from slicehub import SliceHub
from slicehub.services.ride import RideSlice


def create_app():
    hub = SliceHub(title="SliceHub Example")
    # enable features
    hub.enable_auth(secret_key="supersecret")
    hub.enable_database(url="postgresql://user:pass@localhost/dbname")

    # register slices
    ride = RideSlice()
    hub.register_slice(ride)

    return hub.get_app()


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
