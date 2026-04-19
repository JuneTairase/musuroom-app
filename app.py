import streamlit as st
import joblib
import pandas as pd

# モデルとエンコーダーの読み込み
model = joblib.load('mushroom_model.pkl')
encoders = joblib.load('encoders.pkl')

st.title('🍄 きのこ毒判定アプリ')
st.write('きのこの特徴を選んで「判定する」ボタンを押してください。')

# データの実際の値に基づいた正確な辞書
options = {
    'cap-shape':                {'ベル型': 'b', '円錐型': 'c', '平型': 'f', '丸型': 'k', 'くぼみ型': 's', '凸型': 'x'},
    'cap-surface':              {'繊維質': 'f', '溝あり': 'g', '滑らか': 's', 'ざらざら': 'y'},
    'cap-color':                {'青': 'b', 'シナモン': 'c', 'えんじ色': 'e', '灰色': 'g', '茶色': 'n', 'ピンク': 'p', '赤': 'r', '紫': 'u', '白': 'w', '黄色': 'y'},
    'bruises':                  {'なし': 'f', 'あり': 't'},
    'odor':                     {'アーモンド': 'a', 'クレオソート': 'c', '悪臭': 'f', 'アニス': 'l', 'カビ臭': 'm', 'なし': 'n', '毒臭': 'p', 'スパイシー': 's', '魚臭': 'y'},
    'gill-attachment':          {'付着': 'a', '離生': 'f'},
    'gill-spacing':             {'密': 'c', '疎': 'w'},
    'gill-size':                {'広い': 'b', '狭い': 'n'},
    'gill-color':               {'黄褐色': 'b', 'バフ': 'e', '灰色': 'g', 'チョコレート': 'h', '黒': 'k', '茶色': 'n', '橙': 'o', 'ピンク': 'p', '赤': 'r', '紫': 'u', '白': 'w', 'イエロー': 'y'},
    'stalk-shape':              {'広がる': 'e', '細くなる': 't'},
    'stalk-surface-above-ring': {'繊維質': 'f', 'シルク': 'k', '滑らか': 's', 'ざらざら': 'y'},
    'stalk-surface-below-ring': {'繊維質': 'f', 'シルク': 'k', '滑らか': 's', 'ざらざら': 'y'},
    'stalk-color-above-ring':   {'バフ': 'b', 'シナモン': 'c', '赤': 'e', '灰色': 'g', '茶色': 'n', 'オレンジ': 'o', 'ピンク': 'p', '白': 'w', '黄色': 'y'},
    'stalk-color-below-ring':   {'バフ': 'b', 'シナモン': 'c', '赤': 'e', '灰色': 'g', '茶色': 'n', 'オレンジ': 'o', 'ピンク': 'p', '白': 'w', '黄色': 'y'},
    'veil-type':                {'部分的': 'p'},
    'veil-color':               {'茶色': 'n', 'オレンジ': 'o', '白': 'w', '黄色': 'y'},
    'ring-number':              {'なし': 'n', '1つ': 'o', '2つ': 't'},
    'ring-type':                {'消失': 'e', '広がる': 'f', '大型': 'l', 'なし': 'n', '垂れ下がる': 'p'},
    'spore-print-color':        {'紫褐色': 'b', '茶緑色': 'h', '黒': 'k', '茶色': 'n', 'オレンジ': 'o', '緑': 'r', '紫': 'u', '白': 'w', '黄色': 'y'},
    'population':               {'豊富': 'a', '集まり': 'c', '多数': 'n', '散在': 's', '単独': 'v', '群生': 'y'},
    'habitat':                  {'森': 'd', '草地': 'g', '木の葉': 'l', '牧草地': 'm', '道端': 'p', '都市': 'u', '廃棄物': 'w'},
}

label_names = {
    'cap-shape': '傘の形',
    'cap-surface': '傘の表面',
    'cap-color': '傘の色',
    'bruises': '傷はあるか',
    'odor': 'におい',
    'gill-attachment': 'ひだの付き方',
    'gill-spacing': 'ひだの間隔',
    'gill-size': 'ひだの大きさ',
    'gill-color': 'ひだの色',
    'stalk-shape': '茎の形',
    'stalk-surface-above-ring': 'つばより上の茎の表面',
    'stalk-surface-below-ring': 'つばより下の茎の表面',
    'stalk-color-above-ring': 'つばより上の茎の色',
    'stalk-color-below-ring': 'つばより下の茎の色',
    'veil-type': 'つばの種類',
    'veil-color': 'つばの色',
    'ring-number': 'つばの数',
    'ring-type': 'つばの形',
    'spore-print-color': '胞子紋の色',
    'population': '群生の状態',
    'habitat': '生育場所',
}

# ユーザー入力
user_input = {}
for col, choices in options.items():
    jp_label = label_names[col]
    selected_jp = st.selectbox(jp_label, list(choices.keys()))
    user_input[col] = choices[selected_jp]

# 判定ボタン
if st.button('判定する'):
    input_df = pd.DataFrame([user_input])

    # 学習時のエンコーダーで変換
    for col in input_df.columns:
        input_df[col] = encoders[col].transform(input_df[col])

    # 予測
    prediction = model.predict(input_df)

    # 結果表示
    if prediction[0] == 1:
        st.error('⚠️ このきのこは【毒あり】の可能性があります！食べないでください！')
    else:
        st.success('✅ このきのこは【食用】の可能性があります。')