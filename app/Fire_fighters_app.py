import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from PIL import Image




# Read data
df_i_2022=pd.read_csv("oct23_bds_int_firefighters/data/raw/df_i_2022.csv")
df_m_2022=pd.read_csv("oct23_bds_int_firefighters/data/raw/df_m_2022.csv")
stations_boroughs=pd.read_csv("oct23_bds_int_firefighters/data/raw/stations_boroughs.csv")





# Sidebar title and page selection
st.sidebar.title("Table of Contents")
pages = ["Home","Introduction","Exploration", "Data Visualization", "Modelling", 
         "Find out for yourself", "Conclusion"]
page = st.sidebar.radio("Go to", pages)

# Display content based on the selected page
if page == "Home":
    # Insert Introduction contents here
    # App title
    st.title("London Fire Brigade Response Time 2023") 
    st.image("oct23_bds_int_firefighters/app/Lego_1.jpg", caption="How it take to the incident?", use_column_width=True)  
    st.write("#### The aim of this presentation is to give you an overview of our project, the modelling and the results. For further details, please refer to the detailed project report.")
    
    pass
elif page == "Introduction":
    # Insert Introduction contents here
    st.write("## Introduction")
    st.write("The London Fire Brigade is the busiest fire and rescue service in the UK and one of the largest fire and rescue organisations in the world.")
    st.write("### Description of the project:")
    st.write("#### Objective:")
    st.markdown("""
        - Analyze and/or estimate response times for the London Fire Brigade/n                       
    """)
    st.write("#### Datasets:")
    st.markdown("""
    - Incident records
      https://data.london.gov.uk/dataset/london-fire-brigade-incident-records 
    - Mobilisation records
      https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records 
    """)
    st.write("#### Little Quiz:")
    st.markdown("""
    - Which do you belive is the attendence time Goal of the London Fire Brigade?
    - What is the main factor that inflence the attendence time?
    """)
    pass
elif page == "Exploration":
    # Insert Exploration contents here
    st.write("## Exploration")
    st.write("The loaded and displayed data is an excerpt from the year 2022 to display the structure and fulfil the GitHub restriction.")
    st.write("### Incident data")
    st.write("The 'Incident data' essentially contained information about:")
    st.markdown("""
    - Attendence Time
    - Date and hour of call
    - Which fire ftation
    - Geo coordinates
    """)
    st.dataframe(df_i_2022.head(10))
    st.write(df_i_2022.shape)
    st.write("### Describe incident data")
    st.dataframe(df_i_2022.describe())
    
    if st.checkbox("Show NA Incident data") :
       st.dataframe(df_i_2022.isna().sum())
    
    st.write("### Mobilisation data")
    st.write("The 'Mobilisation data' essentially contained information about:")
    st.markdown("""
    - Turnout time
    - Travel Time
    - Attendence time
    - Delay discription
    """)   
    st.dataframe(df_m_2022.head(10))
    st.write(df_m_2022.shape)
    st.write("### Describe Mobilisation data")
    st.dataframe(df_m_2022.describe())
  
    if st.checkbox("Show NA Mobilisation Data") :
       st.dataframe(df_m_2022.isna().sum())
       
    st.write("### Stations & Boroughs")
    st.write("In order to calculate the distance between the fire stations and the location, we have researched the addresses of the current London fire stations and their geo-coordinates:")
    st.dataframe(stations_boroughs.head(10))
    
    st.write("")
    st.write("### Additional variables")
    st.write("In order to have more explanatory variables available, we have added the following variables:")
    st.markdown("""
    - Distance between fierstation and incidence
    - Distance between the centre of London and the firestation
    - Area of the boroughs
    - Population of the boroughs
    - Population density of the boroughs
    """) 
    st.write("")
    st.write("## Formulas for Distance calculation")
    st.image("oct23_bds_int_firefighters/app/Formula_distance_center.png", caption="Formula Distance Firestation from London center", use_column_width=True)
    st.image("oct23_bds_int_firefighters/app/Formula_distance_station.png", caption="Formula Distance Incident from Firestation", use_column_width=True)
    
        
    st.write("")
    st.write("### Deleted data")
    st.write("We have deleted variables that we did not need for our models.")
    st.markdown("""
    - Many variables were duplicated, e.g. Firestation and Firestation Code or Geo Coordinates. We deleted duplicate variables.
    - Some variables did not provide an explanation according to our first models. We have also deleted these.
    - We deleted rows with a small number of NaN (<5%).
    """) 
    
    st.write("")
    st.write("### Join data")
    st.write("To work with one data set, we have linked the mobilisation table and the incident table. The key for the join was the incident number. We only transferred data records where the incident number was present in both data records.")
    pass


