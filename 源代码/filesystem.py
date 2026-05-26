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
        print(f"用户 {username} 创建成功。")

    def login(self, username):
        for user in self.users:
            if user.username == username:
                self.current_user = user
                self.current_dir = user.root_dir
                self.path_stack = [user.root_dir]
                print(f"已登录用户 {username}")
                return
        print("用户不存在。")

    def ls(self):
        for entry in self.current_dir.children:
            print(f"{'[DIR]' if entry.is_dir else '[FILE]'} {entry.name}")

    def pwd(self):
        print('/' + '/'.join([entry.name for entry in self.path_stack]))

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
                    return
            print("目录不存在。")

    def mkdir(self, dirname):
        for entry in self.current_dir.children:
            if entry.name == dirname and entry.is_dir:
                print("目录已存在。")
                return
        new_dir = FileEntry(dirname, True)
        self.current_dir.children.append(new_dir)
        print(f"目录 {dirname} 创建成功。")

    def create(self, filename, size):
        for entry in self.current_dir.children:
            if entry.name == filename and not entry.is_dir:
                print("文件已存在。")
                return
        # 简单顺序分配
        address = self._find_free_space(size)
        if address == -1:
            print("磁盘空间不足。")
            return
        new_file = FileEntry(filename, False, address, size)
        self.current_dir.children.append(new_file)
        print(f"文件 {filename} 创建成功。")

    def delete(self, filename):
        for entry in self.current_dir.children:
            if entry.name == filename:
                self.current_dir.children.remove(entry)
                print(f"{'目录' if entry.is_dir else '文件'} {filename} 删除成功。")
                return
        print("未找到该文件/目录。")

    def write(self, filename, content):
        for entry in self.current_dir.children:
            if entry.name == filename and not entry.is_dir:
                if len(content) > entry.length:
                    print("内容超出文件大小。")
                    return
                self.virtual_disk[entry.address:entry.address+len(content)] = content.encode()
                print("写入成功。")
                return
        print("未找到该文件。")

    def read(self, filename):
        for entry in self.current_dir.children:
            if entry.name == filename and not entry.is_dir:
                data = self.virtual_disk[entry.address:entry.address+entry.length]
                print(data.decode(errors='ignore'))
                return
        print("未找到该文件。")

    def _find_free_space(self, size):
        # 简单实现：顺序分配，不考虑碎片
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

def main():
    fs = FileSystem()
    # 预设3个用户
    for username in ['user1', 'user2', 'user3']:
        fs.create_user(username)
    fs.login('user1')

    while True:
        cmd = input(">> ").strip().split()
        if not cmd:
            continue
        if cmd[0] == "ls":
            fs.ls()
        elif cmd[0] == "pwd":
            fs.pwd()
        elif cmd[0] == "cd":
            if len(cmd) > 1:
                fs.cd(cmd[1])
            else:
                print("用法: cd 目录名")
        elif cmd[0] == "mkdir":
            if len(cmd) > 1:
                fs.mkdir(cmd[1])
            else:
                print("用法: mkdir 目录名")
        elif cmd[0] == "create":
            if len(cmd) > 2:
                fs.create(cmd[1], int(cmd[2]))
            else:
                print("用法: create 文件名 大小")
        elif cmd[0] == "delete":
            if len(cmd) > 1:
                fs.delete(cmd[1])
            else:
                print("用法: delete 文件名/目录名")
        elif cmd[0] == "write":
            if len(cmd) > 2:
                fs.write(cmd[1], ' '.join(cmd[2:]))
            else:
                print("用法: write 文件名 内容")
        elif cmd[0] == "read":
            if len(cmd) > 1:
                fs.read(cmd[1])
            else:
                print("用法: read 文件名")
        elif cmd[0] == "login":
            if len(cmd) > 1:
                fs.login(cmd[1])
            else:
                print("用法: login 用户名")
        elif cmd[0] == "exit":
            break
        else:
            print("未知命令。")

if __name__ == "__main__":
    main()