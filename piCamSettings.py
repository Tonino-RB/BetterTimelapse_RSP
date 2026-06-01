width = 2592
height = 1944

def configuration(camera) :
    config = camera.create_still_configuration(main={"size": (width, height)})
    return config