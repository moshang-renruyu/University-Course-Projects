import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

DISK_SIZE = 1024 * 1024  # 1MB

class FileEntry:
    def __init__(self, name, is_dir, address=0, length=0):
        self.name = name
        self.is_dir = is_dir
        self.address = address
        self.length = length
        self.children = []  # 仅目录用

class User:
    def __init__(self, username):
        self.username = username
        self.root_dir = FileEntry(username, True)

class FileSystem:
    def __init__(self):
        self.users = []
        self.virtual_disk = bytearray(DISK_SIZE)
        self.current_user = None
        self.current_dir = None
        self.path_stack = []

    def create_user(self, username):
        user = User(username)
        self.users.append(user)

    def login(self, username):
        for user in self.users:
            if user.username == username:
                self.current_user = user
                self.current_dir = user.root_dir
                self.path_stack = [user.root_dir]
                return True
        return False

    def ls(self):
        return self.current_dir.children

    def cd(self, dirname):
        if dirname == "..":
            if len(self.path_stack) > 1:
                self.path_stack.pop()
                self.current_dir = self.path_stack[-1]
        else:
            for entry in self.current_dir.children:
                if entry.is_dir and entry.name == dirname:
                    self.current_dir = entry
                    self.path_stack.append(entry)
                    return True
            return False
        return True

    def mkdir(self, dirname):
        for entry in self.current_dir.children:
            if entry.name == dirname and entry.is_dir:
                return False
        new_dir = FileEntry(dirname, True)
        self.current_dir.children.append(new_dir)
        return True

    def create(self, filename, size):
        for entry in self.current_dir.children:
            if entry.name == filename and not entry.is_dir:
                return False, "文件已存在。"
        address = self._find_free_space(size)
        if address == -1:
            return False, "磁盘空间不足。"
        new_file = FileEntry(filename, False, address, size)
        self.current_dir.children.append(new_file)
        return True, "文件创建成功。"

    def delete(self, filename):
        for entry in self.current_dir.children:
            if entry.name == filename:
                self.current_dir.children.remove(entry)
                return True
        return False

    def write(self, filename, content):
        for entry in self.current_dir.children:
            if entry.name == filename and not entry.is_dir:
                if len(content.encode()) > entry.length:
                    return False, "内容超出文件大小。"
                self.virtual_disk[entry.address:entry.address+len(content.encode())] = content.encode()
                return True, "写入成功。"
        return False, "未找到该文件。"

    def read(self, filename):
        for entry in self.current_dir.children:
            if entry.name == filename and not entry.is_dir:
                data = self.virtual_disk[entry.address:entry.address+entry.length]
                return True, data.decode(errors='ignore')
        return False, "未找到该文件。"

    def _find_free_space(self, size):
        used = []
        for user in self.users:
            stack = [user.root_dir]
            while stack:
                dir = stack.pop()
                for entry in dir.children:
                    if entry.is_dir:
                        stack.append(entry)
                    else:
                        used.append((entry.address, entry.length))
        used.sort()
        address = 0
        for addr, length in used:
            if address + size <= addr:
                return address
            address = addr + length
        if address + size <= DISK_SIZE:
            return address
        return -1

