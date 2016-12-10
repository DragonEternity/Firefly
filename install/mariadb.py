from subprocess import call
import signal, time

keyserver = keyserver.ubuntu.com 0xcbcb082a1bb943db

def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException, "Key request timed out."
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

def main():
    try:
        with Timeout(3):
            call(["apt-key", "adv", "--recv-keys", "--keyserver", keyserver])
    except Timeout.Timeout:
        print "Keyserver timed out."
