import tkinter as tk
from tkinter import ttk, filedialog
from core.utils import publish_append, register_append_sink
class Tab(ttk.Frame):
 TAB_NAME="Virtual-IP"
 def __init__(self,m):
  super().__init__(m)
  pw=ttk.Panedwindow(self,orient=tk.HORIZONTAL); L=ttk.Frame(pw); R=ttk.Frame(pw); pw.add(L,weight=3); pw.add(R,weight=5); pw.pack(fill=tk.BOTH,expand=True)
  ttk.Label(L,text="Virtual-IP — modular",font=("TkDefaultFont",10,"bold")).pack(anchor='w',padx=12,pady=12)
  R.grid_rowconfigure(0,weight=1); R.grid_columnconfigure(0,weight=1)
  grp=ttk.LabelFrame(R,text="Virtual-IP CLI"); grp.grid(row=0,column=0,sticky='nsew',padx=8,pady=8)
  self.txt=tk.Text(grp,wrap='none'); self.txt.pack(fill=tk.BOTH,expand=True,padx=6,pady=6)
  bar=ttk.Frame(R); bar.grid(row=1,column=0,sticky='ew',padx=8,pady=(0,8))
  ttk.Button(bar,text='Copy',command=self._copy).pack(side=tk.LEFT,padx=4)
  ttk.Button(bar,text='Save As',command=self._save).pack(side=tk.LEFT,padx=4)
  ttk.Button(bar,text='Append',command=self._append).pack(side=tk.LEFT,padx=4)
 def _copy(self):
  try: self.clipboard_clear(); self.clipboard_append(self.txt.get('1.0',tk.END).rstrip('\n'))
  except Exception: pass
 def _save(self):
  p=filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[('Text','*.txt'),('All','*.*')])
  if p: open(p,'w',encoding='utf-8').write(self.txt.get('1.0',tk.END))
 def _append(self): publish_append(self.txt.get('1.0',tk.END))