elif page == "Data Visualization":
    # Insert DataViz contents here
    st.write("## Data Visualization")
    # Aufteilung in 3 Spalten und 2 Reihen
    col1, col2, col3 = st.columns(3)
    with col3:
        st.write("### Target")
        st.image("oct23_bds_int_firefighters/app/Plot_Firefighter_Seite_04_Bild_0001.png", 
                 caption="Here you can see the three histogramms for turnouttime, traveltime and attendancetime. ", 
                 use_column_width=True )
        st.image("oct23_bds_int_firefighters/app/Plot_Firefighter_Seite_13_Bild_0001.png", 
                 caption="Here you can see the three histogramms for turnouttime, traveltime and attendancetime. ", 
                 use_column_width=True )
        
        st.image("oct23_bds_int_firefighters/app/hour_of_call.png", 
                 caption="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 
                 use_column_width=True )
        st.image("oct23_bds_int_firefighters/app/Plot_Firefighter_Seite_07_Bild_0001.png", 
                 caption="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 
                 use_column_width=True )
    with col2:
        st.write("### Firestations")
        st.image("oct23_bds_int_firefighters/app/bourughs by incidents.png", 
                 caption="The capacity utilisation in the individual districts ranges from less than 20000 to almost 120000.", 
                 use_column_width=True )
        st.image("oct23_bds_int_firefighters/app/Plot_Firefighter_Seite_02_Bild_0001 Kopie.png", 
                 caption="The plot impressively illustrates how fire stations are opened and closed over the years.", 
                 use_column_width=True )
        st.image("oct23_bds_int_firefighters/app/Plot_Firefighter_Seite_05_Bild_0001 Kopie.png", 
                 caption="The capacity utilisation in the individual districts ranges from less than 20000 to almost 120000.", 
                 use_column_width=True )
        
    with col1:
        st.write("### London")
        st.image("oct23_bds_int_firefighters/app/Plot_Firefighter_Seite_18_Bild_0002 Kopie.png", 
                 caption="The charts show the Greater London area based on fire service operations and stations, provide a differentiated insight into the regional dynamics.",
                 use_column_width=True )
        st.image("oct23_bds_int_firefighters/app/Plot_Firefighter_Seite_19_Bild_0001.png", 
                 caption="The scatterplot makes it easy to recognise the locations. You even can make out individual streets. Or a diffenrence between inner or outer London", 
                 use_column_width=True )
        st.image("oct23_bds_int_firefighters/app/Plot_Firefighter_Seite_19_Bild_0002.png", 
                 caption="The scatterplot makes it easy to recognise the locations. You even can make out individual streets. Or a diffenrence between inner or outer London", 
                 use_column_width=True )
            
    pass


