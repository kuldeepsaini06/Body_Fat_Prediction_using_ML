import streamlit as st
import joblib

def main():
    
    html_temp="""
    <div style="background-color :gray;padding:10px">
    <h2 style= "color:black";text-align:center> Body Fat Prediction using Machine learning</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model= joblib.load('Random_forest_model')
    
    p1= st.slider("Density determined from underwater weighing",min_value=0.995,max_value=1.1089)
    p2=st.slider("Abdomen 2 circumference (cm)",min_value=69.0,max_value=149.0)
    p3= st.slider("Chest circumference (cm)",min_value=79.0,max_value=137.0)
    p4= st.slider("Hip(cm)",min_value=85.0,max_value=148.0)
    p5= st.slider("Weight(lbs)",min_value=29.0,max_value=78.0) 
        
       
        
    if st.button("Predict"):
        result=model.predict([[p1,p2,p3,p4,p5]])
        
        st.balloons()
        
        st.success("BodyFat {}".format(round(result[0],2)))
        
    
if __name__ == '__main__':
    main()