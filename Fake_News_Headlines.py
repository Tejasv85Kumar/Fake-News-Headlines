import streamlit as st
import csv
import random

sub, act_with_obj, act_with_places, obj, places = [], [], [], [], []

with open("Dataset_FNH.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sub.append(row["subjects"])
        act_with_obj.append(row["act_with_objects"])
        act_with_places.append(row["act_with_places"])
        obj.append(row["objects"])
        places.append(row["places"])

#Generate headline 
def generate_headline():
    if random.choice([True, False]):
        return f"{random.choice(sub)} {random.choice(act_with_obj)} {random.choice(obj)}"
    else:
        return f"{random.choice(sub)} {random.choice(act_with_places)} {random.choice(places)}"


st.title(" Fake News Headline Generator")

st.text("")
st.write("Choose the number of Headlines you want")


num = st.slider("Number of headlines", 1, 10, 1)
if st.button("Generate Headlines"):
    for i in range(num):
        st.write(f"->{generate_headline()}")

st.write("Note:- To generate new headlines again click on 'Genrate Headlines' ")

