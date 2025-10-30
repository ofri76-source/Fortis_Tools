try:
 import tkinter as tk
 from tkinter import ttk
except Exception:
 tk=None; ttk=None
class ThemeManager:
 def apply_default(self):
  if tk is None: return
  r=tk._default_root
  if not r: return
  s=ttk.Style(r)
  try: s.theme_use('clam')
  except Exception: pass
  s.configure('TNotebook',padding=0); s.configure('TNotebook.Tab',padding=(16,8))
