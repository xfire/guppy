callbacks = []

def startupNotification(callback):
    callbacks.append(callback)
    return callback

def notify():
    for callback in callbacks:
        callback()
    
