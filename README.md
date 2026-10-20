\# Đề tài: Tìm hiểu thuật toán Random Forest và xây dựng hệ thống phân loại phân khúc giá nhà Hà Nội



\## 1. Giới thiệu đề tài



Dự án tìm hiểu thuật toán học máy Random Forest và ứng dụng thuật toán để phân loại phân khúc giá nhà tại Hà Nội dựa trên các đặc trưng của bất động sản.



Hệ thống cung cấp giao diện web cho phép người dùng nhập thông tin căn nhà và nhận kết quả phân loại bằng mô hình Random Forest đã huấn luyện.



\## 2. Mục tiêu



\- Tìm hiểu nguyên lý hoạt động của thuật toán Random Forest.

\- Tiền xử lý và phân tích dữ liệu nhà ở Hà Nội.

\- Xây dựng mô hình phân loại phân khúc giá nhà.

\- Đánh giá hiệu quả mô hình bằng các chỉ số phân loại.

\- Xây dựng giao diện web để thử nghiệm mô hình.



\## 3. Công nghệ sử dụng



\- \*\*Python:\*\* ngôn ngữ lập trình chính.

\- \*\*Pandas, NumPy:\*\* xử lý dữ liệu.

\- \*\*Scikit-learn:\*\* tiền xử lý dữ liệu, huấn luyện và đánh giá mô hình.

\- \*\*Joblib:\*\* lưu và tải mô hình đã huấn luyện.

\- \*\*Streamlit:\*\* xây dựng giao diện web.



\## 4. Các phân khúc giá



Dự án sử dụng các ngưỡng phân loại theo quy ước:



| Phân khúc | Khoảng giá |

|---|---|

| Bình dân | Không quá 2 tỷ đồng |

| Trung cấp | Trên 2 đến 5 tỷ đồng |

| Cao cấp | Trên 5 đến 10 tỷ đồng |

| Hạng sang | Trên 10 tỷ đồng |



Các ngưỡng trên phục vụ mục đích thực nghiệm của dự án, không phải tiêu chuẩn định giá chính thức.



\## 5. Cấu trúc dự án



\- `app.py`: mã nguồn giao diện ứng dụng.

\- `requirements.txt`: danh sách thư viện Python cần cài đặt.

\- `house\_price\_rf\_bundle.joblib`: mô hình đã huấn luyện và thông tin tiền xử lý.

\- `Random\_Forest\_Phan\_Loai\_Gia\_Nha\_Ha\_Noi.ipynb`: notebook phân tích dữ liệu, huấn luyện và đánh giá mô hình.

\- `VN\_housing\_dataset.csv`: dữ liệu nhà ở sử dụng trong dự án, nếu được cung cấp trong repository.



\## 6. Cài đặt và chạy ứng dụng



\### Yêu cầu



Cài đặt Python tương thích với phiên bản Scikit-learn được sử dụng khi huấn luyện mô hình.



\### Bước 1: Tải mã nguồn



```bash

git clone https://github.com/26th09/KPDL.git

cd KPDL

```



\### Bước 2: Tạo môi trường ảo



Trên Windows:



```bat

python -m venv .venv

.venv\\Scripts\\activate

```



\### Bước 3: Cài đặt thư viện



```bash

python -m pip install -r requirements.txt

```



\### Bước 4: Chạy ứng dụng



```bash

python -m streamlit run app.py

```



Mở trình duyệt tại địa chỉ:



`http://localhost:8501`



\## 7. Quy trình hoạt động



1\. Thu thập và đọc dữ liệu nhà ở.

2\. Tiền xử lý dữ liệu và lựa chọn đặc trưng.

3\. Chia dữ liệu thành tập huấn luyện và tập kiểm tra.

4\. Huấn luyện mô hình Random Forest.

5\. Đánh giá mô hình bằng Accuracy, Precision, Recall và F1-score.

6\. Lưu mô hình đã huấn luyện.

7\. Sử dụng giao diện Streamlit để nhập thông tin và dự đoán phân khúc giá.



\## 8. Hạn chế



Kết quả phân loại phụ thuộc vào chất lượng, phạm vi và cách phân bố của dữ liệu huấn luyện. Kết quả dự đoán chỉ mang tính tham khảo, không thay thế việc định giá bất động sản chuyên nghiệp.



\## 9. Repository



Mã nguồn dự án: https://github.com/26th09/KPDL

