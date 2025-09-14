## Mục tiêu

- Quản lý sinh viên (CRUD: thêm, sửa, xóa, tìm kiếm).
- Tính GPA, xếp loại học lực.
- Lưu trữ dữ liệu JSON/CSV.
- Giao diện trực quan bằng **Tkinter**: form nhập, bảng hiển thị, nút bấm.



manager_student/
│
├── person.py
├── student.py
├── course.py
├── student_manager.py   # Quản lý thêm/xóa/sửa/tìm sinh viên
├── storage.py           # Đọc/ghi dữ liệu JSON
├── gui.py               # Giao diện Tkinter
├── data.json            # File lưu dữ liệu
└── main.py              # Điểm khởi chạy



![UML](manager_student_UML.png)
