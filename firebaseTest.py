from firebase import firebase

def readFirebase():
    firebase1 = firebase.FirebaseApplication('https://augmentedreality-af310-default-rtdb.firebaseio.com/', None)

    gas_value = firebase1.get('/AE393/gas_value', None)
    fire_status = firebase1.get('/AE393/fire_status', None)
    tilt_status = firebase1.get('/AE393/tilt_status', None)
    sos_status = firebase1.get('/AE393/sos_status', None)
    temperature = firebase1.get('/AE393/temperature', None)
    humidity = firebase1.get('/AE393/humidity', None)
    heartbeat_bpm = firebase1.get('/AE393/heartbeat_bpm', None)
    buzzer_state = firebase1.get('/AE393/buzzer_state', None)

    return (gas_value, fire_status, tilt_status, sos_status, temperature, humidity, heartbeat_bpm, buzzer_state)
