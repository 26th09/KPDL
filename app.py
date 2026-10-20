import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Phân loại giá nhà Hà Nội", page_icon="🏠", layout="wide")
st.title("🏠 Hệ thống phân loại phân khúc giá nhà Hà Nội")
st.caption("Mô hình Random Forest được huấn luyện từ dữ liệu nhà đất đã cung cấp.")

MODEL_PATH = "house_price_rf_bundle.joblib"

@st.cache_resource
def load_bundle(path):
    return joblib.load(path)

if not os.path.exists(MODEL_PATH):
    st.error(f"Không tìm thấy {MODEL_PATH}. Hãy chạy notebook trước và đặt file mô hình cùng thư mục với app.py.")
    st.stop()

bundle = load_bundle(MODEL_PATH)
model = bundle["model"]
feature_columns = bundle["feature_columns"]
numeric_features = bundle.get("numeric_features", [])
metrics = bundle.get("metrics", {})

with st.sidebar:
    st.header("Thông tin mô hình")
    st.write("Thuật toán: Random Forest")
    st.write(f"Số đặc trưng: {len(feature_columns)}")
    st.write("Bình dân: dưới 2 tỷ")
    st.write("Trung cấp: 2 đến dưới 5 tỷ")
    st.write("Cao cấp: 5 đến 10 tỷ")
    st.write("Hạng sang: trên 10 tỷ")
    st.caption("Đây là quy ước phục vụ bài tập, không phải định giá chuyên nghiệp.")
    st.subheader("Kết quả trên tập kiểm tra")
    st.metric("Accuracy", f"{metrics.get('accuracy', 0):.3f}")
    st.metric("Macro F1", f"{metrics.get('f1_macro', 0):.3f}")

st.subheader("Nhập thông tin bất động sản")
st.write("Các trường hiển thị tương ứng với đặc trưng được sử dụng trong notebook. Có thể để trống trường không biết; mô hình sẽ xử lý giá trị thiếu.")
values = {}
cols = st.columns(2)

for idx, col_name in enumerate(feature_columns):
    with cols[idx % 2]:
        if col_name in numeric_features:
            raw = st.text_input(f"{col_name} (số)", value="", placeholder="Nhập giá trị số", key=f"num_{col_name}")
            if raw.strip() == "":
                values[col_name] = np.nan
            else:
                try:
                    values[col_name] = float(raw.replace(",", "."))
                except ValueError:
                    st.warning(f"'{col_name}' cần là số; tạm để trống.")
                    values[col_name] = np.nan
        else:
            raw = st.text_input(f"{col_name} (văn bản)", value="", placeholder="Nhập giá trị nếu biết", key=f"cat_{col_name}")
            values[col_name] = raw if raw.strip() else np.nan

if st.button("Dự đoán phân khúc", type="primary", use_container_width=True):
    input_df = pd.DataFrame([{c: values.get(c, np.nan) for c in feature_columns}])
    for c in numeric_features:
        input_df[c] = pd.to_numeric(input_df[c], errors="coerce")
    prediction = model.predict(input_df)[0]
    st.success(f"Phân khúc dự đoán: {prediction}")
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_df)[0]
        result = pd.DataFrame({"Phân khúc": model.classes_, "Xác suất mô hình": probabilities})
        result = result.sort_values("Xác suất mô hình", ascending=False)
        result["Xác suất mô hình"] = result["Xác suất mô hình"].map(lambda x: f"{x:.1%}")
        st.subheader("Xác suất theo phân khúc")
        st.dataframe(result, use_container_width=True, hide_index=True)
    st.info("Kết quả là phân loại theo dữ liệu lịch sử, không phải giá thẩm định hay lời khuyên đầu tư.")

st.divider()
st.subheader("Giới thiệu")
st.write("Ứng dụng phân loại bất động sản bằng Random Forest. Cột giá không được dùng làm đầu vào vì giá là cơ sở tạo nhãn.")
