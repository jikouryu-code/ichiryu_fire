import re

for word, desc in items.items():
    if search == "" or search in str(word) or search in desc:

        # 🔥表示用だけ加工（元データはそのまま）
        display_desc = re.sub(r"<[^>]+>", "", desc)

        st.write(f"{word[0]} × {word[1]}")
        st.write(display_desc)
