feat# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc:# Danh sách để lưu các công việc (mỗi công việc là một dictionary)
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách với trạng thái mặc định là False."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """Liệt kê tất cả các công việc kèm trạng thái hoàn thành."""
    print("\n--- Danh sách công việc ---")
    if not tasks:
        print("Danh sách trống.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{index}. {status} {task['name']}")

def complete_task(task_index):
    """Đánh dấu một công việc là đã hoàn thành dựa trên chỉ số (index)."""
    if task_index in range(len(tasks)):
        tasks[task_index]['completed'] = True
        print(f"Đã đánh dấu hoàn thành: '{tasks[task_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()
    complete_task(0)
    list_tasks() '{task_name}'")

def list_tasks():
    """Liệt kê tất cả các công việc hiện có."""
    print("\n--- Danh sách công việc ---")
    if not tasks:
        print("Danh sách trống.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks(): Implement function to list all tasks
