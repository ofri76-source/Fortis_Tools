from typing import Optional, Callable
_append=None
def register_append_sink(cb: Callable[[str],None]):
 global _append; _append=cb

def publish_append(text:str):
 global _append
 if _append:
  try: _append(text)
  except Exception: pass