elif page == "Modelling":
    import joblib
    from sklearn.metrics import confusion_matrix, classification_report
  
    subpages = ["General Approach", "Regression with Random Forest", "Random Forest Classifier", "XGBoost Classifier"]
    subpage = st.sidebar.radio("Go to", subpages)

    if subpage == "General Approach":
      st.header('General Approach')
      st.markdown("""
      - Random splitting of the data with 20% allocated to the testing set
      - Regression Models and Classification Models 
                           
      """)

      st.write (' #### Approach in Regressinon Models')
      st.markdown("""
      - Performance measurement: $R^2$ - Value
      - Looking at Attendance Time as well as Turnout Time and Travel Time separately, where:
      """)
      st.latex(r""" \boxed{\text{Attendance Time} = \text{Turnout Time} + \text{Travel Time}} """)
      """ 
      - We explored various methodologies, including Linear Regression, Decision Tree Regressor, Random Forest Regressor, 
        and XGBoost Regressor, employing diverse feature configurations. The most promising results were achieved with the 
        Decision Tree and Random Forest Regressors.
      - To achieve better results with our top-performing model, we had to generate numerous dummy variables.
      """

      st.markdown(' #### Approach in Classification Models')
      st.markdown("""
      - Classification of the **response time** into 3-minute intervals and 4-minute intervals
      - Performance measurement: accuracy score (classification report) and confusion matrix   
      - Random Forest and XGBoost      
      """)

    if subpage == "Regression with Random Forest":
       st.markdown("""
       For the Random Forest model we used following variables 
       ```python
       features = 
          ['distance', 'HourOfCall', 'CalYear', 'FirstPumpArriving_DeployedFromStation', 
           'DeployedFromLocation', 'IncidentGroup', 'StopCodeDescription',
           'PropertyCategory', 'IncGeo_BoroughName','PlusCode_Description']  
        ```           
       All categorical variables were transformed into dummy variables, resulting together with other numerical variables in 166 explanatory columns in total.
       
       - TurnoutTimeSeconds (Random Forest):
         * Mean Squared Error (MSE): 1571.41
         * R-squared ($R^2$): 0.1448
       - TravelTimeSeconds (Random Forest):
         * Mean Squared Error (MSE): 11026.68
         * R-squared ($R^2$): 0.3933
       - AttendanceTimeSeconds (Random Forest):
         * Mean Squared Error (MSE): 11283.71
         * R-squared ($R^2$): 0.3953
          """)
      

    if subpage == "Random Forest Classifier":
      # Handle Random Forest Classifier section
      
       st.markdown(" ## Random Forest Classifier")
       # Markdown-Text
       st.markdown("""
       - We attempted to incorporate different features::
       ```python
       features = 
          ['distance', 'bor_sqkm', 'Month', 'DayOfWeek', 'distance_stat', 'pop', 
          'area_sqkm_stat', 'station', 'PropertyType', 'IncidentStationGround', 
          'FirstPumpArriving_DeployedFromStation', 'HourOfCall', 'CallsPerIncident']     
       ```
       - We conducted two distinct grid searches on one year of the data::
       ```python
       param_grid = {'n_estimators': [50, 100, 200],  
                     'max_depth': [None, 10, 20, 30],  
                     'min_samples_split': [2, 5, 10] }
              
       param_grid = {'bootstrap': [True],
                    'max_depth': [50, 75, 100],
                    'max_features': [2, 3],
                    'min_samples_leaf': [3, 4, 5],
                    'min_samples_split': [8, 10, 12],
                    'n_estimators': [200, 300, 500, 1000]}
           
       ```
       - We achieved the best results using the following set of hyperparameters and only 5 features:   
        ```python
        features = 
            ['HourOfCall', 'distance', 'distance_stat', 'pop_per_stat', 'bor_sqkm']
              
       params = 
           {max_depth=10, min_samples_split=5, n_estimators=200}   
       ```                      
       """)

       st.write(" ### Results:")
       selected_option = st.radio("Choose an option", ["3 minutes", "4 minutes"])

       if selected_option == "3 minutes":
        y_test = pd.read_csv('oct23_bds_int_firefighters/app/y_test_rf3.csv')
        y_pred = pd.read_csv('oct23_bds_int_firefighters/app/y_pred_rf3.csv')
        y_test_np = y_test.values.flatten()
        y_pred_np = y_pred.values.flatten()
        class_mapping = {1: '00-03min', 2: '03-06min', 3: '06-09min', 4: '09-12min', 5: '12-15min', 6: '> 15min'}  # und so weiter...
        # Umbenennung der Klassen in y_test und y_pred
        y_test_mapped = [class_mapping[y] for y in y_test_np]
        y_pred_mapped = [class_mapping[y] for y in y_pred_np]
        # Erstellung des classification reports mit den neuen Klassenbezeichnungen
        report = classification_report(y_test_mapped, y_pred_mapped)
        conf_matrix = confusion_matrix(y_test_np, y_pred_np)
        cm = pd.DataFrame(conf_matrix, columns=['0-3min', '3-6min', '6-9min', '9-12min', '12-15min', '>15min'],
                             index=['0-3min', '3-6min', '6-9min', '9-12min', '12-15min', '>15min'])
       if selected_option == '4 minutes':
        y_test = pd.read_csv('oct23_bds_int_firefighters/app/y_test_rf4.csv')
        y_pred = pd.read_csv('oct23_bds_int_firefighters/app/y_pred_rf4.csv')
        y_test_np = y_test.values.flatten()
        y_pred_np = y_pred.values.flatten()
        class_mapping = {1: '00-04min', 2: '04-08min', 3: '08-12min', 4: '12-16min', 5: '> 16min'}  # und so weiter...
        # Umbenennung der Klassen in y_test und y_pred
        y_test_mapped = [class_mapping[y] for y in y_test_np]
        y_pred_mapped = [class_mapping[y] for y in y_pred_np]
        # Erstellung des classification reports mit den neuen Klassenbezeichnungen
        report = classification_report(y_test_mapped, y_pred_mapped)    # output_mapped=True)
        conf_matrix = confusion_matrix(y_test_np, y_pred_np)
        cm = pd.DataFrame(conf_matrix, columns=['0-4min', '4-8min', '8-12min', '12-16min', '>16min'],
                           index=['0-4min', '4-8min', '8-12min', '12-16min', '>16min'])
    
       st.write(' ##### Classification Report')
       st.text(report)
       st.write(' ##### Confusion Matrix')
       st.write(cm)
    

    #XGBoost Classifier for 4min Classes, 5 features and trained on years 2020, 2021, 2022
    if subpage == "XGBoost Classifier":
      # Handle XGBoost Classifier section
     
       st.markdown(" ## XGBoost Classifier")
       # Markdown-Text
       st.markdown("""
       - We incorporated many different features::
       ```python
       features = [
           'CallsPerIncidents', 'distance', 'bor_sqkm', 'Month', 'DayOfWeek', 
           'distance_stat', 'pop', 'in_o_out', 'lat_cal_r', 'long_cal_r', 
           'area_sqkm_stat', 'station', 'SpecialServiceType', 'PropertyType', 
           'IncidentStationGround', 'FirstPumpArriving_DeployedFromStation', 
           'DateAndTimeMobilised', 'IncGeo_WardName']
       ```
       - We conducted two distinct grid searches on one year of the data::
       ```python
       param_grid = {
                      'n_estimators': [50, 200, 400, 600],  
                      'max_depth': [3, 5, 8,10],  
                      'learning_rate': [0.1, 0.2, 0.5, 0.8]  }
              
        param_grid = {
                      'n_estimators': [50, 100, 200, 400],
                      'max_depth': [3, 4, 5, 8],
                      'learning_rate': [0.01, 0.1, 0.2, 0.5] }

       ```
       - We achieved the best results with the following set of hyperparameters:   
       ```python              
       params = { 'n_estimators': 400, 'max_depth': 8,  'learning_rate': 0.1  } 
       ```                      
       """)

       st.write(" ### Results:")
       sel_option = st.radio("Choose an option", ["3 minutes", "4 minutes"], key="unique_key_here")

       if sel_option == "3 minutes":
        y_test = pd.read_csv('oct23_bds_int_firefighters/app/y_test_xgb3.csv')
        y_pred = pd.read_csv('oct23_bds_int_firefighters/app/y_pred_xgb3.csv')
        y_test_np = y_test.values.flatten()
        y_pred_np = y_pred.values.flatten()
        class_mapping = {0: '00-03min', 1: '03-06min', 2: '06-09min', 3: '09-12min', 4: '12-15min', 5: '> 15min'}  # und so weiter...
        # Umbenennung der Klassen in y_test und y_pred
        y_test_mapped = [class_mapping[y] for y in y_test_np]
        y_pred_mapped = [class_mapping[y] for y in y_pred_np]
       # Erstellung des classification reports mit den neuen Klassenbezeichnungen
        report = classification_report(y_test_mapped, y_pred_mapped)
        conf_matrix = confusion_matrix(y_test_np, y_pred_np)
        cm = pd.DataFrame(conf_matrix, columns=['0-3min', '3-6min', '6-9min', '9-12min', '12-15min', '>15min'],
                             index=['0-3min', '3-6min', '6-9min', '9-12min', '12-15min', '>15min'])
       if sel_option == '4 minutes':
        y_test = pd.read_csv('oct23_bds_int_firefighters/app/y_test_xgb4.csv')
        y_pred = pd.read_csv('oct23_bds_int_firefighters/app/y_pred_xgb4.csv')
        y_test_np = y_test.values.flatten()
        y_pred_np = y_pred.values.flatten()
        class_mapping = {0: '00-04min', 1: '04-08min', 2: '08-12min', 3: '12-16min', 4: '> 16min'}  # und so weiter...
        # Umbenennung der Klassen in y_test und y_pred
        y_test_mapped = [class_mapping[y] for y in y_test_np]
        y_pred_mapped = [class_mapping[y] for y in y_pred_np]
        # Erstellung des classification reports mit den neuen Klassenbezeichnungen
        report = classification_report(y_test_mapped, y_pred_mapped)    # output_mapped=True)
        conf_matrix = confusion_matrix(y_test_np, y_pred_np)
        cm = pd.DataFrame(conf_matrix, columns=['0-4min', '4-8min', '8-12min', '12-16min', '>16min'],
                             index=['0-4min', '4-8min', '8-12min', '12-16min', '>16min'])
    
       st.write(' ##### Classification Report')
       st.text(report)
       st.write(' ##### Confusion Matrix')
       st.write(cm)
    

