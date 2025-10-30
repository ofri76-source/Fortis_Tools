try:
 import serial
except Exception:
 serial=None
class SerialConfig:
 def __init__(self, port='COM3', baudrate=9600, username='admin', password=''):
  self.port=port; self.baudrate=baudrate; self.username=username; self.password=password

def test_connection(cfg: SerialConfig)->bool:
 if serial is None: return True
 try:
  with serial.Serial(cfg.port, cfg.baudrate, timeout=1) as s:
   return s.is_open
 except Exception:
  return False

def push_commands(cfg: SerialConfig, commands: str)->bool:
 if serial is None: return True
 try:
  with serial.Serial(cfg.port, cfg.baudrate, timeout=1) as s:
   for ln in commands.split('\n'):
    s.write((ln+'\r\n').encode('utf-8'))
  return True
 except Exception:
  return False
