import streamlit as st
import numpy as np


st.title("家計診断アプリ")
st.write("あなたの家計は貯まる家計？減る家計？")
st.write("家計簿を出して、始めましょう！")

st.write("手順")
st.write("１．家計簿を出す")
st.write("２．月を選ぶ")
st.write("３．左側の費目別入力欄の各費目にその月の収入／支出額を入力する")
st.write("４．毎月発生しない費目は、発生した月から１年間同額を入力する")
st.write("　   →月額にならして計算するため（月額は自動計算）")
st.write("５．発生した全費目を入力したら、『総合計を表示』ボタンを押す")
st.write("※各支出カテゴリーごとの合計も表示可能")

month = st.selectbox("何月の家計ですか？",
 ["１月", "２月", "３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"],
 index = 0, placeholder = "月を選択する")
st.sidebar.title("費目別入力欄")
st.sidebar.write(f"{month}の収支内訳を入力してください")


income1 = st.sidebar.number_input("収入１",0)
income2 = st.sidebar.number_input("収入２",0)
income3 = st.sidebar.number_input("その他収入",0)
if st.sidebar.button("収入合計"):
  allincome = income1 + income2 + income3
  f_allincome = f"{allincome:,}"
  st.write(f"収入合計 : {f_allincome}円")

st.sidebar.write("支出")
st.sidebar.write("カテゴリー１：毎月発生／固定費")
rent = st.sidebar.number_input("住宅関連費",0)
comm = st.sidebar.number_input("通信費",0)
ins_m = st.sidebar.number_input("保険（月払い）",0)
lessons = st.sidebar.number_input("習い事",0)
school = st.sidebar.number_input("学校関連費",0)
subsc_m= st.sidebar.number_input("サブスク（月払い）",0)
others1 = st.sidebar.number_input("その他１",0)
if st.sidebar.button("支出１合計"):
  expense1 = rent + comm + ins_m + lessons + school + subsc_m + others1
  f_expense1 = f"{expense1:,}"
  st.write(f"支出１合計 : {f_expense1}円")

st.sidebar.write("カテゴリー２：毎月発生／変動費")
grocery = st.sidebar.number_input("食費",0)
cons = st.sidebar.number_input("日用消耗品費",0)
utility = st.sidebar.number_input("水道光熱費",0)
clothes = st.sidebar.number_input("被服費",0)
medical = st.sidebar.number_input("医療費",0)
vehicle = st.sidebar.number_input("車関連費",0)
care = st.sidebar.number_input("美容",0)
others2 = st.sidebar.number_input("その他２",0)
if st.sidebar.button("支出２合計"):
  expense2 = grocery + cons + utility + clothes + medical + vehicle + care + others2
  f_expense2 = f"{expense2:,}"
  st.write(f"支出２合計:{f_expense2}円")
 
st.sidebar.write("カテゴリー３：毎年発生／固定費")
ins_y = st.sidebar.number_input("保険（年払い）",0)
tax = st.sidebar.number_input("税金",0)
NHK = st.sidebar.number_input("ＮＨＫ",0)
subsc_y = st.sidebar.number_input("サブスク（年払い）",0)
shaken = st.sidebar.number_input("車検(2年)",0)
others3 = st.sidebar.number_input("その他３",0)
if st.sidebar.button("支出３合計"):
  expense3 = (ins_y + tax + NHK + subsc_y+ others3) / 12 + shaken / 24
  r_expense3 = np.round(expense3, 1)
  f_expense3 = f"{r_expense3:,}"
  st.write(f"支出３合計:{f_expense3}円")

st.sidebar.write("カテゴリー４：不定期／変動費")
furniture = st.sidebar.number_input("家具・家電",0)
leasure = st.sidebar.number_input("レジャー",0)
hospital = st.sidebar.number_input("病気",0)
entert = st.sidebar.number_input("交際",0)
grad_ent = st.sidebar.number_input("卒業・入学",0)
others4 = st.sidebar.number_input("その他４",0)
if st.sidebar.button("支出４合計"):
  expense4 = furniture + leasure + hospital + entert + grad_ent + others4
  r_expense4 = np.round(expense4, 1)
  f_expense4 = f"{r_expense4:,}"
  st.write(f"支出４合計:{f_expense4}円")

st.write(f"{month}の家計は・・・？")

if st.sidebar.button("総合計を表示"):
    allincome = income1 + income2 + income3
    f_allincome = f"{allincome:,}"
    expense1 = rent + comm + ins_m + lessons + school + subsc_m + others1
    f_expense1 = f"{expense1:,}"
    expense2 = grocery + cons + utility + clothes + medical + vehicle + care + others2
    f_expense2 = f"{expense2:,}"
    expense3 = (ins_y + tax + NHK + subsc_y+ others3) / 12 + shaken / 24
    r_expense3 = np.round(expense3, 1)
    f_expense3 = f"{r_expense3:,}"
    expense4 = (furniture + leasure + hospital + entert + grad_ent + others4) / 12
    r_expense4 = np.round(expense4, 1)
    f_expense4 = f"{r_expense4:,}"

    allexpenses = expense1 + expense2 + r_expense3 + r_expense4
    r_allexpenses = np.round(allexpenses, 0)
    f_allexpenses = f"{r_allexpenses:,}"
    balance = allincome - allexpenses
    r_balance = np.round(balance, 0)
    f_balance = f"{r_balance:,}"
    ratio = allexpenses / allincome * 100
    r_ratio = np.round(ratio, 1)
    saving = 100 - r_ratio
    r_saving = np.round(saving, 1)


    st.write(f"収入合計: {f_allincome}円")
   
    st.write(f"支出１（毎月発生、固定費）合計: {f_expense1}円")
    st.write(f"支出２（毎月発生、変動費）合計: {f_expense2}円")
    st.write(f"支出３（毎年発生、固定費）合計: {f_expense3}円")
    st.write(f"支出４（不定期発生、変動費）合計: {f_expense4}円")
    
    st.write(f"支出総合計: {f_allexpenses}円")
   
    st.write(f"収支差額: {f_balance}円")
    st.write(f"貯蓄率: {r_saving}%")


    if saving >= 20:
      st.write("素晴らしい。その調子！")
      st.image = "banzai_boy.png"
    elif saving >=5:
      st.write("いい感じ。理想の家計はすぐそこ！")
    elif saving >= 0:
      st.write("ぎりぎりセーフ")
    else:
      st.write("赤字！見直しが必要です！！")