if page == "Find out for yourself" : 
  import joblib
  from sklearn.metrics import confusion_matrix, classification_report
  #XGBoost Classifier for 4min Classes, 5 features and trained on years 2020, 2021, 2022
  st.subheader( "XGBoost Classifier trained and tested on 5 features using data from the years 2020, 2021, and 2022:")

  st.subheader('Select time intervals for the classification')
  selected_option = st.radio("Choose an option", ["3 minutes", "4minutes"])

  if selected_option == "3 minutes":
    minutes = 3
    st.write(" ### Results of the model for 3 minutes classification")
    xgb = joblib.load("oct23_bds_int_firefighters/app/XGB3kurzII.pkl")
    yt_xgb3 = pd.read_csv('oct23_bds_int_firefighters/app/yt_xgb3.csv')
    yp_xgb3 = pd.read_csv('oct23_bds_int_firefighters/app/yp_xgb3.csv')

    yt = yt_xgb3.values.flatten()
    yp = yp_xgb3.values.flatten()
    class_mapping = {0: '00-03min', 1: '03-06min', 2: '06-09min', 3: '09-12min', 4: '12-15min', 5: '> 15min'}  # und so weiter...
    # Umbenennung der Klassen in y_test und y_pred
    yt_mapped = [class_mapping[y] for y in yt]
    yp_mapped = [class_mapping[y] for y in yp]
    # Erstellung des classification reports mit den neuen Klassenbezeichnungen
    report = classification_report(yt_mapped, yp_mapped)
    st.write(' ##### Classification Report')
    st.text(report)

    conf_matrix = confusion_matrix(yt_xgb3, yp_xgb3)
    st.write(' ##### Confusion Matrix')
    st.write(pd.DataFrame(conf_matrix, columns=['0-3min', '3-6min', '6-9min', '9-12min', '12-15min', '> 15min'],
                           index=['0-3min', '3-6min', '6-9min', '9-12min', '12-15min', ' > 15min']))
  else:
    minutes = 4
    st.write(" ### Results of the model for 4 minutes classification")
    xgb = joblib.load("oct23_bds_int_firefighters/app/XGB4kurz.pkl")
    yt_xgb4 = pd.read_csv('oct23_bds_int_firefighters/app/yt_xgb4.csv')
    yp_xgb4 = pd.read_csv('oct23_bds_int_firefighters/app/yp_xgb4.csv')

    yt = yt_xgb4.values.flatten()
    yp = yp_xgb4.values.flatten()
    class_mapping = {0: '00-04min', 1: '04-08min', 2: '08-12min', 3: '12-16min', 4: '>16min'}  # und so weiter...
    # Umbenennung der Klassen in y_test und y_pred
    yt_mapped = [class_mapping[y] for y in yt]
    yp_mapped = [class_mapping[y] for y in yp]
    # Erstellung des classification reports mit den neuen Klassenbezeichnungen
    report = classification_report(yt_mapped, yp_mapped)
    st.write(' ##### Classification Report')
    st.text(report)

    conf_matrix = confusion_matrix(yt_xgb4, yp_xgb4)
    st.write(' ##### Confusion Matrix')
    st.write(pd.DataFrame(conf_matrix, columns=['0-4min', '4-8min', '8-12min', '12-16min', '>16min'],
                           index=['0-4min', '4-8min', '8-12min', '12-16min', '>16min']))


  from geopy.geocoders import Nominatim
  from geopy.distance import geodesic
  #import streamlit as st
  #import pandas as pd
  import datetime
  from datetime import datetime
  import pytz
  

  sb = pd.read_csv("oct23_bds_int_firefighters/app/sb.csv")
  # Streamlit App
  st.subheader('Find Nearest Fire Stations')

  # Input field for the address
  address = st.text_input('Enter an address in London:')

  if address:
    # Check if the address contains "London"
    if "London" not in address:
        st.write("Please enter an address in London.")
    else:
        # Initialize geocoder and restrict to London
        geolocator = Nominatim(user_agent="my_geocoder")
        geolocator.headers = {"accept-language": "en-US,en;q=0.5"}
        geolocator.country_bias = "United Kingdom"
        #geolocator.view_box = (-0.510375, 51.286760, 0.334015, 51.691874)  # London area
        geolocator.view_box = (-1.0, 51.0, 1.0, 52.0)
        #(min_lon, min_lat, max_lon, max_lat) angeordnet:
        #min_lon: Minimale Längengradposition (westlichster Punkt)
        #min_lat: Minimale Breitengradposition (südlichster Punkt)
        #max_lon: Maximale Längengradposition (östlichster Punkt)
        #max_lat: Maximale Breitengradposition (nördlichster Punkt)
        # Attempt to retrieve coordinates
        try:
            location = geolocator.geocode(address)
            if location:
                st.subheader('Coordinates of the given adress:')
                st.write('Latitude:', location.latitude)
                st.write('Longitude:', location.longitude)
                
                            
                # Adress coordinates (Latitude, Longitude)
                address_coords = (location.latitude, location.longitude)

                # Function for calculating distance between address and firestation
                def calculate_distance(coords1, coords2):
                    return geodesic(coords1, coords2).meters  # Entfernung in Metern

                # Calculating distance between address and firestation
                #sb['distance'] = sb.apply(lambda row: calculate_distance(address_coords, (row['lat'], row['long'])), axis=1)
                sb['distance'] = sb.apply(lambda row: round(calculate_distance(address_coords, (row['lat'], row['long'])), 3), axis=1)

                # find 3 nearest stations 
                nearest_fire_stations = sb.nsmallest(3, 'distance')
                #st.dataframe(nearest_fire_stations)

                # names of the 3 nearest firestations
                st.subheader(" Three nearest firestations are:")
                for idx, station in nearest_fire_stations.iterrows():
                    st.markdown(f"**{station['stat'] }** in borough **{station['borough']}** - Distance to the given adress: **{station['distance']} meters**")
                
            else:
                st.write('Address not found in London.')
        except Exception as e:
            st.write('Error retrieving coordinates:', e)
    
    st.subheader('Select time option: ')
    selected_option = st.radio("Choose an option", ["Use current time", "Use time of your choice"])

    if selected_option == "Use current time":
        london_timezone = pytz.timezone('Europe/London')
        current_time = datetime.now(london_timezone)
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"Current time in London: {formatted_time}")
        current_hour = current_time.hour + 1
        st.write(f"Hour of Call: {current_hour}")
    else:
        # Input field for the hour of call
        st.write('Hour of Call is the complete hour plus 1. For example, if you make a call at 17:17, then the Hour of Call is 18.')
        current_hour = st.number_input("Enter the hour of call (0-23):", min_value=0, max_value=23, step=1)
        st.write(f"Selected hour of call: {current_hour}")

    nearest_fire_stations['HourOfCall'] = current_hour 
    
    st.subheader('Featurs for the three nearest firestationes')
    x = nearest_fire_stations[['HourOfCall', 'distance', 'distance_stat', 'pop_per_stat', 'bor_sqkm']]
    st.dataframe(x)

    xp = xgb.predict(x)
 
    def arrival_time_message(prediction):
        if minutes == 3:
            if prediction == 0:
                return '0 to 3 minutes'
            elif prediction == 1:
                 return '3 to 6 minutes'
            elif prediction == 2:
                return '6 to 9 minutes'
            elif prediction == 3:
                return '9 to 12 minutes'
            elif prediction == 4:
                return '12 to 15 minutes'
            else:
                return 'more than 15 minutes'
        else:
            if prediction == 0:
                return '0 to 4 minutes'
            elif prediction == 1:
                 return '4 to 8 minutes'
            elif prediction == 2:
                return '8 to 12 minutes'
            elif prediction == 3:
                return '12 to 16 minutes'
            else:
                return 'more than 16 minutes'    
            

    arrival_times = ['nearest', 'second nearest', 'third nearest']
    for i, time in enumerate(arrival_times):
       st.markdown(f"**If the {time} fire station sends the pump it should arrive within:**")
       st.write(arrival_time_message(xp[i]))
   
    pass

