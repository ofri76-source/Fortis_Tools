import importlib, pkgutil, tkinter as tk
from tkinter import ttk
from core.logger import get_logger
log=get_logger(__name__)
class MainWindow(ttk.Frame):
 def __init__(self, m): super().__init__(m); self.pack(fill=tk.BOTH,expand=True); self.nb=ttk.Notebook(self); self.nb.pack(fill=tk.BOTH,expand=True); self._load()
 def _load(self):
  from ui import tabs as p
  for mi in pkgutil.iter_modules(p.__path__, p.__name__+'.'):
   md=importlib.import_module(mi.name)
   if hasattr(md,'Tab'):
    cls=getattr(md,'Tab')
    try: self.nb.add(cls(self.nb), text=getattr(cls,'TAB_NAME',cls.__name__)); log.info('Loaded %s', getattr(cls,'TAB_NAME',cls.__name__))
    except Exception as e: log.exception('Failed tab %s: %s', mi.name, e)
def run_app():
 r=tk.Tk(); r.title('Fortis Toolbox'); r.geometry('1200x750'); MainWindow(r); r.mainloop()
