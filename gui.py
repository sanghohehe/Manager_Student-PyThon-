import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from student_manager import StudentManager
from student import Student

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Quản lý Sinh viên")
        self.manager = StudentManager()

        # --- Form ---
        form_frame = tk.LabelFrame(root, text="Thông tin sinh viên")
        form_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(form_frame, text="Mã SV").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id = tk.Entry(form_frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Họ tên").grid(row=1, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(form_frame)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Tuổi").grid(row=2, column=0, padx=5, pady=5)
        self.entry_age = tk.Entry(form_frame)
        self.entry_age.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Ngành").grid(row=3, column=0, padx=5, pady=5)
        self.entry_major = tk.Entry(form_frame)
        self.entry_major.grid(row=3, column=1, padx=5, pady=5)

        # --- Buttons ---
        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Thêm", command=self.add_student).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Cập nhật", command=self.update_student).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Xóa", command=self.delete_student).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Xóa form", command=self.clear_form).grid(row=0, column=3, padx=5)

        # --- Table ---
        table_frame = tk.LabelFrame(root, text="Danh sách sinh viên")
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        columns = ("id", "name", "age", "major", "gpa")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, width=100)
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_select_student)

        # --- Course Button ---
        tk.Button(root, text="➕ Thêm môn học cho sinh viên", command=self.add_course).pack(pady=5)

        self.load_students()

   