if page == "Conclusion" :
    # Insert Introduction contents here
    st.write("## Conclusion")
    st.write("### Empfehlungen an die Londoner Firebrigarde:")
    st.markdown("""
                #### From the data analysis:  
                **Open Firestations in the outer boroughs**  
                
                Firestations haben eine längere Reaktionszeit, wenn sie in Außenbezirken liegen.
                Vermutlich, weil das Gebiet, dass sie abdecken müssen größer ist und die Straßen 
                nicht so gut ausgebaut sind.
                Durch zusätzliche Firestations könnte man die Reaktionszeiten hier sicherlich verkürzen.
                Dies würde aber zusätzliche Kosten nach sich ziehen. Es scheint also eine Abwägung 
                zu sein zwischen kurzen Reaktionszeiten und Kosten. Außerdem gibt es hier weniger 
                Einsätze, da die Gebiete dünner besiedelt sind.
                  
                  
                **Launch an information campaign to reduce false alarms**
                
                An information campaign would definitely be worthwhile, as almost half of all alarms 
                are false alarms. This could certainly also reduce costs.
                
                #### From the prediction model:
                
                **Give Information about the expected response time**
                
                The prediction model could be installed at the emergency call centre.
                Callers could be told when they can expect the fire brigade to arrive.
                This could help to reassure callers.
                
                **Development of an app**
                
                The development of an app is conceivable so that the arrival time can be 
                predicted automatically by linking it to the mobile phone GPS.
                
                """)
 
    pass

#