class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("文件系统设计")
        # 设置窗口大小和居中
        w, h = 800, 500
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        root.geometry(f"{w}x{h}+{x}+{y}")
        root.configure(bg="#f0f4f8")
        self.fs = FileSystem()
        for username in ['user1', 'user2', 'user3']:
            self.fs.create_user(username)
        self.fs.login('user1')

        # 主体frame
        main_frame = tk.Frame(root, bg="#f0f4f8")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 左侧目录树带滚动条
        tree_frame = tk.Frame(main_frame, bg="#f0f4f8")
        tree_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        tree_scroll = tk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
        self.tree.pack(side=tk.LEFT, fill=tk.Y)
        tree_scroll.config(command=self.tree.yview)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        style = ttk.Style()
        style.configure("Treeview", font=("微软雅黑", 11), rowheight=24)
        style.configure("Treeview.Heading", font=("微软雅黑", 12, "bold"))

        # 右侧文件内容带滚动条
        text_frame = tk.Frame(main_frame, bg="#f0f4f8")
        text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_scroll = tk.Scrollbar(text_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text = tk.Text(text_frame, width=40, font=("Consolas", 12), bd=2, relief=tk.GROOVE, yscrollcommand=text_scroll.set, bg="#fafdff")
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_scroll.config(command=self.text.yview)

        # 操作按钮美化
        btn_frame = tk.Frame(root, bg="#e0e6ed")
        btn_frame.pack(side=tk.TOP, fill=tk.X, pady=(0, 5))
        btn_style = {"font": ("微软雅黑", 11), "bg": "#4f8cff", "fg": "white", "activebackground": "#357ae8", "activeforeground": "#fff", "bd": 0, "padx": 12, "pady": 6}
        tk.Button(btn_frame, text="新建文件", command=self.create_file, **btn_style).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="新建目录", command=self.create_dir, **btn_style).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="删除", command=self.delete_entry, **btn_style).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="写入", command=self.write_file, **btn_style).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="读取", command=self.read_file, **btn_style).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="查询用户", command=self.switch_user, **btn_style).pack(side=tk.LEFT, padx=6)

        self.refresh_tree()

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for user in self.fs.users:
            user_id = self.tree.insert("", "end", text=user.username, open=True)
            self._add_dir(user.root_dir, user_id)

    def _add_dir(self, dir_entry, parent_id):
        for entry in dir_entry.children:
            eid = self.tree.insert(parent_id, "end", text=entry.name, open=True)
            if entry.is_dir:
                self._add_dir(entry, eid)

    def on_tree_select(self, event):
        item = self.tree.selection()
        if not item:
            return
        item = item[0]
        path = self._get_path(item)
        entry = self._find_entry_by_path(path)
        if entry and not entry.is_dir:
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, self.fs.virtual_disk[entry.address:entry.address+entry.length].decode(errors='ignore'))
        else:
            self.text.delete(1.0, tk.END)

    def _get_path(self, item):
        path = []
        while item:
            path.insert(0, self.tree.item(item, "text"))
            item = self.tree.parent(item)
        return path

    def _find_entry_by_path(self, path):
        if not path:
            return None
        for user in self.fs.users:
            if user.username == path[0]:
                entry = user.root_dir
                for name in path[1:]:
                    for child in entry.children:
                        if child.name == name:
                            entry = child
                            break
                    else:
                        return None
                return entry
        return None

    def create_file(self):
        item = self.tree.selection()
        if not item:
            messagebox.showinfo("提示", "请选择目录")
            return
        path = self._get_path(item[0])
        entry = self._find_entry_by_path(path)
        if not entry or not entry.is_dir:
            messagebox.showinfo("提示", "请选择目录")
            return
        # 文件名输入框
        filename = simpledialog.askstring("新建文件", "文件名（不含后缀）：")
        if not filename:
            return
        # 文件格式下拉框
        formats = ['.txt', '.md', '.py', '.c', '.cpp', '.log']
        format_win = tk.Toplevel(self.root)
        format_win.title("选择文件格式")
        format_win.configure(bg="#fafdff")
        tk.Label(format_win, text="文件格式：", font=("微软雅黑", 11), bg="#fafdff").pack(side=tk.LEFT, padx=4, pady=8)
        format_var = tk.StringVar(value=formats[0])
        format_box = ttk.Combobox(format_win, textvariable=format_var, values=formats, state="readonly", font=("微软雅黑", 11), width=8)
        format_box.pack(side=tk.LEFT, padx=4)
        size_var = tk.StringVar()
        tk.Label(format_win, text="文件大小（字节）：", font=("微软雅黑", 11), bg="#fafdff").pack(side=tk.LEFT, padx=4)
        size_entry = tk.Entry(format_win, textvariable=size_var, width=10, font=("微软雅黑", 11))
        size_entry.pack(side=tk.LEFT, padx=4)
        result = {}
        def on_ok():
            result['format'] = format_var.get()
            result['size'] = size_var.get()
            format_win.destroy()
        tk.Button(format_win, text="确定", command=on_ok, font=("微软雅黑", 11), bg="#4f8cff", fg="white", bd=0, padx=10, pady=4).pack(side=tk.LEFT, padx=8)
        format_win.grab_set()
        self.root.wait_window(format_win)
        file_format = result.get('format')
        size_str = result.get('size')
        if not file_format or not size_str:
            return
        try:
            size = int(size_str)
        except Exception:
            messagebox.showinfo("提示", "文件大小需为整数")
            return
        full_filename = filename + file_format
        self.fs.current_dir = entry
        ok, msg = self.fs.create(full_filename, size)
        if not ok:
            messagebox.showinfo("提示", msg)
        self.refresh_tree()

    def create_dir(self):
        item = self.tree.selection()
        if not item:
            messagebox.showinfo("提示", "请选择目录")
            return
        path = self._get_path(item[0])
        entry = self._find_entry_by_path(path)
        if not entry or not entry.is_dir:
            messagebox.showinfo("提示", "请选择目录")
            return
        dirname = simpledialog.askstring("新建目录", "目录名：")
        if dirname:
            self.fs.current_dir = entry
            if not self.fs.mkdir(dirname):
                messagebox.showinfo("提示", "目录已存在。")
            self.refresh_tree()

    def delete_entry(self):
        item = self.tree.selection()
        if not item:
            messagebox.showinfo("提示", "请选择要删除的文件或目录")
            return
        path = self._get_path(item[0])
        if len(path) < 2:
            messagebox.showinfo("提示", "不能删除用户根目录")
            return
        parent_path = path[:-1]
        parent_entry = self._find_entry_by_path(parent_path)
        self.fs.current_dir = parent_entry
        if not self.fs.delete(path[-1]):
            messagebox.showinfo("提示", "删除失败")
        self.refresh_tree()

    def write_file(self):
        item = self.tree.selection()
        if not item:
            messagebox.showinfo("提示", "请选择文件")
            return
        path = self._get_path(item[0])
        entry = self._find_entry_by_path(path)
        if not entry or entry.is_dir:
            messagebox.showinfo("提示", "请选择文件")
            return
        # 弹出输入框输入内容
        content = simpledialog.askstring("写入文件", "请输入要写入的内容：")
        if content is None or content.strip() == '':
            messagebox.showinfo("提示", "请输入内容")
            return
        self.fs.current_dir = self._find_entry_by_path(path[:-1])
        ok, msg = self.fs.write(entry.name, content)
        messagebox.showinfo("提示", msg)

    def read_file(self):
        item = self.tree.selection()
        if not item:
            messagebox.showinfo("提示", "请选择文件")
            return
        path = self._get_path(item[0])
        entry = self._find_entry_by_path(path)
        if not entry or entry.is_dir:
            messagebox.showinfo("提示", "请选择文件")
            return
        self.text.delete(1.0, tk.END)
        self.fs.current_dir = self._find_entry_by_path(path[:-1])
        ok, content = self.fs.read(entry.name)
        if ok:
            self.text.insert(tk.END, content)
        else:
            messagebox.showinfo("提示", content)

    def switch_user(self):
        username = simpledialog.askstring("查询用户", "用户名：")
        if username:
            if not self.fs.login(username):
                messagebox.showinfo("提示", "用户不存在。")
            self.refresh_tree()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemGUI(root)
    root.mainloop() 