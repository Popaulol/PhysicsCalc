import glob
import os
import tkinter as tk
from tkinter import ttk
import importlib.util
import sys


def load_modules(directory="src"):
    modules = []
    files = glob.glob(os.path.join(directory, "*.py"))
    for file_path in files:
        module_name = file_path[len(directory) + 1 : -3]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        modules.append(module)
    return modules


def main():
    root = tk.Tk()
    root.title("Physics Calculator")

    tab_control = ttk.Notebook(root)
    tabs = list(map(lambda module: module.construct(tab_control), load_modules()))

    for name, frame in tabs:
        tab_control.add(frame, text=name)

    tab_control.pack(expand=1, fill="both")
    root.mainloop()


if __name__ == "__main__":
    load_modules()
    main()
