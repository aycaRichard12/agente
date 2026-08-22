"""CheckboxTreeview component for selecting folder files."""
import tkinter as tk
from tkinter import ttk
from typing import Set, List


class CheckboxTreeview(ttk.Treeview):
    def __init__(self, master, **kwargs):
        super().__init__(master, columns=("check", "name"), show="tree headings", **kwargs)
        self.heading("#0", text="", anchor="w")
        self.heading("check", text="☑", anchor="center", command=self.toggle_all_header)
        self.heading("name", text="Archivo / Carpeta", anchor="w")
        self.column("#0", width=35, stretch=False)
        self.column("check", width=40, stretch=False, anchor="center")
        self.column("name", width=260, stretch=True)
        
        self.tag_configure("checked", foreground="#1b5e20")
        self.tag_configure("unchecked", foreground="#757575")
        self.bind("<Button-1>", self.on_click)
        self.checked_items: Set[str] = set()

    def insert_file(self, parent, rel_path: str, is_checked: bool = True):
        item = self.insert(parent, "end", text="📄", values=("☑" if is_checked else "☐", rel_path), tags=("checked" if is_checked else "unchecked",))
        if is_checked:
            self.checked_items.add(rel_path)
        return item

    def insert_folder(self, parent, rel_path: str):
        return self.insert(parent, "end", text="📁", values=("", rel_path), open=True)

    def check_item(self, item):
        rel_path = self.set(item, "name")
        if rel_path:
            self.set(item, "check", "☑")
            self.item(item, tags=("checked",))
            if not self.get_children(item):
                self.checked_items.add(rel_path)
        for child in self.get_children(item):
            self.check_item(child)

    def uncheck_item(self, item):
        rel_path = self.set(item, "name")
        if rel_path:
            self.set(item, "check", "☐")
            self.item(item, tags=("unchecked",))
            if rel_path in self.checked_items:
                self.checked_items.remove(rel_path)
        for child in self.get_children(item):
            self.uncheck_item(child)

    def toggle_item(self, item):
        check_val = self.set(item, "check")
        if check_val == "☑":
            self.uncheck_item(item)
        else:
            self.check_item(item)

    def toggle_all_header(self):
        all_children = self.get_children()
        if not all_children:
            return
        all_checked = all(self.set(child, "check") == "☑" for child in all_children if self.set(child, "check") != "")
        for child in all_children:
            if all_checked:
                self.uncheck_item(child)
            else:
                self.check_item(child)

    def on_click(self, event):
        region = self.identify_region(event.x, event.y)
        item = self.identify_row(event.y)
        if not item:
            return
        column = self.identify_column(event.x)
        if region == "cell" and column == "#2":
            self.toggle_item(item)
        elif region == "tree":
            self.toggle_item(item)

    def select_all(self):
        for item in self.get_children():
            self.check_item(item)

    def deselect_all(self):
        for item in self.get_children():
            self.uncheck_item(item)

    def get_checked_files(self) -> List[str]:
        return list(self.checked_items)
