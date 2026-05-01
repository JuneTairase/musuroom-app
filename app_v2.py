import streamlit as st
import joblib
import pandas as pd

model = joblib.load('mushroom_model.pkl')
encoders = joblib.load('encoders.pkl')

st.title('きのこ毒判定アプリ')
st.caption('きのこの特徴を選んで「判定する」ボタンを押すと毒か食用かが％で表示されます。')
st.divider()

options = {
    'cap-shape':                {'凸型': 'x', 'ベル型': 'b', 'くぼみ型': 's', '平型': 'f', '丸型': 'k', '円錐型': 'c'},
    'cap-surface':              {'滑らか': 's', 'ざらざら': 'y', '繊維質': 'f', '溝あり': 'g'},
    'cap-color':                {'茶色': 'n', '黄色': 'y', '白': 'w', '灰色': 'g', 'えんじ色': 'e', 'ピンク': 'p', '青': 'b', '紫': 'u', 'シナモン': 'c', '赤': 'r'},
    'bruises':                  {'あり': 't', 'なし': 'f'},
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

user_input = {}

st.subheader('傘の特徴')
col1, col2, col3, col4 = st.columns(4)
with col1:
    jp = st.selectbox('傘の形', list(options['cap-shape'].keys()))
    user_input['cap-shape'] = options['cap-shape'][jp]
with col2:
    jp = st.selectbox('傘の表面', list(options['cap-surface'].keys()))
    user_input['cap-surface'] = options['cap-surface'][jp]
with col3:
    jp = st.selectbox('傘の色', list(options['cap-color'].keys()))
    user_input['cap-color'] = options['cap-color'][jp]
with col4:
    jp = st.selectbox('傷はあるか', list(options['bruises'].keys()))
    user_input['bruises'] = options['bruises'][jp]

st.subheader('においの特徴')
col1, col2 = st.columns([1, 3])
with col1:
    jp = st.selectbox('におい', list(options['odor'].keys()))
    user_input['odor'] = options['odor'][jp]

st.subheader('ひだの特徴')
col1, col2, col3, col4 = st.columns(4)
with col1:
    jp = st.selectbox('ひだの付き方', list(options['gill-attachment'].keys()))
    user_input['gill-attachment'] = options['gill-attachment'][jp]
with col2:
    jp = st.selectbox('ひだの間隔', list(options['gill-spacing'].keys()))
    user_input['gill-spacing'] = options['gill-spacing'][jp]
with col3:
    jp = st.selectbox('ひだの大きさ', list(options['gill-size'].keys()))
    user_input['gill-size'] = options['gill-size'][jp]
with col4:
    jp = st.selectbox('ひだの色', list(options['gill-color'].keys()))
    user_input['gill-color'] = options['gill-color'][jp]

st.subheader('茎の特徴')
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    jp = st.selectbox('茎の形', list(options['stalk-shape'].keys()))
    user_input['stalk-shape'] = options['stalk-shape'][jp]
with col2:
    jp = st.selectbox('つばより上の表面', list(options['stalk-surface-above-ring'].keys()))
    user_input['stalk-surface-above-ring'] = options['stalk-surface-above-ring'][jp]
with col3:
    jp = st.selectbox('つばより下の表面', list(options['stalk-surface-below-ring'].keys()))
    user_input['stalk-surface-below-ring'] = options['stalk-surface-below-ring'][jp]
with col4:
    jp = st.selectbox('つばより上の色', list(options['stalk-color-above-ring'].keys()))
    user_input['stalk-color-above-ring'] = options['stalk-color-above-ring'][jp]
with col5:
    jp = st.selectbox('つばより下の色', list(options['stalk-color-below-ring'].keys()))
    user_input['stalk-color-below-ring'] = options['stalk-color-below-ring'][jp]

st.subheader('つばの特徴')
# veil-typeは選択肢が1種類のみのため固定値を設定
user_input['veil-type'] = 'p'

col1, col2, col3 = st.columns(3)
with col1:
    jp = st.selectbox('つばの色', list(options['veil-color'].keys()))
    user_input['veil-color'] = options['veil-color'][jp]
with col2:
    jp = st.selectbox('つばの数', list(options['ring-number'].keys()))
    user_input['ring-number'] = options['ring-number'][jp]
with col3:
    jp = st.selectbox('つばの形', list(options['ring-type'].keys()))
    user_input['ring-type'] = options['ring-type'][jp]

st.subheader('その他の特徴')
col1, col2, col3 = st.columns(3)
with col1:
    jp = st.selectbox('胞子紋の色', list(options['spore-print-color'].keys()))
    user_input['spore-print-color'] = options['spore-print-color'][jp]
with col2:
    jp = st.selectbox('群生の状態', list(options['population'].keys()))
    user_input['population'] = options['population'][jp]
with col3:
    jp = st.selectbox('生育場所', list(options['habitat'].keys()))
    user_input['habitat'] = options['habitat'][jp]

st.divider()
if st.button('🔍 判定する', use_container_width=True):
    input_df = pd.DataFrame([user_input])
    for col in input_df.columns:
        input_df[col] = encoders[col].transform(input_df[col])

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0]

    if prediction[0] == 1:
        st.error(f'⚠️ このきのこは毒がある可能性があります！食べない方が良いです')
        st.progress(probability[1], text=f'毒きのこの確率：{probability[1]*100:.1f}%')
        st.progress(probability[0], text=f'食用きのこの確率：{probability[0]*100:.1f}%')
    else:
        st.success(f'✅ このきのこは食べても大丈夫そうですが、最後は自己責任でお願いします')
        st.progress(probability[0], text=f'食用きのこの確率：{probability[0]*100:.1f}%')
        st.progress(probability[1], text=f'毒きのこの確率：{probability[1]*100:.1f}%')